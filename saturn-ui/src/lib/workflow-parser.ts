export interface SatWorkflow {
  id: string
  name: string
  steps: Array<{
    id: string
    description: string
    cloud_provider: string | null
    tool_to_use: string
    dependencies: string[]
    executed_command?: string
    execution_successful?: boolean
    tool_args?: Record<string, unknown>
    mcp_tool_name?: string
    mcp_tool_args?: Record<string, unknown>
    file_tool_name?: string
    file_tool_args?: Record<string, unknown>
  }>
  metadata?: {
    created_at?: string
    version?: string
    description?: string
  }
}

export function parseSatFile(content: string): SatWorkflow {
  try {
    const data = JSON.parse(content)
    
    // Handle different .sat file formats
    
    // Format 1: Standard Saturn .sat format with step_details_map
    if (data.step_details_map && data.dag) {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const steps = Object.entries(data.step_details_map).map(([id, details]: [string, any]) => ({
        id,
        description: details.description || 'No description',
        cloud_provider: details.cloud_provider || null,
        tool_to_use: details.tool_to_use || 'unknown',
        dependencies: details.dependencies || [],
        executed_command: details.executed_command,
        execution_successful: details.execution_successful,
        tool_args: details.tool_args,
        mcp_tool_name: details.mcp_tool_name,
        mcp_tool_args: details.mcp_tool_args,
        file_tool_name: details.file_tool_name,
        file_tool_args: details.file_tool_args
      }))
      
      return {
        id: data.workflow_id || generateWorkflowId(),
        name: data.workflow_name || 'Unnamed Workflow',
        steps,
        metadata: {
          created_at: data.created_at,
          version: data.version,
          description: data.description
        }
      }
    }
    
    // Format 2: New Saturn format with steps object and saturn_workflow metadata
    if (data.steps && typeof data.steps === 'object' && !Array.isArray(data.steps) && data.dag) {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const steps = Object.entries(data.steps).map(([id, details]: [string, any]) => ({
        id,
        description: details.description || 'No description',
        cloud_provider: details.cloud_provider || null,
        tool_to_use: details.tool_to_use || 'unknown',
        dependencies: details.dependencies || [],
        executed_command: details.executed_command,
        execution_successful: details.execution_successful,
        tool_args: details.tool_args,
        mcp_tool_name: details.mcp_tool_name,
        mcp_tool_args: details.mcp_tool_args,
        file_tool_name: details.file_tool_name,
        file_tool_args: details.file_tool_args
      }))
      
      const saturnWorkflow = data.saturn_workflow || {}
      return {
        id: generateWorkflowId(),
        name: saturnWorkflow.original_query || 'Saturn Generated Workflow',
        steps,
        metadata: {
          created_at: saturnWorkflow.created_at,
          version: saturnWorkflow.version,
          description: saturnWorkflow.description
        }
      }
    }
    
    // Format 3: Direct workflow format with steps array
    if (data.steps && Array.isArray(data.steps)) {
      return {
        id: data.id || generateWorkflowId(),
        name: data.name || 'Imported Workflow',
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        steps: data.steps.map((step: any) => ({
          id: step.id,
          description: step.description || 'No description',
          cloud_provider: step.cloud_provider || null,
          tool_to_use: step.tool_to_use || 'unknown',
          dependencies: step.dependencies || [],
          executed_command: step.executed_command,
          execution_successful: step.execution_successful,
          tool_args: step.tool_args,
          mcp_tool_name: step.mcp_tool_name,
          mcp_tool_args: step.mcp_tool_args,
          file_tool_name: step.file_tool_name,
          file_tool_args: step.file_tool_args
        })),
        metadata: data.metadata
      }
    }
    
    // Format 4: Direct array format
    if (Array.isArray(data)) {
      return {
        id: generateWorkflowId(),
        name: 'Imported Workflow',
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        steps: data.map((step: any) => ({
          id: step.id,
          description: step.description || 'No description',
          cloud_provider: step.cloud_provider || null,
          tool_to_use: step.tool_to_use || 'unknown',
          dependencies: step.dependencies || [],
          executed_command: step.executed_command,
          execution_successful: step.execution_successful,
          tool_args: step.tool_args,
          mcp_tool_name: step.mcp_tool_name,
          mcp_tool_args: step.mcp_tool_args,
          file_tool_name: step.file_tool_name,
          file_tool_args: step.file_tool_args
        })),
        metadata: {}
      }
    }
    
    throw new Error('Unrecognized .sat file format')
  } catch (error) {
    throw new Error(`Failed to parse .sat file: ${error instanceof Error ? error.message : 'Unknown error'}`)
  }
}

export function generateWorkflowId(): string {
  return `workflow_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
}

export function validateWorkflow(workflow: SatWorkflow): string[] {
  const errors: string[] = []
  
  if (!workflow.id) {
    errors.push('Workflow must have an ID')
  }
  
  if (!workflow.name) {
    errors.push('Workflow must have a name')
  }
  
  if (!workflow.steps || workflow.steps.length === 0) {
    errors.push('Workflow must have at least one step')
  }
  
  // Check for circular dependencies
  const visited = new Set<string>()
  const recursionStack = new Set<string>()
  
  function hasCycle(stepId: string): boolean {
    if (recursionStack.has(stepId)) {
      return true
    }
    
    if (visited.has(stepId)) {
      return false
    }
    
    visited.add(stepId)
    recursionStack.add(stepId)
    
    const step = workflow.steps.find(s => s.id === stepId)
    if (step) {
      for (const depId of step.dependencies) {
        if (hasCycle(depId)) {
          return true
        }
      }
    }
    
    recursionStack.delete(stepId)
    return false
  }
  
  for (const step of workflow.steps) {
    if (hasCycle(step.id)) {
      errors.push('Workflow contains circular dependencies')
      break
    }
  }
  
  // Check for missing dependencies
  const stepIds = new Set(workflow.steps.map(s => s.id))
  for (const step of workflow.steps) {
    for (const depId of step.dependencies) {
      if (!stepIds.has(depId)) {
        errors.push(`Step "${step.id}" depends on missing step "${depId}"`)
      }
    }
  }
  
  return errors
} 