from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import inspect

from .package.database.database import engine
from .package.classes.LoadData import LoadData
from .package.database import crud, models, schemas
from .dependencies import get_db
from .routers import city_route, departures
from .package.database.Model import Model

# Model.metadata.drop_all(bind=engine)
# Model.metadata.create_all(bind=engine)

# load_all_files = LoadData()
# load_all_files()

app = FastAPI()

app.include_router(city_route.router)
app.include_router(departures.router)

@app.get("/")
async def root(db: Session = Depends(get_db)):
    return {"message": "Hello World"}

