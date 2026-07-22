from sqlalchemy.orm import Session

from app.models.device import Device
from app.schemas.device import DeviceCreate
from datetime import datetime

def create_device(db: Session, device: DeviceCreate):
    new_device = Device(**device.model_dump())

    db.add(new_device)
    db.commit()
    db.refresh(new_device)

    return new_device


def get_devices(db: Session):
    return db.query(Device).all()


def get_device_by_id(db: Session, device_id: int):
    return db.query(Device).filter(Device.id == device_id).first()


def update_device(db: Session, device_id: int, device: DeviceCreate):
    db_device = get_device_by_id(db, device_id)

    if not db_device:
        return None

    update_data = device.model_dump()

    for key, value in update_data.items():
        setattr(db_device, key, value)

    db.commit()
    db.refresh(db_device)

    return db_device


def delete_device(db: Session, device_id: int):
    db_device = get_device_by_id(db, device_id)

    if not db_device:
        return None

    db.delete(db_device)
    db.commit()

    return db_device
#pour savoir si je suis toujours en ligne
def update_heartbeat(db: Session, device_uuid: str):

    device = db.query(Device).filter(
        Device.device_uuid == device_uuid
    ).first()

    if not device:
        return None

    device.status = "ONLINE"
    device.last_seen = datetime.now()

    db.commit()
    db.refresh(device)

    return device