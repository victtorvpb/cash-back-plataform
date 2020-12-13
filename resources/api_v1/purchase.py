import logging

from uuid import uuid4
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from resources import deps
from commons import schemas, crud, models

log = logging.getLogger()

purchase_router = APIRouter()


@purchase_router.post(
    '/purchase',
    response_model=schemas.Pusrchase,
    responses= {status.HTTP_400_BAD_REQUEST: {"model": schemas.HTTPException},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": schemas.HTTPException}},
)
def create_purchase(
    *,
    db: Session = Depends(deps.get_db),
    puchase_in: schemas.PurchaseCreate,
    # current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    
    request_uuid = str(uuid4())
    
    user = crud.user.get_by_cpf(db, puchase_in.cpf)

    if not user:
        log.warning(f'create_purchase Not user in database with cpf {puchase_in.cpf}')
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not user with cpf",
        )

    purchase_in_bd = crud.purchase.get_purchase_by_code(db, code=puchase_in.code, request_uuid=request_uuid)

    if purchase_in_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Purchase with code {puchase_in.code} exist in db",
        )

    
    purchase = crud.purchase.create(db, obj_in=puchase_in, user_id= user.id, request_uuid=request_uuid)

    return purchase


@purchase_router.get(
    '/purchase',
    response_model=List[schemas.Pusrchase],
    responses= {status.HTTP_400_BAD_REQUEST: {"model": schemas.HTTPException},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": schemas.HTTPException}},
)
def list_purchase(
    *,
    db: Session = Depends(deps.get_db),
    page: int =0,
    # current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:

    purchases = crud.purchase.get_multi(db, skip=page)
    return purchases
