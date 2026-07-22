from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.peer_service import get_device_info

from app.crud.device import (
    create_device,
    update_heartbeat
)

from app.schemas.device import (
    DeviceCreate,
    DeviceResponse
)


router = APIRouter(
    prefix="/peers",
    tags=["Peers"]
)


# Enregistrer automatiquement un pair
@router.post(
    "/register",
    response_model=DeviceResponse
)
def register_peer(
    db: Session = Depends(get_db)
):

    # Récupération automatique des informations machine
    device_info = get_device_info()

    # Transformation en schema Pydantic
    device = DeviceCreate(**device_info)

    # Enregistrement en base
    new_device = create_device(
        db,
        device
    )

    return new_device



# Envoyer un heartbeat pour signaler que le pair est actif
@router.put(
    "/{device_uuid}/heartbeat",
    response_model=DeviceResponse
)
def heartbeat(
    device_uuid: str,
    db: Session = Depends(get_db)
):

    device = update_heartbeat(
        db,
        device_uuid
    )

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return device