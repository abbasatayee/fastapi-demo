from fastapi import APIRouter

from .user_routes import router as user_router
from .auth_routes import router as auth_router
from .order_routes import router as order_router
from .customer_routes import router as customer_router

# collective router for /v1 prefix
router = APIRouter(prefix="/v1")
router.include_router(user_router)
router.include_router(auth_router)
router.include_router(order_router)
router.include_router(customer_router)