import { cn } from "@/lib/utils"
import { 
  Play, 
  Square, 
  RotateCcw, 
  Save, 
  Share, 
  Tag,
  Activity
} from "lucide-react"

interface TopBarProps {
  workflowName?: string
  workflowStatus: 'idle' | 'running' | 'completed' | 'failed'
  onExecute: () => void
  onStop: () => void
  onSave: () => void
  isExecuting: boolean
}

export function TopBar({ 
  workflowName = "No workflow selected",
  workflowStatus,
  onExecute,
  onStop,
  onSave,
  isExecuting
}: TopBarProps) {
  return (
    <div className="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6">
      {/* Left Section - Workflow Info */}
      <div className="flex items-center gap-4">
        <div className="flex items-center gap-3">
          <h2 className="text-lg font-semibold text-gray-900 truncate max-w-md">
            {workflowName}
          </h2>
          <div className={cn(
            "px-2 py-1 rounded-full text-xs font-medium flex items-center gap-1",
            workflowStatus === 'running' && "bg-green-100 text-green-800",
            workflowStatus === 'completed' && "bg-blue-100 text-blue-800", 
            workflowStatus === 'failed' && "bg-red-100 text-red-800",
            workflowStatus === 'idle' && "bg-gray-100 text-gray-800"
          )}>
            <div className={cn(
              "w-1.5 h-1.5 rounded-full",
              workflowStatus === 'running' && "bg-green-500 animate-pulse",
              workflowStatus === 'completed' && "bg-blue-500",
              workflowStatus === 'failed' && "bg-red-500",
              workflowStatus === 'idle' && "bg-gray-500"
            )} />
            {workflowStatus === 'running' ? 'Executing' : workflowStatus}
          </div>
        </div>
        
        <button className="flex items-center gap-1 px-3 py-1 text-sm text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md transition-colors">
          <Tag className="w-4 h-4" />
          Add Tag
        </button>
      </div>

      {/* Right Section - Controls */}
      <div className="flex items-center gap-3">
        {/* Execution Controls */}
        <div className="flex items-center gap-2">
          {!isExecuting ? (
            <button
              onClick={onExecute}
              disabled={!workflowName || workflowName === "No workflow selected"}
              className={cn(
                "flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-colors",
                !workflowName || workflowName === "No workflow selected"
                  ? "bg-gray-100 text-gray-400 cursor-not-allowed"
                  : "bg-green-600 text-white hover:bg-green-700"
              )}
            >
              <Play className="w-4 h-4" />
              Execute
            </button>
          ) : (
            <button
              onClick={onStop}
              className="flex items-center gap-2 px-4 py-2 bg-red-600 text-white rounded-lg font-medium hover:bg-red-700 transition-colors"
            >
              <Square className="w-4 h-4" />
              Stop
            </button>
          )}
          
          <button
            onClick={onSave}
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 transition-colors"
          >
            <Save className="w-4 h-4" />
            Save
          </button>
        </div>

        <div className="w-px h-6 bg-gray-300" />

        {/* Additional Controls */}
        <button className="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors">
          <RotateCcw className="w-5 h-5" />
        </button>
        
        <button className="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors">
          <Share className="w-5 h-5" />
        </button>
        
        <button className="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors">
          <Activity className="w-5 h-5" />
        </button>
      </div>
    </div>
  )
} 