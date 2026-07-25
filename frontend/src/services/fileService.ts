import api from "./api"

import type { FileItem } from "../types/file"


export async function getFiles(): Promise<FileItem[]> {

  const { data } = await api.get<FileItem[]>(
    "/files"
  )

  return data

}



export async function searchFiles(
  query: string
): Promise<FileItem[]> {


  const { data } = await api.get<FileItem[]>(
    `/files/search?q=${query}`
  )


  return data

}



export async function deleteFile(
  id:number
){

  await api.delete(
    `/files/${id}`
  )

}


export async function uploadFile(
  file: File,
  device_id: number
){

  const formData = new FormData()


  formData.append(
    "file",
    file
  )


  formData.append(
    "device_id",
    device_id.toString()
  )


  const response = await api.post(
    "/files/upload",
    formData
  )


  return response.data
}