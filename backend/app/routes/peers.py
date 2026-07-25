from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.peer_service import get_device_info
from fastapi import APIRouter
from app.core.p2p import discovery
from app.crud.device import (
    create_device,
    update_heartbeat
)

from app.schemas.device import (
    DeviceCreate,
    DeviceResponse
)
from app.p2p.tcp_client import connect_peer

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
@router.get("/discover")
def discover():

    return discovery.discover()
@router.post("/connect")
def connect(
    ip: str,
    port: int
):

    return connect_peer(
        ip,
        port
    )