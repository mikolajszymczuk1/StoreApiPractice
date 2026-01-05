from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import APIRouter, FastAPI

from app.core.container import Container
from app.modules.store.presentation.controllers.store_controller import router as store_router
from app.shared.domain.services.database.i_sqlite_database_service import ISQLiteDatabaseService

# ====== Application Factory ======


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan context manager to handle startup and shutdown events.
    """

    DATABASE_PATH: Path = Path(__file__).parent.parent / "db" / "store_api.db"
    DATABASE_URL: str = f"sqlite+aiosqlite:///{DATABASE_PATH}"

    # Initialize the dependency injection container
    container = Container()
    container.config.database.url.from_value(DATABASE_URL)
    container.config.database.echo.from_value(True)
    container.wire(packages=["app.modules"])

    app.state.container = container

    db: ISQLiteDatabaseService = container.db()

    try:
        yield
    finally:
        await db.dispose()


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    # Create FastAPI application instance
    app = FastAPI(lifespan=lifespan)

    # Prepare all project controllers (routers)
    api_router = APIRouter(prefix="/api")
    api_router.include_router(store_router)
    app.include_router(api_router)

    return app
