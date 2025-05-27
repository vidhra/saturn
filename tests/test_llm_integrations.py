#!/usr/bin/env python3
"""
Test script to verify all LLM integrations are working properly.
Run this script to test OpenAI, Claude, Gemini, and Mistral integrations.
"""

import os
import asyncio
from typing import Dict, Any

from model.llm.openai_llm import OpenAILLM
from model.llm.claude_llm import ClaudeLLM
from model.llm.gemini_llm import GeminiLLM
from model.llm.mistral_llm import MistralLLM
from model.llm.base_interface import BaseLLMInterface


async def test_llm_agenerate(llm_interface: BaseLLMInterface, provider_name: str) -> bool:
    """Test the agenerate method of an LLM interface."""
    try:
        print(f"\n=== Testing {provider_name} agenerate ===")
        
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello and tell me what LLM you are in one sentence."}
        ]
        
        response = await llm_interface.agenerate(messages)
        
        # Extract content based on the response format
        if hasattr(response, 'choices') and response.choices:
            content = response.choices[0].message.content
            print(f"✅ {provider_name} agenerate success: {content[:100]}...")
            return True
        else:
            print(f"❌ {provider_name} agenerate failed: Unexpected response format")
            return False
            
    except Exception as e:
        print(f"❌ {provider_name} agenerate failed: {str(e)}")
        return False


async def test_llm_tool_calls(llm_interface: BaseLLMInterface, provider_name: str) -> bool:
    """Test the get_tool_calls method of an LLM interface."""
    try:
        print(f"\n=== Testing {provider_name} get_tool_calls ===")
        
        # Define a simple tool for testing
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the current weather for a location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA"
                            },
                            "unit": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "Temperature unit"
                            }
                        },
                        "required": ["location"]
                    }
                }
            }
        ]
        
        query = "What's the weather like in San Francisco?"
        system_prompt = "You are a weather assistant. Use the get_weather function to answer weather questions."
        
        tool_calls, text_response = await llm_interface.get_tool_calls(
            query=query,
            system_prompt=system_prompt,
            tools=tools
        )
        
        if tool_calls:
            print(f"✅ {provider_name} tool calls success: {len(tool_calls)} tool(s) called")
            for i, call in enumerate(tool_calls):
                print(f"   Tool {i+1}: {call.get('name')} with args: {call.get('arguments')}")
            return True
        elif text_response:
            print(f"✅ {provider_name} returned text response: {text_response[:100]}...")
            return True
        else:
            print(f"❌ {provider_name} tool calls failed: No tools called and no text response")
            return False
            
    except Exception as e:
        print(f"❌ {provider_name} tool calls failed: {str(e)}")
        return False


async def test_provider(provider_config: Dict[str, Any], provider_name: str, llm_class) -> Dict[str, bool]:
    """Test a specific LLM provider."""
    print(f"\n{'='*50}")
    print(f"Testing {provider_name}")
    print(f"{'='*50}")
    
    results = {"init": False, "agenerate": False, "tool_calls": False}
    
    try:
        # Test initialization
        llm_interface = llm_class(provider_config)
        results["init"] = True
        print(f"✅ {provider_name} initialization successful")
        
        # Test agenerate
        results["agenerate"] = await test_llm_agenerate(llm_interface, provider_name)
        
        # Test tool calls
        results["tool_calls"] = await test_llm_tool_calls(llm_interface, provider_name)
        
    except Exception as e:
        print(f"❌ {provider_name} initialization failed: {str(e)}")
    
    return results


async def main():
    """Main test function."""
    print("🧪 LLM Integration Test Suite")
    print("=" * 60)
    
    # Test configurations
    test_configs = {
        "OpenAI": {
            "config": {"openai_api_key": os.getenv('OPENAI_API_KEY')},
            "class": OpenAILLM,
            "required_env": "OPENAI_API_KEY"
        },
        "Claude": {
            "config": {"anthropic_api_key": os.getenv('ANTHROPIC_API_KEY')},
            "class": ClaudeLLM,
            "required_env": "ANTHROPIC_API_KEY"
        },
        "Gemini": {
            "config": {"gemini_api_key": os.getenv('GEMINI_API_KEY')},
            "class": GeminiLLM,
            "required_env": "GEMINI_API_KEY"
        },
        "Mistral": {
            "config": {"mistral_api_key": os.getenv('MISTRAL_API_KEY')},
            "class": MistralLLM,
            "required_env": "MISTRAL_API_KEY"
        }
    }
    
    all_results = {}
    
    for provider_name, test_config in test_configs.items():
        # Check if API key is available
        if not os.getenv(test_config["required_env"]):
            print(f"\n⚠️  Skipping {provider_name}: {test_config['required_env']} not found in environment")
            all_results[provider_name] = {"init": False, "agenerate": False, "tool_calls": False, "skipped": True}
            continue
        
        results = await test_provider(
            provider_config=test_config["config"],
            provider_name=provider_name,
            llm_class=test_config["class"]
        )
        all_results[provider_name] = results
    
    # Summary
    print(f"\n{'='*60}")
    print("📊 Test Summary")
    print(f"{'='*60}")
    
    for provider_name, results in all_results.items():
        if results.get("skipped"):
            print(f"{provider_name:10} - SKIPPED (API key not found)")
        else:
            init_status = "✅" if results["init"] else "❌"
            agen_status = "✅" if results["agenerate"] else "❌"
            tool_status = "✅" if results["tool_calls"] else "❌"
            print(f"{provider_name:10} - Init: {init_status} | AGenerate: {agen_status} | Tools: {tool_status}")
    
    print(f"\n{'='*60}")
    print("💡 Tips:")
    print("- Set environment variables for API keys to test all providers")
    print("- OPENAI_API_KEY for OpenAI")
    print("- ANTHROPIC_API_KEY for Claude")
    print("- GEMINI_API_KEY for Gemini")
    print("- MISTRAL_API_KEY for Mistral")
    print(f"{'='*60}")


if __name__ == "__main__":
    asyncio.run(main()) 