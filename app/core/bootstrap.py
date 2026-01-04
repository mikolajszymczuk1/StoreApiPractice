from fastapi import APIRouter, FastAPI

from app.modules.store.presentation.controllers.store_controller import router as store_router

# ====== Application Factory ======


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    app = FastAPI()

    api_router = APIRouter(prefix="/api")

    # Prepare all project controllers (routers)

    api_router.include_router(store_router)

    app.include_router(api_router)

    return app
