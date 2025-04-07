from fastapi import APIRouter, status, Depends
from src.models.user import UserModel
from src.services.auth import AuthServices
from src.utils.security import get_user


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", status_code=status.HTTP_200_OK)
def login(user: UserModel):
    service = AuthServices()

    token = service.verify_user(user.id, user.email, user.password, user.role)

    return token


@router.get("/private", dependencies=[Depends(get_user)])
def private_route():
    return {"msg": "voce esta em uma rota que precisa de autenticação"}
