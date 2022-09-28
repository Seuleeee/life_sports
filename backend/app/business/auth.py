from fastapi import Form, HTTPException, status
from sqlalchemy.orm import Session

from app.services.user_service import UserService
from app.utils.auth_utils import verify_password, create_access_token, create_refresh_token


class AuthBusiness:
    def login(self, user_id: Form(), password: Form(), db: Session):
        user = UserService().read(db=db, user_id=user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not valid user!'
            )
        is_verified_password: bool = verify_password(password, user.password)
        if is_verified_password:
            return {
                'access_token': create_access_token(user_id),
                'refresh_token': create_refresh_token(user_id),
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not valid user!'
            )


