import { createBrowserRouter, RouterProvider } from "react-router-dom"

import { Navigate } from "react-router-dom"
import MainLayout from "../layouts/MainLayout"
import Dashboard from "../pages/Dashboard"
import Files from "../pages/Files"
import Peers from "../pages/Peers"
import Settings from "../pages/Settings"
import Transfers from "../pages/Transfers"

const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [
        {
            index: true,
            element: <Navigate to="/dashboard" replace />,
        }, 
      {
        path: "dashboard",
        element: <Dashboard />,
      },
      {
        path: "files",
        element: <Files />,
      },
      {
        path: "peers",
        element: <Peers />,
      },
      {
        path: "settings",
        element: <Settings />,
      },
      {
        path: "transfers",
        element: <Transfers />,
      },
    ],
  },
])


function AppRouter() {
  return <RouterProvider router={router} />
}

export default AppRouter