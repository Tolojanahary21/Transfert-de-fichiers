import {
  Monitor,
  Wifi
} from "lucide-react"


function DeviceCard() {

  const device = {
    name: "DESKTOP-PC",
    ip: "192.168.1.15",
    os: "Windows 11",
    uuid: "xxxx-xxxx",
    port: 8000,
    status: "Online"
  }


  return (
    <div className="rounded-xl border p-6">

      <div className="flex items-center gap-3">

        <Monitor />

        <h2 className="text-xl font-semibold">
          Mon appareil
        </h2>

      </div>


      <div className="mt-5 space-y-3">


        <p>
          <strong>Nom :</strong> {device.name}
        </p>


        <p>
          <strong>IP :</strong> {device.ip}
        </p>


        <p>
          <strong>OS :</strong> {device.os}
        </p>


        <p>
          <strong>UUID :</strong> {device.uuid}
        </p>


        <p>
          <strong>Port :</strong> {device.port}
        </p>


        <div className="flex items-center gap-2">

          <Wifi size={18}/>

          <span className="text-green-600">
            {device.status}
          </span>

        </div>


      </div>


    </div>
  )
}


export default DeviceCard