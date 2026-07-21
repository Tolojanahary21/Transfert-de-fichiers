from pydantic import BaseModel
from datetime import datetime


class DeviceBase(BaseModel):

    device_uuid: str
    device_name: str
    ip_address: str
    port: int
    os: str
    status: str = "OFFLINE"


class DeviceCreate(DeviceBase):
    pass


class DeviceResponse(DeviceBase):

    id: int
    last_seen: datetime | None = None
    created_at: datetime
    updated_at: datetime | None = None


    class Config:
        from_attributes = True