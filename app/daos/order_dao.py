from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.order_models import Order, OrderItem, Table
from typing import List

class OrderDAO:
    @staticmethod
    async def get(session: AsyncSession, order_id):
        result = await session.execute(select(Order).where(Order.id == order_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def list(session: AsyncSession):
        result = await session.execute(select(Order))
        return result.scalars().all()

    @staticmethod
    async def create(session: AsyncSession, order: Order, items: List[OrderItem]):
        session.add(order)
        for i in items:
            session.add(i)
        await session.commit()
        await session.refresh(order)
        return order
