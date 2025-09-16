from fastapi import APIRouter
from app.api.order.order import router as order_router
router = APIRouter()

router.include_router(order_router)