# Dependency Installation Guide

This guide helps resolve dependency conflicts when installing Saturn with different LLM and RAG configurations.

## The google-generativeai Version Conflict

There's a version conflict between:
- **LLM Integration**: Requires `google-generativeai>=0.8.0` for latest Gemini features
- **RAG Embeddings**: `llama-index-embeddings-google` requires `google-generativeai<0.6.0`

## Installation Options

### Option 1: Standard Installation (Recommended)
For most users who want all LLM providers working:

```bash
pip install -e .
```

This installs:
- ✅ OpenAI, Claude, Mistral LLMs (fully functional)
- ✅ Gemini LLM with `google-generativeai 0.5.x` (functional but not latest features)
- ✅ RAG with HuggingFace embeddings
- ❌ RAG with Google embeddings (conflict)

### Option 2: Latest Gemini Features
If you need the latest Gemini features and don't need Google embeddings for RAG:

```bash
pip install -e .[full-gemini]
```

This gives you:
- ✅ All LLM providers with latest features
- ✅ RAG with HuggingFace embeddings
- ❌ RAG with Google embeddings (conflict)

### Option 3: Google Embeddings for RAG
If you specifically need Google embeddings for RAG:

```bash
pip install -e .[rag-gemini]
```

This provides:
- ✅ OpenAI, Claude, Mistral LLMs
- ✅ Gemini LLM (basic functionality)
- ✅ RAG with Google embeddings
- ⚠️ Gemini with limited features

## Recommended Approach

**For most users**: Use Option 1 (standard installation) because:

1. **All LLM providers work** - You can use OpenAI, Claude, Gemini, and Mistral
2. **RAG still works** - Use HuggingFace embeddings instead of Google embeddings
3. **No conflicts** - Clean installation without dependency issues

## Alternative RAG Embedding Models

If you can't use Google embeddings, these alternatives work great:

```python
# Instead of Google embeddings, use:
config = {
    'rag_embedding_model': 'sentence-transformers/all-MiniLM-L6-v2',  # Fast and good
    # or
    'rag_embedding_model': 'BAAI/bge-small-en-v1.5',  # High quality
}
```

## Troubleshooting

### Error: "google-generativeai 0.8.5 which is incompatible"

**Solution**: Uninstall and reinstall with proper constraints:

```bash
pip uninstall google-generativeai llama-index-embeddings-google -y
pip install -e .
```

### Want to test specific combinations?

1. **Test standard installation**:
   ```bash
   pip install -e .
   python -c "from model.llm.gemini_llm import GeminiLLM; print('✅ Gemini works')"
   ```

2. **Test with latest Gemini**:
   ```bash
   pip install -e .[full-gemini]
   ```

### Using with Saturn Orchestrator

All installation options work with the orchestrator:

```python
# Configuration works the same regardless of installation option
config = {
    'llm_provider': 'gemini',  # or openai, claude, mistral
    'gemini_api_key': 'your-key',
    'rag_embedding_model': 'sentence-transformers/all-MiniLM-L6-v2',
    # ... other config
}
```

## Summary

- **Default installation** works for 99% of use cases
- **Use HuggingFace embeddings** instead of Google embeddings for RAG
- **All LLM providers work** with the standard installation
- **No need to worry** about the Google embedding conflict unless you specifically need it

The dependency conflict only affects RAG embeddings, not the core LLM functionality! 