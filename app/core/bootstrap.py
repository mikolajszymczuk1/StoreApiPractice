from fastapi import APIRouter, FastAPI

from app.core.container import Container
import app.modules.store.presentation.controllers.store_controller as store_controller
from app.modules.store.presentation.controllers.store_controller import router as store_router

# ====== Application Factory ======


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    container = Container()

    container.wire(modules=[store_controller])

    app = FastAPI()
    app.state.container = container

    api_router = APIRouter(prefix="/api")

    # Prepare all project controllers (routers)

    api_router.include_router(store_router)

    app.include_router(api_router)

    return app
