'use client'

import { useState, useCallback } from 'react'
import { Sidebar } from '@/components/sidebar'
import { TopBar } from '@/components/top-bar'
import { DAGViewer } from '@/components/dag-viewer'
import { parseSatFile, validateWorkflow, type SatWorkflow } from '@/lib/workflow-parser'

interface WorkflowItem {
  id: string
  name: string
  status: 'idle' | 'running' | 'completed' | 'failed'
  data: SatWorkflow
}

interface ExecutionStatus {
  [stepId: string]: {
    status: 'pending' | 'running' | 'completed' | 'failed'
    output?: unknown
    error?: string
  }
}

export default function Home() {
  const [workflows, setWorkflows] = useState<WorkflowItem[]>([])
  const [selectedWorkflowId, setSelectedWorkflowId] = useState<string>()
  const [executionStatus, setExecutionStatus] = useState<ExecutionStatus>({})
  const [isExecuting, setIsExecuting] = useState(false)

  const selectedWorkflow = workflows.find(w => w.id === selectedWorkflowId)

  const handleFileUpload = useCallback((file: File) => {
    const reader = new FileReader()
    reader.onload = (e) => {
      try {
        const content = e.target?.result as string
        const workflowData = parseSatFile(content)
        
        // Validate the workflow
        const errors = validateWorkflow(workflowData)
        if (errors.length > 0) {
          alert(`Workflow validation failed:\n${errors.join('\n')}`)
          return
        }

        const newWorkflow: WorkflowItem = {
          id: workflowData.id,
          name: workflowData.name,
          status: 'idle',
          data: workflowData
        }

        setWorkflows(prev => {
          // Replace if already exists, otherwise add
          const existing = prev.findIndex(w => w.id === workflowData.id)
          if (existing >= 0) {
            const updated = [...prev]
            updated[existing] = newWorkflow
            return updated
          } else {
            return [...prev, newWorkflow]
          }
        })

        // Select the newly loaded workflow
        setSelectedWorkflowId(workflowData.id)
      } catch (error) {
        alert(`Failed to load workflow: ${error instanceof Error ? error.message : 'Unknown error'}`)
      }
    }
    reader.readAsText(file)
  }, [])

  const simulateExecution = useCallback(async () => {
    if (!selectedWorkflow || isExecuting) return

    setIsExecuting(true)
    setWorkflows(prev => prev.map(w => 
      w.id === selectedWorkflowId ? { ...w, status: 'running' } : w
    ))

    // Reset execution status
    const initialStatus: ExecutionStatus = {}
    selectedWorkflow.data.steps.forEach(step => {
      initialStatus[step.id] = { status: 'pending' }
    })
    setExecutionStatus(initialStatus)

    try {
      // Get execution order based on dependencies
      const executionOrder = getExecutionOrder(selectedWorkflow.data.steps)
      
      for (const stepId of executionOrder) {
        const step = selectedWorkflow.data.steps.find(s => s.id === stepId)
        if (!step) continue

        // Mark step as running
        setExecutionStatus(prev => ({
          ...prev,
          [stepId]: { status: 'running' }
        }))

        // Simulate execution time (1-3 seconds)
        await new Promise(resolve => setTimeout(resolve, 1000 + Math.random() * 2000))

        // Simulate success/failure (90% success rate)
        const success = Math.random() > 0.1

        if (success) {
          setExecutionStatus(prev => ({
            ...prev,
            [stepId]: { 
              status: 'completed',
              output: step.executed_command || `Executed ${step.tool_to_use} successfully`
            }
          }))
        } else {
          // Simulate failure
          setExecutionStatus(prev => ({
            ...prev,
            [stepId]: { 
              status: 'failed',
              error: `Failed to execute ${step.tool_to_use}: Simulated error`
            }
          }))
          
          // Stop execution on failure
          setWorkflows(prev => prev.map(w => 
            w.id === selectedWorkflowId ? { ...w, status: 'failed' } : w
          ))
          setIsExecuting(false)
          return
        }
      }

      // Mark workflow as completed
      setWorkflows(prev => prev.map(w => 
        w.id === selectedWorkflowId ? { ...w, status: 'completed' } : w
      ))
    } catch {
      setWorkflows(prev => prev.map(w => 
        w.id === selectedWorkflowId ? { ...w, status: 'failed' } : w
      ))
    }

    setIsExecuting(false)
  }, [selectedWorkflow, selectedWorkflowId, isExecuting])

  const handleStop = useCallback(() => {
    setIsExecuting(false)
    setWorkflows(prev => prev.map(w => 
      w.id === selectedWorkflowId ? { ...w, status: 'idle' } : w
    ))
  }, [selectedWorkflowId])

  const handleSave = useCallback(() => {
    if (!selectedWorkflow) return
    
    const dataStr = JSON.stringify(selectedWorkflow.data, null, 2)
    const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr)
    
    const exportFileDefaultName = `${selectedWorkflow.name.replace(/[^a-zA-Z0-9]/g, '_')}.sat`
    
    const linkElement = document.createElement('a')
    linkElement.setAttribute('href', dataUri)
    linkElement.setAttribute('download', exportFileDefaultName)
    linkElement.click()
  }, [selectedWorkflow])

  return (
    <div className="h-screen flex flex-col bg-gray-100">
      <TopBar
        workflowName={selectedWorkflow?.name}
        workflowStatus={selectedWorkflow?.status || 'idle'}
        onExecute={simulateExecution}
        onStop={handleStop}
        onSave={handleSave}
        isExecuting={isExecuting}
      />
      
      <div className="flex flex-1 overflow-hidden">
        <Sidebar
          onFileUpload={handleFileUpload}
          workflows={workflows}
          selectedWorkflow={selectedWorkflowId}
          onSelectWorkflow={setSelectedWorkflowId}
        />
        
        <DAGViewer
          workflow={selectedWorkflow?.data}
          executionStatus={executionStatus}
        />
      </div>
    </div>
  )
}

// Utility function to get execution order based on dependencies
function getExecutionOrder(steps: SatWorkflow['steps']): string[] {
  const order: string[] = []
  const visited = new Set<string>()
  const visiting = new Set<string>()

  function visit(stepId: string) {
    if (visiting.has(stepId)) {
      throw new Error(`Circular dependency detected involving step: ${stepId}`)
    }
    
    if (visited.has(stepId)) {
      return
    }

    visiting.add(stepId)
    
    const step = steps.find(s => s.id === stepId)
    if (step) {
      // Visit all dependencies first
      for (const depId of step.dependencies) {
        visit(depId)
      }
    }
    
    visiting.delete(stepId)
    visited.add(stepId)
    order.push(stepId)
  }

  // Visit all steps
  for (const step of steps) {
    if (!visited.has(step.id)) {
      visit(step.id)
    }
  }

  return order
}
