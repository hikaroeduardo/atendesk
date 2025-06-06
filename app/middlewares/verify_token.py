import os
from dotenv import load_dotenv
from jwt import decode, InvalidTokenError, ExpiredSignatureError
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

security = HTTPBearer()

class Middleware:
    @staticmethod
    def verify_token(schema_token: Annotated[HTTPAuthorizationCredentials, Depends(security)]):

        token = schema_token.credentials
        secret_key = os.getenv("SECRET_KEY_JWT")
        algorithm = os.getenv("ALGORITHM_JWT")

        try:
            token_decode = decode(token, secret_key, algorithms=algorithm)

            user_id = token_decode.get("sub")

            return user_id
        except InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido."
                )
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido."
                )