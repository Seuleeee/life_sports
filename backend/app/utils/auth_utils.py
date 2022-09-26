import bcrypt


def hash_password(plain_password: str):
    bytes_password: bytes = plain_password.encode('utf-8')
    salt: bytes = bcrypt.gensalt()
    hashed_password: bytes = bcrypt.hashpw(bytes_password, salt)
    return hashed_password


def verify_password(input_password, stored_password) -> bool:
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_password.encode('utf-8'))

