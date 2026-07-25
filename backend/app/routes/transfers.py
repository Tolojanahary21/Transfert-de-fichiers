from fastapi import APIRouter;


router = APIRouter(
    prefix="/transfers",
    tags=["Transfers"]
)

@router.get("/")
def get_transfers():
    return {
        "message": "Liste des transferts"
    }

@router.post("/")
def create_transfers():
    return {
        "message": "Transfert cree"
    }

@router.delete("/{transfer_id}")
def delete_transfers(transfer_id: int):
    return {
        "message": f"Transfert {transfer_id} supprimé"
        }

