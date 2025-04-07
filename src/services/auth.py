from src.utils.security import generate_token, verify_token


class AuthServices:
    def verify_user(self, id: int, email: str, password: str, role: str):
        if email != "test@email" and password != "test":
            return {"msg": "erro"}
        token = generate_token(id, email, role)
        return token
