from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.auth import AuthTokenSchema
from app.business.auth import AuthBusiness

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/login', response_model=AuthTokenSchema)
async def login(email: str = Form(...), password: str = Form(), db: Session = Depends(get_db)):
    return AuthBusiness().login(email=email, password=password, db=db)
