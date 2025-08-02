from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.core.dependencies.services.auth_service import get_auth_service
from src.models.dto.auth import LoginResponse, LoginCredentials
from src.services.auth_service import AuthService

router = APIRouter(prefix='/auth')


@router.post(path='/login', summary='login')
async def login(
        # credentials: LoginCredentials,
        form_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends(get_auth_service)
) -> LoginResponse:
    """
    docstig
    """
    credentials = LoginCredentials(
        username=form_data.username,
        plain_password=form_data.password
    )
    jwt_token = await auth_service.login(credentials=credentials)

    return LoginResponse(access_token=jwt_token)
