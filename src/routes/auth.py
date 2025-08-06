from fastapi import APIRouter, Depends

from src.core.dependencies.services.auth_service import get_auth_service
from src.models.dto.auth import LoginResponse, LoginCredentials
from src.services.auth_service import AuthService

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post(path='/login', summary='login')
async def login(
        credentials: LoginCredentials,
        auth_service: AuthService = Depends(get_auth_service)
) -> LoginResponse:
    """
    # Mardkdown docstring
    This is a test to see how SwaggerUI handles MD dosctring formatting.

    ## Args
    `codeblock` -  description \n
    `cia` - argument description \n
    """
    # credentials = LoginCredentials(
    #     username=credentials.username,
    #     plain_password=credentials.password
    # )
    jwt_token = await auth_service.login(credentials=credentials)

    return LoginResponse(access_token=jwt_token)
