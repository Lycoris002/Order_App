import uuid
from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dtos.table_dto import TableCreateDTO, TableReadDTO
from app.models.order_models import Table
from app.utils.db_utils import create_database_session
from app.daos.table_dao import TableDAO

router = APIRouter(prefix="/tables", tags=["tables"])

@router.post("/", response_model=TableReadDTO)
async def create_table(
    payload: TableCreateDTO,
    session: Annotated[AsyncSession, Depends(create_database_session)]
):
    new_table = Table(
        id=uuid.uuid4(),
        name=payload.name,
        location=payload.location,
        code=payload.code
    )
    return await TableDAO.create(session, new_table)

@router.get("/{table_id}", response_model=TableReadDTO)
async def get_table(
    table_id: uuid.UUID,
    session: Annotated[AsyncSession, Depends(create_database_session)]
):
    table = await TableDAO.get(session, table_id)
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    return table

@router.get("/", response_model=List[TableReadDTO])
async def list_tables(
    session: Annotated[AsyncSession, Depends(create_database_session)]
):
    return await TableDAO.list(session)
