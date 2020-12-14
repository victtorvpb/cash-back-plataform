import logging

from uuid import uuid4
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from resources import deps
from commons import schemas, crud, services, models
from commons.utils.format import format_cpf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

purchase_router = APIRouter()


@purchase_router.post(
    '/purchase',
    response_model=schemas.Pusrchase,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": schemas.HTTPException},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": schemas.HTTPException},
    },
)
def create_purchase(
    *,
    db: Session = Depends(deps.get_db),
    puchase_in: schemas.PurchaseCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:

    request_uuid = str(uuid4())

    user = crud.user.get_by_cpf(db, puchase_in.cpf)

    if not user:
        logger.warning(f'create_purchase Not user in database with cpf {puchase_in.cpf}')
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not user with cpf",
        )

    purchase_in_bd = crud.purchase.get_purchase_by_code(
        db, code=puchase_in.code, request_uuid=request_uuid
    )

    if purchase_in_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Purchase with code {puchase_in.code} exist in db",
        )

    purchase = crud.purchase.create(
        db, obj_in=puchase_in, user_id=user.id, request_uuid=request_uuid
    )

    return purchase


@purchase_router.get(
    '/purchase',
    response_model=List[schemas.Pusrchase],
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": schemas.HTTPException},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": schemas.HTTPException},
    },
)
def list_purchase(
    *,
    db: Session = Depends(deps.get_db),
    page: int = 0,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    purchases = crud.purchase.get_multi(db, skip=page)
    return purchases


@purchase_router.get(
    '/credit-delear',
    response_model=schemas.PurcahseCredit,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": schemas.HTTPException},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": schemas.HTTPException},
    },
)
def reseller_credit(
    *,
    db: Session = Depends(deps.get_db),
    reseller_cpf: str,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:

    reseller_cpf = format_cpf(reseller_cpf)
    user = crud.user.get_by_cpf(db, reseller_cpf)

    if not user:
        logger.warning(f'create_purchase Not user in database with cpf {reseller_cpf}')
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not user with cpf",
        )
    reseller_credit = services.get_credit_value(reseller_cpf)
    if reseller_credit:
        return reseller_credit

    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Not possible get delear credit"
    )
