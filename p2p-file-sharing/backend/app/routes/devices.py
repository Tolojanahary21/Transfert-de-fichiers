from fastapi import APIRouter;


router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)

@router.get("/")
def get_devices():
    return {
        "message": "Liste des apps connectees"
    }

@router.post("/")
def create_devices():
    return {
        "message": "App connectee creee"
        }

@router.delete("/{device_id}")
def delete_devices(device_id: int):
    return { 
        "message": f"Device {device_id} supprimé"
        }

