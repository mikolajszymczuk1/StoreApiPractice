from app.modules.store.application.services.store_service import StoreService
from app.modules.store.domain.repositories.i_store_repository import IStoreRepository
from app.modules.store.domain.services.i_store_service import IStoreService
from app.modules.store.infrastructure.repositories.store_repository import StoreRepository

# ====== Modules Initialization ======
# Simple implementation of Dependency Injection pattern
# In this version of project we operate with singletons

# ====== Repositories ======
storeRepository: IStoreRepository = StoreRepository()

# ====== Services ======
storeService: IStoreService = StoreService(storeRepository)
