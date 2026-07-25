import type { FileItem } from "../../types/file"


function FileStats({
  files
}:{
  files:FileItem[]
}){


  const totalSize =
    files.reduce(
      (sum,file)=>sum+file.file_size,
      0
    )


  return (

    <div className="grid md:grid-cols-2 gap-4">


      <div className="border rounded-xl p-5">

        <p>
          Total Files
        </p>

        <h2 className="text-3xl font-bold">
          {files.length}
        </h2>

      </div>



      <div className="border rounded-xl p-5">

        <p>
          Storage
        </p>

        <h2 className="text-3xl font-bold">
          {(totalSize / 1024 /1024).toFixed(2)} MB
        </h2>

      </div>


    </div>

  )

}


export default FileStats