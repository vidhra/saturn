import { memo } from 'react'
import { Handle, Position, NodeProps } from '@xyflow/react'
import { cn } from '@/lib/utils'
import { 
  Cloud, 
  Database, 
  FileText, 
  Terminal, 
  CheckCircle, 
  XCircle, 
  Clock, 
  Play,
  Zap
} from 'lucide-react'

interface WorkflowNodeData {
  label: string
  description: string
  cloudProvider: string | null
  toolToUse: string
  executedCommand?: string
  executionSuccessful?: boolean
  status: 'pending' | 'running' | 'completed' | 'failed'
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  output?: any
  error?: string
}

function getNodeIcon(cloudProvider: string | null, toolToUse: string) {
  if (cloudProvider === 'aws' || cloudProvider === 'gcp') {
    return <Cloud className="w-4 h-4" />
  }
  
  if (toolToUse.includes('file') || toolToUse.includes('read') || toolToUse.includes('write')) {
    return <FileText className="w-4 h-4" />
  }
  
  if (toolToUse.includes('mcp')) {
    return <Zap className="w-4 h-4" />
  }
  
  if (toolToUse.includes('database') || toolToUse.includes('sql')) {
    return <Database className="w-4 h-4" />
  }
  
  return <Terminal className="w-4 h-4" />
}

function getStatusIcon(status: string) {
  switch (status) {
    case 'completed':
      return <CheckCircle className="w-4 h-4 text-green-600" />
    case 'failed':
      return <XCircle className="w-4 h-4 text-red-600" />
    case 'running':
      return <Play className="w-4 h-4 text-blue-600 animate-pulse" />
    default:
      return <Clock className="w-4 h-4 text-gray-400" />
  }
}

function getCloudProviderColor(cloudProvider: string | null) {
  switch (cloudProvider) {
    case 'aws':
      return 'bg-orange-100 text-orange-800 border-orange-200'
    case 'gcp':
      return 'bg-blue-100 text-blue-800 border-blue-200'
    default:
      return 'bg-gray-100 text-gray-800 border-gray-200'
  }
}

export const WorkflowNode = memo(({ data }: NodeProps) => {
  const {
    label,
    description,
    cloudProvider,
    toolToUse,
    executedCommand,
    status,
    output,
    error
  } = data as unknown as WorkflowNodeData

  return (
    <div className={cn(
      "relative bg-white rounded-lg border-2 shadow-lg min-w-[280px] max-w-[300px]",
      status === 'running' && "border-blue-400 shadow-blue-200 bg-blue-50",
      status === 'completed' && "border-green-400 shadow-green-200 bg-green-50", 
      status === 'failed' && "border-red-400 shadow-red-200 bg-red-50",
      status === 'pending' && "border-gray-400 bg-white"
    )}>
      {/* Input Handle */}
      <Handle
        type="target"
        position={Position.Top}
        className="w-3 h-3 !bg-gray-700 !border-2 !border-white"
      />
      
      {/* Node Header */}
      <div className={cn(
        "px-4 py-3 border-b bg-gray-100 rounded-t-lg",
        status === 'running' && "bg-blue-100",
        status === 'completed' && "bg-green-100",
        status === 'failed' && "bg-red-100",
        status === 'pending' && "bg-gray-100"
      )}>
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            {getNodeIcon(cloudProvider, toolToUse)}
            <h3 className="font-semibold text-sm text-gray-900 truncate">
              {label}
            </h3>
          </div>
          {getStatusIcon(status)}
        </div>
        
        {cloudProvider && (
          <div className="mt-2">
            <span className={cn(
              "inline-flex items-center px-2 py-1 rounded-full text-xs font-medium border",
              getCloudProviderColor(cloudProvider)
            )}>
              {cloudProvider.toUpperCase()}
            </span>
          </div>
        )}
      </div>

      {/* Node Body */}
      <div className="px-4 py-3">
        <p className="text-sm text-gray-700 mb-3 line-clamp-2">
          {description}
        </p>
        
        <div className="space-y-2">
          <div>
            <span className="text-xs font-medium text-gray-500">Tool:</span>
            <p className="text-xs text-gray-900 font-mono bg-gray-100 px-2 py-1 rounded mt-1">
              {toolToUse}
            </p>
          </div>
          
          {executedCommand && (
            <div>
              <span className="text-xs font-medium text-gray-500">Command:</span>
              <p className="text-xs text-gray-900 font-mono bg-gray-100 px-2 py-1 rounded mt-1 truncate">
                {executedCommand}
              </p>
            </div>
          )}
          
          {status === 'failed' && error && (
            <div>
              <span className="text-xs font-medium text-red-600">Error:</span>
              <p className="text-xs text-red-700 bg-red-50 px-2 py-1 rounded mt-1 line-clamp-2">
                {error}
              </p>
            </div>
          )}
          
          {status === 'completed' && output && (
            <div>
              <span className="text-xs font-medium text-green-600">Output:</span>
              <p className="text-xs text-green-700 bg-green-50 px-2 py-1 rounded mt-1 line-clamp-2">
                {typeof output === 'string' ? output : JSON.stringify(output)}
              </p>
            </div>
          )}
        </div>
      </div>

      {/* Status Indicator */}
      <div className={cn(
        "absolute -top-1 -right-1 w-3 h-3 rounded-full border-2 border-white",
        status === 'running' && "bg-blue-500 animate-pulse",
        status === 'completed' && "bg-green-500",
        status === 'failed' && "bg-red-500",
        status === 'pending' && "bg-gray-400"
      )} />

      {/* Output Handle */}
      <Handle
        type="source"
        position={Position.Bottom}
        className="w-3 h-3 !bg-gray-700 !border-2 !border-white"
      />
    </div>
  )
})

WorkflowNode.displayName = 'WorkflowNode'

export default WorkflowNode 