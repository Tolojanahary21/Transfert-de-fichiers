import api from "./api"

import type { Device } from "../types/device"


export async function registerDevice(): Promise<Device> {

  const { data } = await api.post<Device>(
    "/peers/register"
  )

  return data

}