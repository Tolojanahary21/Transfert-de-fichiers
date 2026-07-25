import FilesHeader from "../components/files/FilesHeader"
import FileStats from "../components/files/FileStats"
import UploadFile from "../components/files/UploadFile"
import FileTable from "../components/files/FileTable"


import {
useFiles
} from "../hooks/useFiles"



function Files(){


const {
data:files=[],
isLoading
}=useFiles()



if(isLoading){

return <p>Loading...</p>

}



return (

<div className="space-y-8">


<FilesHeader />


<UploadFile />


<FileStats
files={files}
/>


<FileTable
files={files}
/>



</div>

)

}


export default Files