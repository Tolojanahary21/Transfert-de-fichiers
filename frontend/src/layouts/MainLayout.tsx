import { Outlet } from "react-router-dom"

import Sidebar from "../components/sidebar/Sidebar"
import Navbar from "../components/navbar/Navbar"


function MainLayout() {
  return (
    <div className="flex min-h-screen">

      <Sidebar />


      <div className="flex-1">

        <Navbar />

        <main className="p-6">
          <Outlet />
        </main>

      </div>


    </div>
  )
}

export default MainLayout