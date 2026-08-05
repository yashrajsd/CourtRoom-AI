from sqlalchemy.ext.asyncio import create_async_engine
from app.core.settings import settings

# create_async_engine create an async engine every request can reuse it.
# With pre_ping connects automatically
# pool size = 10 database connection remain open
# if 10 are busy it will create temporarily 20 more
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)
