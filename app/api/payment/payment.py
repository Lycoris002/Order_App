import uuid
from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dtos.payment_dto import PaymentCreateDTO, PaymentReadDTO
from app.models.order_models import Payment
from app.daos.payment_dao import PaymentDAO
from app.utils.db_utils import create_database_session

router = APIRouter(prefix="/payments", tags=["payments"])

@router.post("/", response_model=PaymentReadDTO)
async def create_payment(
    payload: PaymentCreateDTO,
    session: Annotated[AsyncSession, Depends(create_database_session)]
):
    new_payment = Payment(
        id=uuid.uuid4(),
        order_id=payload.order_id,
        amount=payload.amount,
        payment_method=payload.payment_method,
        status="pending"
    )
    return await PaymentDAO.create(session, new_payment)


@router.get("/{payment_id}", response_model=PaymentReadDTO)
async def get_payment(
    payment_id: uuid.UUID,
    session: Annotated[AsyncSession, Depends(create_database_session)]
):
    payment = await PaymentDAO.get(session, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


@router.get("/", response_model=List[PaymentReadDTO])
async def list_payments(
    session: Annotated[AsyncSession, Depends(create_database_session)]
):
    return await PaymentDAO.list(session)
