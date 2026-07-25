from pydantic import BaseModel
from datetime import datetime


class FileBase(BaseModel):

    file_name: str
    file_size: int
    file_type: str
    file_extension: str
    file_hash: str
    file_path: str
    device_id: int



class FileCreate(FileBase):
    pass



class FileResponse(FileBase):

    id: int
    created_at: datetime
    updated_at: datetime | None = None


    class Config:
        from_attributes = True