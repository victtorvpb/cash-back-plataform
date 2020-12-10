from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import logging

from commons.config import settings
from commons.utils import security, auth
from commons import schemas
from commons import crud
from resources import deps


login_router = APIRouter()


log = logging.getLogger()


@login_router.post(
    '/access-token',
    response_model=schemas.Token,
    responses={status.HTTP_400_BAD_REQUEST: {"model": schemas.HTTPException}},
)
async def login_access_token(
    db: Session = Depends(deps.get_db),
    form_data: auth.CustomOAuth2PasswordRequestForm = Depends(),
) -> Any:

    log.info(f"login_access_token: Login with access token for user {form_data.email,}")
    user = crud.user.authenticate(db, email=form_data.email, password=form_data.password)

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