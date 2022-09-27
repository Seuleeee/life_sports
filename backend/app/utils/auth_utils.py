import os
import bcrypt
import json
import jwt
from pathlib import Path
from datetime import datetime, timedelta

BASE_DIR = str(Path(__file__).parent.parent) + '/config'

# TODO: 설정 관련 파일 관리
SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
secrets = json.loads(open(SECRET_FILE).read())
auth = secrets["auth"]


def hash_password(plain_password: str):
    bytes_password: bytes = plain_password.encode('utf-8')
    salt: bytes = bcrypt.gensalt()
    hashed_password: bytes = bcrypt.hashpw(bytes_password, salt)
    return hashed_password


def verify_password(input_password, stored_password) -> bool:
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_password.encode('utf-8'))


def create_access_token(subject: str, expires_delta: int = None) -> str:
    if expires_delta:
        expires_delta: datetime | int = datetime.now() + expires_delta
    else:
        expires_delta: datetime | int = datetime.now() + timedelta(minutes=auth.get('ACCESS_TOKEN_EXPIRE_MINUTES'))

    to_encode: dict[str, str] = {
        'exp': expires_delta,
        'sub': str(subject)
    }
    encoded_jwt: str = jwt.encode(to_encode, auth.get('JWT_SECRET_KEY'), auth.get('ALGORITHM'))

    return encoded_jwt


def create_refresh_token(subject: str, expires_delta: int = None) -> str:
    if expires_delta:
        expires_delta: datetime | int = datetime.now() + expires_delta
    else:
        expires_delta: datetime | int = datetime.now() + timedelta(minutes=auth.get('REFRESH_TOKEN_EXPIRE_MINUTES'))

    to_encode: dict[str, str] = {
        'exp': expires_delta,
        'sub': str(subject)
    }
    encoded_jwt: str = jwt.encode(to_encode, auth.get('JWT_REFRESH_SECRET_KEY'), auth.get('ALGORITHM'))

    return encoded_jwt
