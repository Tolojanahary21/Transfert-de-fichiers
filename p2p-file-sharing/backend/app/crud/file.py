from sqlalchemy.orm import Session

from app.models.file import File
from app.schemas.file import FileCreate


def create_file(db: Session, file: FileCreate):
    new_file = File(**file.model_dump())

    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return new_file


def get_files(db: Session):
    return db.query(File).all()


def get_file_by_id(db: Session, file_id: int):
    return db.query(File).filter(File.id == file_id).first()


def update_file(db: Session, file_id: int, file: FileCreate):
    db_file = get_file_by_id(db, file_id)

    if not db_file:
        return None

    update_data = file.model_dump()

    for key, value in update_data.items():
        setattr(db_file, key, value)

    db.commit()
    db.refresh(db_file)

    return db_file


def delete_file(db: Session, file_id: int):
    db_file = get_file_by_id(db, file_id)

    if not db_file:
        return None

    db.delete(db_file)
    db.commit()

    return db_file