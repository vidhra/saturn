# Saturn Workflows (.sat files)

Saturn workflows allow you to save and reuse execution plans as `.sat` files. This enables reproducible infrastructure automation and sharing of complex workflows.

## Overview

When you run a natural language query with Saturn, the system:
1. **Plans** the execution by breaking down your query into steps
2. **Generates a DAG** with dependencies between steps
3. **Automatically saves** the workflow as a `.sat` file (if enabled)
4. **Executes** the planned steps

You can then rerun the exact same workflow using the saved `.sat` file, bypassing the planning phase.

## Workflow File Format

`.sat` files are JSON-based and contain:

- **Workflow metadata**: Version, creation time, original query
- **DAG structure**: Nodes, edges, and execution order
- **Step details**: Tool information, cloud providers, dependencies

Example structure:
```json
{
  "saturn_workflow": {
    "version": "1.0",
    "created_at": "2024-01-15T10:30:00.000000",
    "original_query": "Create a GCS bucket and deploy a Cloud Function",
    "description": "Saturn workflow generated from: Create a GCS bucket..."
  },
  "dag": {
    "nodes": ["create_bucket", "create_function", "configure_trigger"],
    "edges": [{"source": "create_bucket", "target": "create_function"}],
    "execution_order": ["create_bucket", "create_function", "configure_trigger"]
  },
  "steps": {
    "create_bucket": {
      "id": "create_bucket",
      "description": "Create a GCS bucket for file processing",
      "tool_to_use": "cli_command_generation",
      "cloud_provider": "gcp",
      "dependencies": [],
      "pass_output_to_next": true
    }
  }
}
```

## Usage

### Running Natural Language Queries
```bash
# Saturn automatically saves workflows after planning
saturn run "Create a GCS bucket and configure IAM permissions"
# Output: Workflow saved to: workflows/Create_a_GCS_bucket_20240115_103000.sat
```

### Running Saved Workflows
```bash
# Execute a saved workflow
saturn run workflows/Create_a_GCS_bucket_20240115_103000.sat

# Or use a relative path
saturn run example_workflow.sat
```

### Managing Workflows

#### List Available Workflows
```bash
# List all .sat files in current directory
saturn workflow list

# List workflows in specific directory
saturn workflow list --dir ./my-workflows

# Show detailed information
saturn workflow list --verbose
```

#### Validate Workflows
```bash
# Check if a workflow file is valid
saturn workflow validate --path example_workflow.sat
```

#### View Workflow Information
```bash
# Show detailed workflow information
saturn workflow info --path example_workflow.sat

# Show with dependency details
saturn workflow info --path example_workflow.sat --verbose
```

## Benefits

### 1. **Reproducibility**
- Exact same execution every time
- No variation in planning between runs
- Consistent results across environments

### 2. **Speed**
- Skip planning phase on subsequent runs
- Faster execution for complex workflows
- Reduced LLM API calls

### 3. **Sharing & Collaboration**
- Share workflows as files
- Version control friendly (JSON format)
- Template creation for common patterns

### 4. **Debugging & Testing**
- Inspect planned steps before execution
- Modify workflows manually if needed
- Test different execution strategies

## Configuration

Control workflow saving behavior in your config:

```yaml
# config.yaml
save_workflow: true           # Enable/disable automatic saving (default: true)
workflows_dir: "workflows"    # Directory for saved workflows (default: "workflows")
```

Or via CLI options:
```bash
# Disable workflow saving for this run
saturn run "my query" --config save_workflow=false

# Use custom workflows directory
saturn run "my query" --config workflows_dir="/my/custom/path"
```

## Advanced Usage

### Manual Workflow Creation
You can create `.sat` files manually by following the JSON schema. This is useful for:
- Creating templates for common tasks
- Building complex workflows incrementally
- Integrating with external tools

### Workflow Modification
Since `.sat` files are JSON, you can modify them:
- Change step descriptions
- Adjust tool arguments
- Modify dependencies
- Add or remove steps

Always validate modified workflows:
```bash
saturn workflow validate --path modified_workflow.sat
```

### Integration with CI/CD
Use workflows in automated pipelines:
```bash
# In your CI/CD script
saturn run production_deployment.sat --execution-mode yolo
```

## Best Practices

1. **Meaningful Names**: Use descriptive filenames for workflows
2. **Version Control**: Keep workflows in source control
3. **Validation**: Always validate modified workflows
4. **Documentation**: Add comments in the original query field
5. **Organization**: Use subdirectories for different types of workflows

## Troubleshooting

### Common Issues

**File Not Found**
```bash
saturn run my_workflow.sat
# Error: Saturn workflow file not found: my_workflow.sat
```
- Check the file path
- Ensure the file has `.sat` extension
- Use `saturn workflow list` to see available workflows

**Invalid Format**
```bash
saturn workflow validate --path broken_workflow.sat
# Error: Invalid JSON in .sat file
```
- Check JSON syntax
- Validate against the schema
- Compare with working examples

**Missing Dependencies**
```bash
# Error: Dependency 'step_x' for step 'step_y' not found
```
- Check step IDs match exactly
- Ensure all referenced steps exist
- Use `saturn workflow info` to inspect dependencies

### Getting Help

- Use `saturn workflow --help` for command help
- Check `examples/example_workflow.sat` for format reference
- Validate workflows with `saturn workflow validate`
- View detailed info with `saturn workflow info --verbose`

## Examples

See the `examples/` directory for sample `.sat` files demonstrating:
- Simple GCS bucket creation
- Multi-step Cloud Function deployment
- Complex infrastructure workflows
- File build tool integration
- MCP tool usage

Start with these examples and modify them for your use cases. 