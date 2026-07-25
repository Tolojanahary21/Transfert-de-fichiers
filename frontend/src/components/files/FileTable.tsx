import type { FileItem } from "../../types/file"

import {
useDeleteFile
} from "../../hooks/useFiles"



function FileTable({
files
}:{
files:FileItem[]
}){


const deleteMutation =
useDeleteFile()



return (

<div className="border rounded-xl">


<table className="w-full">

<thead>

<tr className="border-b">

<th className="p-3 text-left">
Name
</th>

<th>
Size
</th>

<th>
Type
</th>

<th>
Action
</th>

</tr>

</thead>



<tbody>


{
files.map(file=>(

<tr
key={file.id}
className="border-b"
>


<td className="p-3">
{file.file_name}
</td>


<td>
{
(file.file_size/1024).toFixed(2)
} KB
</td>


<td>
{file.file_type}
</td>


<td>

<button

className="text-red-500"

onClick={()=>deleteMutation.mutate(file.id)}

>
Delete
</button>


</td>


</tr>

))
}


</tbody>


</table>


</div>

)

}


export default FileTable