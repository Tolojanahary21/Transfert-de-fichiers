import {
  useQuery,
  useMutation,
  useQueryClient
} from "@tanstack/react-query"


import {
  getFiles,
  deleteFile,
  uploadFile
} from "../services/fileService"



export function useFiles(){

  return useQuery({

    queryKey:["files"],

    queryFn:getFiles

  })

}



export function useDeleteFile(){

  const queryClient = useQueryClient()


  return useMutation({

    mutationFn:deleteFile,


    onSuccess(){

      queryClient.invalidateQueries({
        queryKey:["files"]
      })

    }

  })

}



export function useUploadFile(){

const queryClient = useQueryClient()


return useMutation({

 mutationFn: ({
    file,
    device_id
 }: {
    file: File,
    device_id:number
 }) =>
 uploadFile(file, device_id),


 onSuccess(){

    queryClient.invalidateQueries({
      queryKey:["files"]
    })

 }

})

}