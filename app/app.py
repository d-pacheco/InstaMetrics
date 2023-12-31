from fastapi import FastAPI
from db.database import engine, SessionLocal
from db import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
