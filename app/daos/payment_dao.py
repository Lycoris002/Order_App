from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.order_models import Payment

class PaymentDAO:
    @staticmethod
    async def create(session: AsyncSession, payment: Payment) -> Payment:
        session.add(payment)
        await session.commit()
        await session.refresh(payment)
        return payment

    @staticmethod
    async def get(session: AsyncSession, payment_id) -> Payment | None:
        result = await session.execute(select(Payment).where(Payment.id == payment_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def list(session: AsyncSession) -> list[Payment]:
        result = await session.execute(select(Payment))
        return result.scalars().all()
