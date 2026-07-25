import {
  Files,
  Users,
  ArrowLeftRight,
  HardDrive
} from "lucide-react"


const stats = [
  {
    title: "Shared Files",
    value: 18,
    icon: Files,
  },
  {
    title: "Connected Peers",
    value: 4,
    icon: Users,
  },
  {
    title: "Transfers",
    value: 12,
    icon: ArrowLeftRight,
  },
  {
    title: "Storage Used",
    value: "2.3 GB",
    icon: HardDrive,
  },
]


function StatsCards() {
  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">

      {stats.map((stat) => {

        const Icon = stat.icon

        return (
          <div
            key={stat.title}
            className="rounded-xl border p-5"
          >

            <div className="flex items-center justify-between">

              <p className="text-sm text-muted-foreground">
                {stat.title}
              </p>

              <Icon size={20}/>

            </div>


            <h2 className="mt-4 text-3xl font-bold">
              {stat.value}
            </h2>


          </div>
        )

      })}

    </div>
  )
}

export default StatsCards