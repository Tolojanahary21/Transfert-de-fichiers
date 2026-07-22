from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.file import FileCreate, FileResponse
from app.crud.file import (
    create_file,
    get_files,
    get_file_by_id,
    update_file,
    delete_file
)

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.post("/", response_model=FileResponse)
def create(file: FileCreate, db: Session = Depends(get_db)):
    return create_file(db, file)


@router.get("/", response_model=list[FileResponse])
def get_all(db: Session = Depends(get_db)):
    return get_files(db)


@router.get("/{file_id}", response_model=FileResponse)
def get_one(file_id: int, db: Session = Depends(get_db)):
    file = get_file_by_id(db, file_id)

    if file is None:
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return file


@router.put("/{file_id}", response_model=FileResponse)
def update(file_id: int, file: FileCreate, db: Session = Depends(get_db)):
    updated_file = update_file(db, file_id, file)

    if updated_file is None:
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return updated_file


@router.delete("/{file_id}")
def delete(file_id: int, db: Session = Depends(get_db)):
    deleted_file = delete_file(db, file_id)

    if deleted_file is None:
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return {
        "message": "File deleted successfully"
    }