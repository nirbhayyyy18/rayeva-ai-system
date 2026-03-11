from fastapi import FastAPI

from backend.routes import category_routes, proposal_routes

from backend.database.database import engine
from backend.database.models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(category_routes.router)

app.include_router(proposal_routes.router)

@app.get("/")
def home():
    return {"message": "Rayeva AI System Running"}