function SystemStatus(){

  const status = [
    "Backend Connected",
    "Database Available",
    "API Running",
    "Peer Registered"
  ]


  return (
    <div className="rounded-xl border p-6">

      <h2 className="text-xl font-semibold">
        System Status
      </h2>


      <div className="mt-5 space-y-3">

        {
          status.map(item=>(
            <div
              key={item}
              className="flex justify-between"
            >

              <span>
                {item}
              </span>

              <span className="text-green-600">
                ● Online
              </span>

            </div>
          ))
        }

      </div>


    </div>
  )
}


export default SystemStatus