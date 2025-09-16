from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils.db_utils import create_database_session
from app.daos.order_dao import OrderDAO
from app.dtos.order_dto import OrderCreateDTO, OrderReadDTO
from app.models.order_models import Order, OrderItem
import uuid

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=OrderReadDTO)
async def create_order(
    payload: OrderCreateDTO,
    session: Annotated[AsyncSession, Depends(create_database_session)]
):
    order = Order(
        id=uuid.uuid4(),
        table_id=payload.table_id,
        total_amount=sum(i.price * i.quantity for i in payload.items),
        status="pending"
    )
    items = [
        OrderItem(
            id=uuid.uuid4(),
            order_id=order.id,
            item_name=i.item_name,
            quantity=i.quantity,
            price=i.price,
        )
        for i in payload.items
    ]
    return await OrderDAO.create(session, order, items)
