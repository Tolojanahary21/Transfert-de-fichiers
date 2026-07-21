from fastapi import FastAPI
#import pour les routes 
from app.routes import devices 
from app.routes import files
from app.routes import transfers
#import pour le CORS
from fastapi.middleware.cors import CORSMiddleware 


app = FastAPI(
    title= "P2P Transfert de Fichiers",
    version= "1.0.0"
)


#Routes
app.include_router(devices.router)
app.include_router(files.router)
app.include_router(transfers.router)

#Config CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Tongasoa FastAPI"}
