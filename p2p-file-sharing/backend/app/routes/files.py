from fastapi import APIRouter;


router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

@router.get("/")
def get_files():
    return {
        "message": "Liste des fichiers"
    }

@router.post("/")
def create_files():
    return {
        "message": "Fichier cree"
    }

@router.delete("/{file_id}")
def delete_files(file_id: int):
    return {
        "message": f"Fichier {file_id} supprimé"
        }

