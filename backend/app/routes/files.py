from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.file import search_files
from app.database.database import get_db
from app.schemas.file import FileCreate, FileResponse
from app.crud.file import (
    create_file,
    get_files,
    get_file_by_id,
    update_file,
    delete_file
)
#upload
import os
from fastapi import UploadFile, File as FastAPIFile
from app.services.file_service import (
    save_file,
    calculate_hash
)
#down
from fastapi.responses import FileResponse as FastAPIFileResponse
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

#pour la recherche
@router.get("/search", response_model=list[FileResponse])
def search(
    q: str,
    db: Session = Depends(get_db)
):

    return search_files(
        db,
        q
    )
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
#pour l'upload
@router.post(
    "/upload",
    response_model=FileResponse
)
def upload(
    device_id: int,
    file: UploadFile = FastAPIFile(...),
    db: Session = Depends(get_db)
):

    # Sauvegarde physique
    file_path = save_file(file)

    # Calcul SHA-256
    file_hash = calculate_hash(file_path)

    extension = (
        file.filename.split(".")[-1]
        if "." in file.filename
        else ""
    )

    new_file = FileCreate(
        device_id=device_id,
        file_name=file.filename,
        file_size=os.path.getsize(file_path),
        file_type=file.content_type,
        file_extension=extension,
        file_hash=file_hash,
        file_path=file_path
    )

    return create_file(
        db,
        new_file
    )

#down des fichiers 
@router.get("/download/{file_id}")
def download_file(file_id: int, db: Session = Depends(get_db)):
    file = get_file_by_id(db, file_id)

    if file is None:
        raise HTTPException(status_code=404, detail="File not found")

    if not os.path.exists(file.file_path):
        raise HTTPException(status_code=404, detail="Physical file not found")

    return FastAPIFileResponse(
        path=file.file_path,
        filename=file.file_name
    )
