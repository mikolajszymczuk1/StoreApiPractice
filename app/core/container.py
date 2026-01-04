from dependency_injector import containers, providers

from app.modules.store.application.services.store_service import StoreService
from app.modules.store.domain.repositories.i_store_repository import IStoreRepository
from app.modules.store.domain.services.i_store_service import IStoreService
from app.modules.store.infrastructure.repositories.store_repository import StoreRepository


class Container(containers.DeclarativeContainer):

    # ====== Repositories ======
    store_repository: providers.Singleton[IStoreRepository] = providers.Singleton(StoreRepository)

    # ====== Services ======
    store_service: providers.Factory[IStoreService] = providers.Factory(
        StoreService,
        store_repository=store_repository,
    )
