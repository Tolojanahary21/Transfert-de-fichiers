import { useQuery } from "@tanstack/react-query"
import { useEffect } from "react"

import { registerDevice } from "../services/deviceService"

import {
  useDeviceStore
} from "../store/deviceStore"



export function useDevice() {


  const setDevice = useDeviceStore(
    (state)=>state.setDevice
  )


  const query = useQuery({

    queryKey:["device"],

    queryFn: registerDevice

  })


  useEffect(()=>{

    if(query.data){

      setDevice(query.data)

    }

  },[
    query.data,
    setDevice
  ])



  return query

}