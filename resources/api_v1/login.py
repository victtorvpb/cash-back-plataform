from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import logging

from commons.config import settings
from commons.utils import security
from commons import schemas
from commons import crud
from resources import deps


login_router = APIRouter()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@login_router.post(
    '/access-token',
    response_model=schemas.Token,
    responses={status.HTTP_400_BAD_REQUEST: {"model": schemas.HTTPException}},
)
async def login_access_token(
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Any:

    logger.info(f"login_access_token: Login with access token for user {form_data.username,}")
    user = crud.user.authenticate(db, email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect email or password',
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        'access_token': security.create_access_token(user.id, expires_delta=access_token_expires),
        'token_type': 'bearer',
    }
