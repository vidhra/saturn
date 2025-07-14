'use client'

import { useMemo, useEffect } from 'react'
import { 
  ReactFlow, 
  Node, 
  Edge, 
  Controls, 
  Background, 
  useNodesState, 
  useEdgesState,
  NodeTypes,
  ConnectionMode,
  BackgroundVariant
} from '@xyflow/react'
import '@xyflow/react/dist/style.css'
import WorkflowNode from './workflow-node'

interface DAGViewerProps {
  workflow?: {
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
      status?: 'pending' | 'running' | 'completed' | 'failed'
    }>
  }
  executionStatus?: Record<string, {
    status: 'pending' | 'running' | 'completed' | 'failed'
    output?: unknown
    error?: string
  }>
}

export function DAGViewer({ workflow, executionStatus = {} }: DAGViewerProps) {
  // Convert workflow steps to React Flow nodes
  const initialNodes: Node[] = useMemo(() => {
    if (!workflow?.steps) {
      return []
    }
    
    return workflow.steps.map((step, index) => {
      const status = executionStatus[step.id]?.status || step.status || 'pending'
      
      const node = {
        id: step.id,
        type: 'workflowNode',
        position: { 
          x: (index % 3) * 320, 
          y: Math.floor(index / 3) * 200 
        },
        data: {
          label: step.id,
          description: step.description,
          cloudProvider: step.cloud_provider,
          toolToUse: step.tool_to_use,
          executedCommand: step.executed_command,
          executionSuccessful: step.execution_successful,
          status,
          output: executionStatus[step.id]?.output,
          error: executionStatus[step.id]?.error
        }
      }
      
      return node
    })
  }, [workflow, executionStatus])

  // Convert dependencies to React Flow edges
  const initialEdges: Edge[] = useMemo(() => {
    if (!workflow?.steps) return []
    
    const edges: Edge[] = []
    
    workflow.steps.forEach(step => {
      step.dependencies.forEach(depId => {
        edges.push({
          id: `${depId}-${step.id}`,
          source: depId,
          target: step.id,
          type: 'smoothstep',
          animated: executionStatus[depId]?.status === 'running',
          style: {
            stroke: executionStatus[depId]?.status === 'completed' ? '#10b981' : 
                   executionStatus[depId]?.status === 'failed' ? '#ef4444' :
                   executionStatus[depId]?.status === 'running' ? '#3b82f6' : '#6b7280'
          }
        })
      })
    })
    
    return edges
  }, [workflow, executionStatus])

  const [nodes, setNodes, onNodesChange] = useNodesState<Node>(initialNodes)
  const [edges, setEdges, onEdgesChange] = useEdgesState<Edge>(initialEdges)

  const nodeTypes: NodeTypes = useMemo(() => ({
    workflowNode: WorkflowNode
  }), [])

  // Update nodes when workflow changes
  useEffect(() => {
    setNodes(initialNodes)
  }, [initialNodes, setNodes])

  // Update edges when workflow changes  
  useEffect(() => {
    setEdges(initialEdges)
  }, [initialEdges, setEdges])

  // Update nodes when execution status changes
  useMemo(() => {
    setNodes(currentNodes => 
      currentNodes.map(node => ({
        ...node,
        data: {
          ...node.data,
          status: executionStatus[node.id]?.status || node.data.status,
          output: executionStatus[node.id]?.output,
          error: executionStatus[node.id]?.error
        }
      }))
    )
  }, [executionStatus, setNodes])

  // Update edges when execution status changes
  useMemo(() => {
    setEdges(currentEdges =>
      currentEdges.map(edge => ({
        ...edge,
        animated: executionStatus[edge.source]?.status === 'running',
        style: {
          stroke: executionStatus[edge.source]?.status === 'completed' ? '#10b981' : 
                 executionStatus[edge.source]?.status === 'failed' ? '#ef4444' :
                 executionStatus[edge.source]?.status === 'running' ? '#3b82f6' : '#9ca3af',
          strokeWidth: 2
        }
      }))
    )
  }, [executionStatus, setEdges])

  if (!workflow) {
    return (
      <div className="flex-1 flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="w-16 h-16 bg-gray-200 rounded-lg flex items-center justify-center mx-auto mb-4">
            <span className="text-2xl text-gray-400">📊</span>
          </div>
          <h3 className="text-lg font-semibold text-gray-900 mb-2">No Workflow Selected</h3>
          <p className="text-gray-600 max-w-md">
            Upload a .sat workflow file from the sidebar to visualize and execute your DAG workflows.
          </p>
        </div>
      </div>
    )
  }

  return (
    <div className="flex-1 bg-gray-900 h-full">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        nodeTypes={nodeTypes}
        connectionMode={ConnectionMode.Strict}
        fitView
        fitViewOptions={{
          padding: 0.3,
          includeHiddenNodes: false,
          minZoom: 0.5,
          maxZoom: 1.5,
        }}
        className="bg-gray-900 w-full h-full"
        defaultEdgeOptions={{
          style: { 
            stroke: '#9ca3af', 
            strokeWidth: 2 
          },
          animated: false,
        }}
        proOptions={{ hideAttribution: true }}
      >
        <Background 
          color="#4b5563" 
          gap={20} 
          variant={BackgroundVariant.Dots}
          size={1}
        />
        <Controls />
      </ReactFlow>
    </div>
  )
} 