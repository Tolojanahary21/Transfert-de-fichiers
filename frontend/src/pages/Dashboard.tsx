import DashboardHeader from "../components/dashboard/DashboardHeader"
import StatsCards from "../components/dashboard/StatsCards"
import DeviceCard from "../components/dashboard/DeviceCard"
import QuickActions from "../components/dashboard/QuickActions"
import RecentFiles from "../components/dashboard/RecentFiles"
import RecentActivity from "../components/dashboard/RecentActivity"
import SystemStatus from "../components/dashboard/SystemStatus"


function Dashboard(){

  return (

    <div className="space-y-8">

      <DashboardHeader />

      <StatsCards />


      <div className="grid gap-6 lg:grid-cols-2">

        <DeviceCard />

        <QuickActions />

      </div>


      <div className="grid gap-6 lg:grid-cols-2">

        <RecentFiles />

        <RecentActivity />

      </div>


      <SystemStatus />

    </div>

  )
}


export default Dashboard