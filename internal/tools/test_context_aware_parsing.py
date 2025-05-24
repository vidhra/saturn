#!/usr/bin/env python3
"""
Test script to demonstrate context-aware parsing capabilities for CLI documentation.

This script shows the difference between standard sentence splitting and 
CLI-specific context-aware parsing.
"""

import os
import sys
from pathlib import Path

# Add saturn directory to path for imports
saturn_dir = Path(__file__).parent.parent.parent / "saturn"
sys.path.insert(0, str(saturn_dir))

from rag_engine import CLIContextAwareParser
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import Document
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax

console = Console()

# Sample CLI documentation text for testing
SAMPLE_CLI_DOC = """
# aws s3 cp

## Synopsis
Copies a local file or S3 object to another location locally or in S3.

```
aws s3 cp <LocalPath> <S3Uri> or <S3Uri> <LocalPath> or <S3Uri> <S3Uri>
```

## Description
The aws s3 cp command copies a file or folder from the source to the destination. 
The following use cases are supported:

- LocalPath to S3
- S3 to LocalPath  
- S3 to S3

## Options

### Global Options
`--dryrun` (boolean)
Displays the operations that would be performed using the specified command without actually running them.

`--quiet` (boolean) 
Does not display the operations performed from the specified command.

`--include` (string)
Don't exclude files or objects in the command that match the specified pattern.

### Transfer Options
`--recursive` (boolean)
Command is performed on all files or objects under the specified directory or prefix.

`--storage-class` (string)
The type of storage to use for the object. Valid values are: STANDARD | REDUCED_REDUNDANCY | STANDARD_IA

## Examples

### Copy a local file to S3
```bash
aws s3 cp test.txt s3://mybucket/test2.txt
```

### Copy a file from S3 to local
```bash
aws s3 cp s3://mybucket/test.txt test2.txt
```

### Copy S3 object to another S3 location
```bash
aws s3 cp s3://mybucket/test.txt s3://mybucket2/test2.txt
```

### Recursive copy with storage class
```bash
aws s3 cp mydir s3://mybucket/mydir --recursive --storage-class REDUCED_REDUNDANCY
```
"""

def test_parsing_comparison():
    """Compare standard vs context-aware parsing."""
    console.print(Panel("CLI Documentation Parsing Comparison", style="bold blue"))
    
    # Create document
    doc = Document(text=SAMPLE_CLI_DOC, metadata={"file_name": "aws_s3_cp.md"})
    
    # Test standard sentence splitter
    console.print("\n[bold yellow]Standard Sentence Splitter Results:[/bold yellow]")
    standard_parser = SentenceSplitter(chunk_size=500, chunk_overlap=50)
    standard_nodes = standard_parser.get_nodes_from_documents([doc])
    
    standard_table = Table(title="Standard Parsing", show_header=True, header_style="bold red")
    standard_table.add_column("Chunk #", style="cyan", width=8)
    standard_table.add_column("Size", style="green", width=8)
    standard_table.add_column("Preview", style="white")
    
    for i, node in enumerate(standard_nodes):
        preview = node.text[:100].replace('\n', ' ') + "..." if len(node.text) > 100 else node.text.replace('\n', ' ')
        standard_table.add_row(str(i+1), str(len(node.text)), preview)
    
    console.print(standard_table)
    
    # Test context-aware parser
    console.print("\n[bold yellow]Context-Aware CLI Parser Results:[/bold yellow]")
    cli_parser = CLIContextAwareParser(
        max_chunk_size=500,
        chunk_overlap=50,
        preserve_code_blocks=True,
        preserve_command_context=True
    )
    cli_nodes = cli_parser.get_nodes_from_documents([doc], show_progress=True)
    
    cli_table = Table(title="Context-Aware Parsing", show_header=True, header_style="bold green")
    cli_table.add_column("Chunk #", style="cyan", width=8)
    cli_table.add_column("Size", style="green", width=8)
    cli_table.add_column("Section", style="yellow", width=15)
    cli_table.add_column("Command", style="magenta", width=15)
    cli_table.add_column("Content Types", style="blue", width=15)
    cli_table.add_column("Preview", style="white")
    
    for i, node in enumerate(cli_nodes):
        metadata = node.metadata
        preview = node.text[:80].replace('\n', ' ') + "..." if len(node.text) > 80 else node.text.replace('\n', ' ')
        
        section_title = metadata.get('section_title', 'N/A')
        command = metadata.get('command', 'N/A')
        content_types = ', '.join(metadata.get('content_types', [])) or 'N/A'
        
        cli_table.add_row(
            str(i+1), 
            str(len(node.text)), 
            section_title[:12] + "..." if len(section_title) > 12 else section_title,
            command[:12] + "..." if len(command) > 12 else command,
            content_types[:12] + "..." if len(content_types) > 12 else content_types,
            preview
        )
    
    console.print(cli_table)
    
    # Show detailed comparison
    console.print(f"\n[bold]Comparison Summary:[/bold]")
    console.print(f"Standard Parser: {len(standard_nodes)} chunks")
    console.print(f"Context-Aware Parser: {len(cli_nodes)} chunks")
    
    # Show a detailed example of one chunk from each
    if cli_nodes and standard_nodes:
        console.print("\n[bold]Example: First Chunk Comparison[/bold]")
        
        console.print(Panel(
            standard_nodes[0].text,
            title="Standard Parser - First Chunk",
            border_style="red"
        ))
        
        console.print(Panel(
            f"**Section:** {cli_nodes[0].metadata.get('section_title', 'N/A')}\n"
            f"**Command:** {cli_nodes[0].metadata.get('command', 'N/A')}\n"
            f"**Content Types:** {', '.join(cli_nodes[0].metadata.get('content_types', []))}\n\n"
            f"{cli_nodes[0].text}",
            title="Context-Aware Parser - First Chunk",
            border_style="green"
        ))

def test_metadata_extraction():
    """Test metadata extraction capabilities."""
    console.print("\n" + "="*80)
    console.print(Panel("Metadata Extraction Test", style="bold blue"))
    
    cli_parser = CLIContextAwareParser()
    doc = Document(text=SAMPLE_CLI_DOC, metadata={"file_name": "aws_s3_cp.md"})
    
    # Extract metadata
    metadata = cli_parser._extract_metadata_from_text(SAMPLE_CLI_DOC, "aws_s3_cp.md")
    
    metadata_table = Table(title="Extracted Metadata", show_header=True, header_style="bold magenta")
    metadata_table.add_column("Key", style="cyan")
    metadata_table.add_column("Value", style="white")
    
    for key, value in metadata.items():
        if isinstance(value, list):
            value = ', '.join(value) if value else 'None'
        metadata_table.add_row(key, str(value))
    
    console.print(metadata_table)

def main():
    """Run all tests."""
    console.print("🧪 Testing Context-Aware RAG Parsing for CLI Documentation\n")
    
    try:
        test_parsing_comparison()
        test_metadata_extraction()
        
        console.print("\n" + "="*80)
        console.print("[bold green]✅ All tests completed successfully![/bold green]")
        console.print("\n[bold]Key Benefits of Context-Aware Parsing:[/bold]")
        console.print("• Preserves command structure and relationships")
        console.print("• Keeps code examples intact")
        console.print("• Extracts meaningful metadata (command, provider, section type)")
        console.print("• Splits by logical sections rather than arbitrary sentence boundaries")
        console.print("• Better RAG retrieval through enhanced metadata")
        
    except Exception as e:
        console.print(f"[bold red]❌ Test failed:[/] {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 