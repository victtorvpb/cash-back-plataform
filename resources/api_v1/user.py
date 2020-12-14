from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from resources import deps
from commons import schemas, crud


auth_router = APIRouter()


@auth_router.post(
    '/',
    response_model=schemas.User,
    responses={status.HTTP_409_CONFLICT: {"model": schemas.HTTPException}},
)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    if crud.user.get_by_email_or_cpf(db, user_in.email, user_in.cpf):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with this email or cpf already exists in the system",
        )

    user = crud.user.create(db, obj_in=user_in)

    return user
