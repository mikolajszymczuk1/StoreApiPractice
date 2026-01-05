from dependency_injector import containers, providers

from app.modules.store.application.services.store_service import StoreService
from app.modules.store.domain.repositories.i_store_repository import IStoreRepository
from app.modules.store.domain.services.i_store_service import IStoreService
from app.modules.store.infrastructure.repositories.store_repository import (
    StoreRepository,
)
from app.shared.domain.services.database.i_sqlite_database_service import ISQLiteDatabaseService
from app.shared.infrastructure.services.database.sqlite_database_service import (
    SQLiteDatabaseService,
)


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # ====== Database Services ======
    db: providers.Singleton[ISQLiteDatabaseService] = providers.Singleton(
        SQLiteDatabaseService,
        db_url=config.database.url,
        echo=config.database.echo.as_(bool),
    )

    # ====== Repositories ======
    store_repository: providers.Singleton[IStoreRepository] = providers.Singleton(
        StoreRepository,
        db=db,
    )

    # ====== Services ======
    store_service: providers.Factory[IStoreService] = providers.Factory(
        StoreService,
        store_repository=store_repository,
    )
