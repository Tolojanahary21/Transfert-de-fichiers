import { useRef, useState } from "react"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { create } from "zustand"
import api from "../../api/axios" // ajuste le chemin selon l'emplacement réel de ce fichier

// ---------------------------------------------------------------------------
// Store device (temporaire, en attendant un vrai système d'auth/device)
// ---------------------------------------------------------------------------
interface Device {
  id: number
}

interface DeviceStore {
  device: Device | null
}

const useDeviceStore = create<DeviceStore>(() => ({
  device: { id: 1 }, // TODO: remplacer une fois l'enregistrement du device en place
}))

// ---------------------------------------------------------------------------
// Types - correspond au FileResponse de ton backend
// ---------------------------------------------------------------------------
interface FileRecord {
  id: number
  device_id: number
  file_name: string
  file_size: number
  file_type: string
  file_extension: string
  file_hash: string
  file_path: string
  created_at: string
}

interface UploadPayload {
  file: File
  device_id: number
}

// ---------------------------------------------------------------------------
// Hook - useMutation gère l'appel POST vers ton backend
// ---------------------------------------------------------------------------
function useUploadFile() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async ({ file, device_id }: UploadPayload) => {
      const formData = new FormData()
      formData.append("file", file)

      const response = await api.post<FileRecord>(
        `/files/upload?device_id=${device_id}`,
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      )
      return response.data
    },
    onSuccess: () => {
      // recharge automatiquement la liste des fichiers si tu utilises
      // useQuery({ queryKey: ["files"], ... }) ailleurs pour l'afficher
      queryClient.invalidateQueries({ queryKey: ["files"] })
    },
  })
}

// ---------------------------------------------------------------------------
// Composant
// ---------------------------------------------------------------------------
function UploadFile() {
  const uploadMutation = useUploadFile()
  const device = useDeviceStore((state) => state.device)
  const inputRef = useRef<HTMLInputElement>(null)
  const [deviceError, setDeviceError] = useState(false)

  function handleUpload(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0]

    if (!file) {
      return
    }

    if (!device) {
      console.error("Device introuvable")
      setDeviceError(true)
      e.target.value = ""
      return
    }

    setDeviceError(false)

    uploadMutation.mutate(
      { file, device_id: device.id },
      {
        onSettled: () => {
          if (inputRef.current) inputRef.current.value = ""
        },
      }
    )
  }

  return (
    <div className="space-y-3">
      <input
        ref={inputRef}
        type="file"
        onChange={handleUpload}
        disabled={uploadMutation.isPending}
      />

      {deviceError && (
        <p className="text-red-600">
          Aucun appareil détecté. Réessaie une fois connecté.
        </p>
      )}

      {uploadMutation.isPending && <p>Upload en cours...</p>}

      {uploadMutation.isSuccess && (
        <p className="text-green-600">Upload terminé</p>
      )}

      {uploadMutation.isError && (
        <p className="text-red-600">Erreur upload</p>
      )}
    </div>
  )
}

export default UploadFile