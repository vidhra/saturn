"""
Saturn Context Engine 
"""

import asyncio
import json
import os
import hashlib
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, asdict
from pathlib import Path
import re

from model.llm.base_interface import get_llm_interface


@dataclass
class Message:
    """Represents a single conversation message with metadata"""
    id: str
    role: str  # 'user', 'assistant', 'system'
    content: str
    timestamp: datetime
    tokens: int = 0
    importance_score: float = 0.0
    context_tags: List[str] = None
    
    def __post_init__(self):
        if self.context_tags is None:
            self.context_tags = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'role': self.role,
            'content': self.content,
            'timestamp': self.timestamp.isoformat(),
            'tokens': self.tokens,
            'importance_score': self.importance_score,
            'context_tags': self.context_tags
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        """Create from dictionary"""
        data['timestamp'] = datetime.fromisoformat(data['timestamp'])
        return cls(**data)


@dataclass
class ConversationSummary:
    """Compressed summary of conversation segments"""
    id: str
    timeframe: Tuple[datetime, datetime]
    summary: str
    key_topics: List[str]
    technical_context: Dict[str, Any]
    importance_score: float
    message_count: int
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'timeframe': [self.timeframe[0].isoformat(), self.timeframe[1].isoformat()],
            'summary': self.summary,
            'key_topics': self.key_topics,
            'technical_context': self.technical_context,
            'importance_score': self.importance_score,
            'message_count': self.message_count
        }


class ContextEngine:
    """
    Intelligent context compression engine inspired by Cursor.
    
    Features:
    - Smart relevance scoring based on current query
    - Technical context extraction (file names, commands, errors)
    - Conversation segment compression
    - Real-time context injection for LLM prompts
    - Persistent conversation storage
    """
    
    def __init__(self, working_directory: str = ".", config: Dict[str, Any] = None):
        self.working_directory = Path(working_directory)
        self.config = config or {}
        
        # Context storage
        self.conversations_dir = self.working_directory / ".saturn" / "conversations"
        self.conversations_dir.mkdir(parents=True, exist_ok=True)
        
        # Current session
        self.current_conversation_id = self._generate_conversation_id()
        self.messages: List[Message] = []
        self.summaries: List[ConversationSummary] = []
        
        # Configuration
        self.max_context_tokens = self.config.get('max_context_tokens', 8000)
        self.max_recent_messages = self.config.get('max_recent_messages', 10)
        self.min_importance_threshold = self.config.get('min_importance_threshold', 0.3)
        self.compression_threshold = self.config.get('compression_threshold', 20)
        
        # LLM interface for summarization
        self.llm_interface = None
        if config:
            self.llm_interface = get_llm_interface(config)
        
        # Context patterns for technical extraction
        self.technical_patterns = {
            'files': re.compile(r'(?:file|path|directory):\s*([^\s]+\.[a-zA-Z0-9]+)', re.IGNORECASE),
            'commands': re.compile(r'(?:run|execute|command):\s*`([^`]+)`', re.IGNORECASE),
            'errors': re.compile(r'(?:error|exception|failed):\s*([^\n]+)', re.IGNORECASE),
            'cloud_resources': re.compile(r'(?:gcp|aws|azure)[\s-]([a-zA-Z0-9-]+)', re.IGNORECASE),
            'operations': re.compile(r'(?:create|delete|update|deploy|list)\s+([a-zA-Z0-9-]+)', re.IGNORECASE)
        }
        
        # Performance optimizations
        self._context_cache = {}
        self._cache_expiry = {}
        self._cache_ttl = 60  # Cache context for 60 seconds
        
        # Load existing conversation if available
        self._load_current_conversation()
    
    def _generate_conversation_id(self) -> str:
        """Generate a unique conversation ID"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"conv_{timestamp}_{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}"
    
    def _estimate_tokens(self, text: str) -> int:
        """Rough token estimation (4 chars ≈ 1 token)"""
        return max(1, len(text) // 4)
    
    def _extract_technical_context(self, content: str) -> Dict[str, Any]:
        """Extract technical context from message content"""
        context = {}
        
        for pattern_name, pattern in self.technical_patterns.items():
            matches = pattern.findall(content)
            if matches:
                context[pattern_name] = list(set(matches))  # Remove duplicates
        
        return context
    
    def _calculate_importance_score(self, message: Message, current_query: str = None) -> float:
        """Calculate importance score for a message"""
        score = 0.0
        content = message.content.lower()
        
        # Base importance by role
        role_weights = {'user': 0.7, 'assistant': 0.8, 'system': 0.3}
        score += role_weights.get(message.role, 0.5)
        
        # Technical content gets higher scores
        technical_keywords = ['error', 'failed', 'success', 'created', 'deployed', 'command', 'file', 'config']
        for keyword in technical_keywords:
            if keyword in content:
                score += 0.1
        
        # Recent messages are more important
        age_hours = (datetime.now() - message.timestamp).total_seconds() / 3600
        recency_weight = max(0.1, 1.0 - (age_hours / 24))  # Decay over 24 hours
        score *= recency_weight
        
        # Relevance to current query
        if current_query:
            query_words = set(current_query.lower().split())
            content_words = set(content.split())
            relevance = len(query_words.intersection(content_words)) / max(len(query_words), 1)
            score += relevance * 0.5
        
        # Longer messages with technical content
        if len(content) > 100 and any(keyword in content for keyword in technical_keywords):
            score += 0.2
        
        return min(1.0, score)
    
    def add_message(self, role: str, content: str, context_tags: List[str] = None) -> Message:
        """Add a new message to the conversation"""
        message = Message(
            id=f"msg_{int(time.time() * 1000)}_{len(self.messages)}",
            role=role,
            content=content,
            timestamp=datetime.now(),
            tokens=self._estimate_tokens(content),
            context_tags=context_tags or []
        )
        
        # Extract technical context
        technical_context = self._extract_technical_context(content)
        if technical_context:
            message.context_tags.extend([f"tech:{k}" for k in technical_context.keys()])
        
        # Calculate importance score
        message.importance_score = self._calculate_importance_score(message)
        
        self.messages.append(message)
        
        # Auto-compress if we have too many messages (async to avoid blocking UI)
        if len(self.messages) > self.compression_threshold:
            # Use call_soon to avoid blocking the UI thread
            try:
                loop = asyncio.get_event_loop()
                loop.create_task(self._compress_old_messages())
            except RuntimeError:
                # Fallback if no event loop
                pass
        
        # Save conversation
        self._save_current_conversation()
        
        return message
    
    async def _compress_old_messages(self):
        """Compress old messages into summaries"""
        if len(self.messages) <= self.max_recent_messages:
            return
        
        # Keep recent messages, compress the rest
        recent_messages = self.messages[-self.max_recent_messages:]
        old_messages = self.messages[:-self.max_recent_messages]
        
        if old_messages and self.llm_interface:
            summary = await self._create_conversation_summary(old_messages)
            if summary:
                self.summaries.append(summary)
                self.messages = recent_messages
                self._save_current_conversation()
    
    async def _create_conversation_summary(self, messages: List[Message]) -> ConversationSummary:
        """Create a compressed summary of message segments"""
        if not messages:
            return None
        
        # Prepare content for summarization
        conversation_text = ""
        technical_context = {}
        key_topics = set()
        
        for msg in messages:
            conversation_text += f"{msg.role}: {msg.content}\n"
            
            # Collect technical context
            tech_ctx = self._extract_technical_context(msg.content)
            for key, values in tech_ctx.items():
                if key not in technical_context:
                    technical_context[key] = []
                technical_context[key].extend(values)
            
            # Extract key topics from tags
            key_topics.update(tag for tag in msg.context_tags if not tag.startswith('tech:'))
        
        # Generate summary using LLM
        summary_prompt = f"""
Summarize the following conversation segment, focusing on:
1. Key user goals and requests
2. Important technical details (file names, commands, errors)
3. Results and outcomes
4. Any ongoing context that might be relevant later

Conversation:
{conversation_text}

Provide a concise but technically complete summary:
"""
        
        try:
            response = await self.llm_interface.agenerate([
                {"role": "user", "content": summary_prompt}
            ])
            summary_text = response.choices[0].message.content.strip()
            
            # Calculate importance score based on technical content and user actions
            importance_score = sum(msg.importance_score for msg in messages) / len(messages)
            
            return ConversationSummary(
                id=f"summary_{int(time.time())}",
                timeframe=(messages[0].timestamp, messages[-1].timestamp),
                summary=summary_text,
                key_topics=list(key_topics),
                technical_context=technical_context,
                importance_score=importance_score,
                message_count=len(messages)
            )
        
        except Exception as e:
            print(f"Error creating summary: {e}")
            return None
    
    async def get_relevant_context(self, current_query: str, max_tokens: int = None) -> Dict[str, Any]:
        """
        Get relevant context for the current query, Cursor-style.
        Returns compressed context that includes only relevant information.
        """
        max_tokens = max_tokens or self.max_context_tokens
        context = {
            'recent_messages': [],
            'relevant_summaries': [],
            'technical_context': {},
            'total_tokens': 0
        }
        
        # Score all messages and summaries for relevance
        scored_messages = []
        for msg in self.messages:
            relevance_score = self._calculate_importance_score(msg, current_query)
            if relevance_score >= self.min_importance_threshold:
                scored_messages.append((msg, relevance_score))
        
        # Always include recent messages
        recent_count = min(self.max_recent_messages, len(self.messages))
        recent_messages = self.messages[-recent_count:]
        
        # Add recent messages first
        for msg in recent_messages:
            if context['total_tokens'] + msg.tokens <= max_tokens:
                context['recent_messages'].append({
                    'role': msg.role,
                    'content': msg.content,
                    'timestamp': msg.timestamp.isoformat(),
                    'importance': msg.importance_score
                })
                context['total_tokens'] += msg.tokens
        
        # Add relevant summaries if we have token budget
        for summary in sorted(self.summaries, key=lambda s: s.importance_score, reverse=True):
            summary_tokens = self._estimate_tokens(summary.summary)
            if context['total_tokens'] + summary_tokens <= max_tokens:
                context['relevant_summaries'].append({
                    'summary': summary.summary,
                    'timeframe': summary.timeframe,
                    'key_topics': summary.key_topics,
                    'importance': summary.importance_score
                })
                context['total_tokens'] += summary_tokens
                
                # Merge technical context
                for key, values in summary.technical_context.items():
                    if key not in context['technical_context']:
                        context['technical_context'][key] = []
                    context['technical_context'][key].extend(values)
        
        return context
    
    async def get_context_for_llm(self, current_query: str) -> List[Dict[str, str]]:
        """
        Format context for LLM prompt injection with caching for performance.
        Returns a list of messages to prepend to the conversation.
        """
        # Check cache first for performance
        cache_key = hashlib.md5(f"{current_query}_{len(self.messages)}".encode()).hexdigest()
        current_time = time.time()
        
        if (cache_key in self._context_cache and 
            cache_key in self._cache_expiry and 
            self._cache_expiry[cache_key] > current_time):
            return self._context_cache[cache_key]
        
        context = await self.get_relevant_context(current_query)
        
        llm_messages = []
        
        # Add technical context if available
        if context['technical_context']:
            tech_summary = "Recent technical context:\n"
            for key, values in context['technical_context'].items():
                if values:
                    unique_values = list(set(values))[:5]  # Limit to 5 most recent
                    tech_summary += f"- {key.title()}: {', '.join(unique_values)}\n"
            
            llm_messages.append({
                "role": "system",
                "content": tech_summary.strip()
            })
        
        # Add compressed summaries
        if context['relevant_summaries']:
            summary_content = "Previous conversation context:\n"
            for summary in context['relevant_summaries']:
                summary_content += f"\n{summary['summary']}\n"
            
            llm_messages.append({
                "role": "system", 
                "content": summary_content.strip()
            })
        
        # Cache the result for performance
        self._context_cache[cache_key] = llm_messages
        self._cache_expiry[cache_key] = current_time + self._cache_ttl
        
        return llm_messages
    
    def _save_current_conversation(self):
        """Save current conversation to disk"""
        conversation_file = self.conversations_dir / f"{self.current_conversation_id}.json"
        
        data = {
            'id': self.current_conversation_id,
            'created_at': datetime.now().isoformat(),
            'messages': [msg.to_dict() for msg in self.messages],
            'summaries': [summary.to_dict() for summary in self.summaries]
        }
        
        try:
            with open(conversation_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving conversation: {e}")
    
    def _load_current_conversation(self):
        """Load the most recent conversation"""
        try:
            conversation_files = list(self.conversations_dir.glob("conv_*.json"))
            if not conversation_files:
                return
            
            # Get the most recent conversation file
            latest_file = max(conversation_files, key=lambda f: f.stat().st_mtime)
            
            with open(latest_file, 'r') as f:
                data = json.load(f)
            
            self.current_conversation_id = data['id']
            self.messages = [Message.from_dict(msg) for msg in data.get('messages', [])]
            self.summaries = [ConversationSummary(**summary) for summary in data.get('summaries', [])]
            
        except Exception as e:
            print(f"Error loading conversation: {e}")
    
    def start_new_conversation(self) -> str:
        """Start a new conversation and return the ID"""
        # Save current conversation
        if self.messages:
            self._save_current_conversation()
        
        # Reset for new conversation
        self.current_conversation_id = self._generate_conversation_id()
        self.messages = []
        self.summaries = []
        
        return self.current_conversation_id
    
    def get_conversation_list(self) -> List[Dict[str, Any]]:
        """Get list of all conversations"""
        conversations = []
        
        for conv_file in self.conversations_dir.glob("conv_*.json"):
            try:
                with open(conv_file, 'r') as f:
                    data = json.load(f)
                
                conversations.append({
                    'id': data['id'],
                    'created_at': data['created_at'],
                    'message_count': len(data.get('messages', [])),
                    'last_message': data.get('messages', [])[-1]['content'][:100] if data.get('messages') else '',
                    'file_path': str(conv_file)
                })
            except Exception as e:
                print(f"Error reading conversation {conv_file}: {e}")
        
        return sorted(conversations, key=lambda c: c['created_at'], reverse=True)
    
    def load_conversation(self, conversation_id: str) -> bool:
        """Load a specific conversation by ID"""
        conversation_file = self.conversations_dir / f"{conversation_id}.json"
        
        if not conversation_file.exists():
            return False
        
        try:
            with open(conversation_file, 'r') as f:
                data = json.load(f)
            
            self.current_conversation_id = data['id']
            self.messages = [Message.from_dict(msg) for msg in data.get('messages', [])]
            self.summaries = [ConversationSummary(**summary) for summary in data.get('summaries', [])]
            
            return True
        except Exception as e:
            print(f"Error loading conversation {conversation_id}: {e}")
            return False
    
    def get_context_stats(self) -> Dict[str, Any]:
        """Get statistics about the current context"""
        total_tokens = sum(msg.tokens for msg in self.messages)
        recent_messages = len(self.messages[-self.max_recent_messages:]) if self.messages else 0
        
        return {
            'conversation_id': self.current_conversation_id,
            'total_messages': len(self.messages),
            'recent_messages': recent_messages,
            'total_summaries': len(self.summaries),
            'total_tokens': total_tokens,
            'compression_ratio': len(self.summaries) / max(1, len(self.messages)) * 100,
            'average_importance': sum(msg.importance_score for msg in self.messages) / max(1, len(self.messages))
        } 