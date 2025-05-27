# LLM Integration Guide

This guide explains how to use different LLM providers with Saturn orchestrator. Saturn now supports OpenAI, Claude (Anthropic), Google Gemini, and Mistral AI.

## Overview

Saturn uses a unified interface for all LLM providers, allowing you to switch between them easily by changing configuration. All providers support:

- **Text Generation** (`agenerate` method): Basic chat completion
- **Tool Calls** (`get_tool_calls` method): Function calling for orchestration

## Supported Providers

### 1. OpenAI (GPT-4, GPT-3.5, etc.)

**Setup:**
```bash
pip install openai>=1.3.0
export OPENAI_API_KEY="your-openai-api-key"
```

**Configuration:**
```python
config = {
    'llm_provider': 'openai',
    'openai_api_key': 'your-openai-api-key',
    'openai_model': 'gpt-4o'  # Optional, defaults to 'gpt-4.1'
}
```

**Features:**
- Full tool calling support
- JSON mode support
- Function calling with proper error handling

### 2. Claude (Anthropic)

**Setup:**
```bash
pip install anthropic>=0.50.0
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

**Configuration:**
```python
config = {
    'llm_provider': 'claude',
    'anthropic_api_key': 'your-anthropic-api-key',
    'claude_model': 'claude-3-5-sonnet-20241022'  # Optional, defaults to latest sonnet
}
```

**Features:**
- Full tool calling support
- Excellent reasoning capabilities
- System prompt handling

### 3. Google Gemini

**Setup:**
```bash
pip install google-generativeai>=0.8.0
export GEMINI_API_KEY="your-gemini-api-key"
```

**Configuration:**
```python
config = {
    'llm_provider': 'gemini',
    'gemini_api_key': 'your-gemini-api-key',
    'gemini_model': 'gemini-1.5-pro-latest',  # Optional
    'gemini_system_prompt': 'Custom system prompt'  # Optional
}
```

**Features:**
- Tool calling support with function declarations
- Large context window
- Multi-modal capabilities (future)

### 4. Mistral AI

**Setup:**
```bash
pip install mistralai>=1.7.0
export MISTRAL_API_KEY="your-mistral-api-key"
```

**Configuration:**
```python
config = {
    'llm_provider': 'mistral',
    'mistral_api_key': 'your-mistral-api-key',
    'mistral_model': 'mistral-large-latest'  # Optional
}
```

**Features:**
- Tool calling support
- High performance
- Cost effective

## Usage Examples

### Basic Text Generation

```python
from model.llm.openai_llm import OpenAILLM

# Initialize LLM
config = {'openai_api_key': 'your-key'}
llm = OpenAILLM(config)

# Generate text
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain cloud computing in one sentence."}
]

response = await llm.agenerate(messages)
print(response.choices[0].message.content)
```

### Tool Calling

```python
# Define tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "create_vm",
            "description": "Create a virtual machine",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "zone": {"type": "string"}
                },
                "required": ["name", "zone"]
            }
        }
    }
]

# Get tool calls
tool_calls, text_response = await llm.get_tool_calls(
    query="Create a VM named 'test-vm' in zone 'us-central1-a'",
    system_prompt="You are a cloud automation assistant.",
    tools=tools
)

if tool_calls:
    for call in tool_calls:
        print(f"Tool: {call['name']}, Args: {call['arguments']}")
```

### Using with Saturn Orchestrator

```python
from saturn.orchestrator import run_query_with_feedback

config = {
    'llm_provider': 'claude',  # or 'openai', 'gemini', 'mistral'
    'anthropic_api_key': 'your-claude-key',
    'gcp_project_id': 'your-project',
    # ... other config
}

await run_query_with_feedback(
    query="Create a VPC network and a compute instance",
    config=config,
    rag_engine=rag_engine,
    verbose=True
)
```

## Environment Variables

Set these environment variables based on which providers you want to use:

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Claude (Anthropic)
export ANTHROPIC_API_KEY="sk-ant-..."

# Gemini (Google AI)
export GEMINI_API_KEY="AI..."

# Mistral
export MISTRAL_API_KEY="..."

# For Saturn orchestrator
export LLM_PROVIDER="openai"  # or claude, gemini, mistral
```

## Testing Your Setup

Use the provided test script to verify all integrations:

```bash
python test_llm_integrations.py
```

This will test:
- ✅ Initialization of each provider
- ✅ Basic text generation (`agenerate`)
- ✅ Tool calling functionality (`get_tool_calls`)

## Provider Comparison

| Feature | OpenAI | Claude | Gemini | Mistral |
|---------|--------|--------|--------|---------|
| Tool Calling | ✅ Excellent | ✅ Excellent | ✅ Good | ✅ Good |
| Reasoning | ✅ Very Good | ✅ Excellent | ✅ Good | ✅ Good |
| Speed | ✅ Fast | ⚡ Fast | ⚡ Very Fast | ⚡ Very Fast |
| Cost | 💰 Medium | 💰 Medium | 💰 Low | 💰 Low |
| Context Window | 📄 128k | 📄 200k | 📄 2M | 📄 128k |

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Install missing dependencies
   pip install -r requirements.txt
   ```

2. **API Key Issues**
   ```bash
   # Verify your API key is set
   echo $OPENAI_API_KEY
   ```

3. **Tool Calling Not Working**
   - Verify the tool schema format
   - Check system prompts are clear
   - Ensure the LLM supports function calling

4. **Async Issues**
   ```python
   # All methods are async, use await
   response = await llm.agenerate(messages)
   ```

### Provider-Specific Notes

- **OpenAI**: Most stable, best documentation
- **Claude**: Excellent for complex reasoning, handles errors well
- **Gemini**: Very large context window, good for document processing
- **Mistral**: Cost-effective, good performance

## API Rate Limits

Be aware of rate limits:
- **OpenAI**: Varies by tier (10-100 requests/minute)
- **Claude**: 50 requests/minute (free), higher for paid
- **Gemini**: 60 requests/minute (free)
- **Mistral**: Varies by subscription

## Best Practices

1. **Error Handling**: Always wrap LLM calls in try-catch blocks
2. **Rate Limiting**: Implement backoff for production use
3. **Cost Management**: Monitor usage and set limits
4. **Model Selection**: Choose appropriate models for your use case
5. **Tool Design**: Keep tool schemas simple and clear

## Getting Help

- Check the test script output for specific errors
- Review provider documentation for API specifics
- Ensure all dependencies are installed correctly
- Verify API keys have the correct permissions 