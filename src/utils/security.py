from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer


ouath2_schema = OAuth2PasswordBearer(tokenUrl="token")

SECRET = "my-secret"
ALGORITHM = "HS256"


def generate_token(id: int, email: str, role: str):
    expiration = datetime.utcnow() + timedelta(minutes=30)
    payload = {"sub": str(id), "exp": expiration, "email": email, "role": role}

    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    return {"access_token": token}


def verify_token(token: str):
    decoded_token = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    return decoded_token.get("sub")


def get_user(token: str = Depends(ouath2_schema)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalido"
    )
    try:
        user_id = verify_token(token)
    except JWTError:
        raise exception

    if not user_id:
        raise exception

    user = {"email": "test@email", "role": "default"}

    return user
