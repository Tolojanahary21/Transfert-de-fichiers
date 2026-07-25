function RecentFiles() {


  const files = [
    {
      name:"document.pdf",
      size:"2 MB",
      type:"PDF"
    },
    {
      name:"image.png",
      size:"500 KB",
      type:"PNG"
    }
  ]


  return (
    <div className="rounded-xl border p-6">

      <h2 className="text-xl font-semibold">
        Recent Files
      </h2>


      <div className="mt-5 space-y-3">

        {
          files.map(file=>(
            <div
              key={file.name}
              className="flex justify-between"
            >

              <span>
                {file.name}
              </span>

              <span>
                {file.size}
              </span>

            </div>
          ))
        }

      </div>


    </div>
  )
}


export default RecentFiles