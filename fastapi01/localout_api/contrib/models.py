from sqlalchemy import UUID
from uuid import uuid4
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgrest import UUID as PG_UUID


class AtletaMode():
    pass
class BassModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nolabell=False)