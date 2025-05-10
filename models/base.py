from sqlalchemy import Column, DateTime

from db.session import Base
from datetime import datetime
from settings.env import TIMEZONE

class TimeMixin(object):
    __abstract__ = True

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(TIMEZONE)
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(TIMEZONE),
        onupdate=lambda: datetime.now(TIMEZONE),
        nullable=True,
    )
