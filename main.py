from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from database import SessionLocal, engine, Base

from user.router import router as router_user
from var_initial_data.router import router as router_variable
from engine.router import router as router_engine
from variant.router import router as router_variant
from formula.router import router as router_formula
from characteristic.router import router as router_characteristic

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_user)
app.include_router(router_variable)
app.include_router(router_engine)
app.include_router(router_variant)
app.include_router(router_formula)
app.include_router(router_characteristic)





