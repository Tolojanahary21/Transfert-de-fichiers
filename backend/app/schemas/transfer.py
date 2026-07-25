from pydantic import BaseModel
from datetime import datetime


class TransferBase(BaseModel):

    file_id: int
    sender_id: int
    receiver_id: int
    status: str = "PENDING"
    progress: int = 0



class TransferCreate(TransferBase):
    pass



class TransferResponse(TransferBase):

    id: int
    created_at: datetime
    updated_at: datetime | None = None


    class Config:
        from_attributes = True