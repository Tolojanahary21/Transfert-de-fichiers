import {
  Upload,
  Search,
  RefreshCcw,
  FolderOpen
} from "lucide-react"


const actions = [
  {
    name:"Upload File",
    icon: Upload
  },
  {
    name:"Browse Files",
    icon: FolderOpen
  },
  {
    name:"Search",
    icon: Search
  },
  {
    name:"Refresh",
    icon: RefreshCcw
  }
]


function QuickActions() {

  return (
    <div className="rounded-xl border p-6">

      <h2 className="text-xl font-semibold">
        Quick Actions
      </h2>


      <div className="mt-5 grid gap-3">

        {
          actions.map((action)=>{

            const Icon = action.icon

            return (
              <button
                key={action.name}
                className="
                flex items-center gap-3
                rounded-lg border p-3
                hover:bg-muted
                "
              >

                <Icon size={18}/>

                {action.name}

              </button>
            )

          })
        }

      </div>


    </div>
  )
}


export default QuickActions