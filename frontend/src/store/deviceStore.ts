import { create } from "zustand"

import type { Device } from "../types/device"


interface DeviceState {

  device: Device | null

  setDevice: (device: Device) => void

  clearDevice: () => void

}



export const useDeviceStore = create<DeviceState>((set) => ({

  device: null,


  setDevice: (device) =>
    set({
      device
    }),


  clearDevice: () =>
    set({
      device: null
    })

}))