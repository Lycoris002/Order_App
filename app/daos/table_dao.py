from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.order_models import Table

class TableDAO:
    @staticmethod
    async def create(session: AsyncSession, table: Table) -> Table:
        session.add(table)
        await session.commit()
        await session.refresh(table)
        return table

    @staticmethod
    async def get(session: AsyncSession, table_id) -> Table | None:
        result = await session.execute(select(Table).where(Table.id == table_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def list(session: AsyncSession) -> list[Table]:
        result = await session.execute(select(Table))
        return list(result.scalars().all())
