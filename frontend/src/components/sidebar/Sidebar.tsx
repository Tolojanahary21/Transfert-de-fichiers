import { NavLink } from "react-router-dom"

import {
  LayoutDashboard,
  Files,
  Users,
  ArrowLeftRight,
  Settings
} from "lucide-react"


const menuItems = [
  {
    name: "Dashboard",
    path: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    name: "Files",
    path: "/files",
    icon: Files,
  },
  {
    name: "Peers",
    path: "/peers",
    icon: Users,
  },
  {
    name: "Transfers",
    path: "/transfers",
    icon: ArrowLeftRight,
  },
  {
    name: "Settings",
    path: "/settings",
    icon: Settings,
  },
]


function Sidebar() {
  return (
    <aside className="w-64 min-h-screen border-r bg-background p-5">

      <h1 className="text-xl font-bold mb-8">
        P2P Sharing
      </h1>


      <nav className="space-y-2">

        {menuItems.map((item) => {

          const Icon = item.icon

          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({isActive}) =>
                `
                flex items-center gap-3 rounded-lg px-3 py-2 text-sm
                ${
                  isActive
                    ? "bg-primary text-primary-foreground"
                    : "hover:bg-muted"
                }
                `
              }
            >

              <Icon size={20}/>

              {item.name}

            </NavLink>
          )

        })}

      </nav>

    </aside>
  )
}


export default Sidebar