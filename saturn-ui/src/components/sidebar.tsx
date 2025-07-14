import { cn } from "@/lib/utils"
import { 
  Settings, 
  HelpCircle, 
  User, 
  Clock, 
  BarChart3,
  FileText,
  Upload
} from "lucide-react"

interface SidebarProps {
  onFileUpload: (file: File) => void
  workflows: Array<{id: string, name: string, status: 'idle' | 'running' | 'completed' | 'failed'}>
  selectedWorkflow?: string
  onSelectWorkflow: (id: string) => void
}

export function Sidebar({ 
  onFileUpload, 
  workflows, 
  selectedWorkflow, 
  onSelectWorkflow 
}: SidebarProps) {
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file && file.name.endsWith('.sat')) {
      onFileUpload(file)
    }
  }

  return (
    <div className="w-64 bg-gray-900 text-white flex flex-col h-full">
      {/* Header */}
      <div className="p-4 border-b border-gray-700">
        <h1 className="text-xl font-bold flex items-center gap-2">
          <div className="w-8 h-8 bg-blue-600 rounded flex items-center justify-center">
            <span className="text-sm font-bold">S</span>
          </div>
          Saturn UI
        </h1>
      </div>

      {/* Upload Section */}
      <div className="p-4 border-b border-gray-700">
        <label className="flex items-center justify-center w-full p-3 border-2 border-gray-600 border-dashed rounded-lg cursor-pointer hover:bg-gray-800 transition-colors">
          <Upload className="w-5 h-5 mr-2" />
          <span className="text-sm">Upload .sat file</span>
          <input 
            type="file" 
            className="hidden" 
            accept=".sat"
            onChange={handleFileChange}
          />
        </label>
      </div>

      {/* Navigation */}
      <div className="flex-1 overflow-y-auto">
        <nav className="p-4 space-y-2">
          <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">
            Workflows
          </div>
          
          {workflows.length === 0 ? (
            <div className="text-sm text-gray-500 text-center py-8">
              No workflows loaded.
              <br />
              Upload a .sat file to get started.
            </div>
          ) : (
            workflows.map((workflow) => (
              <button
                key={workflow.id}
                onClick={() => onSelectWorkflow(workflow.id)}
                className={cn(
                  "w-full flex items-center gap-3 p-3 rounded-lg text-left transition-colors",
                  selectedWorkflow === workflow.id 
                    ? "bg-blue-600 text-white" 
                    : "hover:bg-gray-800 text-gray-300"
                )}
              >
                <div className={cn(
                  "w-2 h-2 rounded-full",
                  workflow.status === 'running' && "bg-green-500 animate-pulse",
                  workflow.status === 'completed' && "bg-green-500",
                  workflow.status === 'failed' && "bg-red-500",
                  workflow.status === 'idle' && "bg-gray-500"
                )} />
                <div className="flex-1 min-w-0">
                  <div className="text-sm font-medium truncate">{workflow.name}</div>
                  <div className="text-xs text-gray-400 capitalize">{workflow.status}</div>
                </div>
              </button>
            ))
          )}

          <div className="pt-6 space-y-2">
            <div className="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">
              Tools
            </div>
            
            <button className="w-full flex items-center gap-3 p-3 rounded-lg text-left hover:bg-gray-800 text-gray-300 transition-colors">
              <BarChart3 className="w-5 h-5" />
              <span className="text-sm">Executions</span>
            </button>
            
            <button className="w-full flex items-center gap-3 p-3 rounded-lg text-left hover:bg-gray-800 text-gray-300 transition-colors">
              <Clock className="w-5 h-5" />
              <span className="text-sm">History</span>
            </button>
            
            <button className="w-full flex items-center gap-3 p-3 rounded-lg text-left hover:bg-gray-800 text-gray-300 transition-colors">
              <FileText className="w-5 h-5" />
              <span className="text-sm">Logs</span>
            </button>
          </div>
        </nav>
      </div>

      {/* Footer */}
      <div className="p-4 border-t border-gray-700 space-y-2">
        <button className="w-full flex items-center gap-3 p-3 rounded-lg text-left hover:bg-gray-800 text-gray-300 transition-colors">
          <Settings className="w-5 h-5" />
          <span className="text-sm">Settings</span>
        </button>
        
        <button className="w-full flex items-center gap-3 p-3 rounded-lg text-left hover:bg-gray-800 text-gray-300 transition-colors">
          <HelpCircle className="w-5 h-5" />
          <span className="text-sm">Help</span>
        </button>
        
        <div className="flex items-center gap-3 p-3 text-gray-400">
          <User className="w-5 h-5" />
          <span className="text-sm">Saturn User</span>
        </div>
      </div>
    </div>
  )
} 