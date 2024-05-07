from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from database import SessionLocal, engine, Base

from user.router import router as router_user
from variable.router import router as router_variable
from engine.router import router as router_engine
from variant.router import router as router_variant

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_user)
app.include_router(router_variable)
app.include_router(router_engine)
app.include_router(router_variant)




