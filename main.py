from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from database import SessionLocal, engine, Base

from user.router import router as router_user

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_user)




