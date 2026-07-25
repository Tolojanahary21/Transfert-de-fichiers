function RecentActivity(){

  const activities = [
    "Device registered",
    "file.pdf uploaded",
    "Peer connected"
  ]


  return (
    <div className="rounded-xl border p-6">

      <h2 className="text-xl font-semibold">
        Recent Activity
      </h2>


      <div className="mt-5 space-y-3">

        {
          activities.map(activity=>(
            <p key={activity}>
              • {activity}
            </p>
          ))
        }

      </div>


    </div>
  )
}


export default RecentActivity