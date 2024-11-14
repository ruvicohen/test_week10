from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.psql_db import Base


class SuspiciousExplosiveContent(Base):
    __tablename__ = "suspicious_explosive_content"
    content_id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String)

    user_quote_id = Column(Integer, ForeignKey("user_quote.user_quote_id"))\

    user_quote = relationship("UserQuote", back_populates="sentences_explosive")