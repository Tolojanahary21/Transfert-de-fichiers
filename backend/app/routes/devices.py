from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.device import DeviceCreate, DeviceResponse

from app.crud.device import (
    create_device,
    get_devices,
    get_device_by_id,
    update_device,
    delete_device
)


router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)


# CREATE
@router.post("/", response_model=DeviceResponse)
def create(
    device: DeviceCreate,
    db: Session = Depends(get_db)
):
    return create_device(db, device)


# READ ALL
@router.get("/", response_model=list[DeviceResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_devices(db)


# READ ONE
@router.get("/{device_id}", response_model=DeviceResponse)
def get_one(
    device_id: int,
    db: Session = Depends(get_db)
):
    device = get_device_by_id(db, device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return device


# UPDATE
@router.put("/{device_id}", response_model=DeviceResponse)
def update(
    device_id: int,
    device: DeviceCreate,
    db: Session = Depends(get_db)
):
    updated_device = update_device(
        db,
        device_id,
        device
    )

    if updated_device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return updated_device


# DELETE
@router.delete("/{device_id}")
def delete(
    device_id: int,
    db: Session = Depends(get_db)
):
    deleted_device = delete_device(
        db,
        device_id
    )

    if deleted_device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return {
        "message": "Device deleted successfully"
    }