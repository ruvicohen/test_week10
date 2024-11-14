from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.psql_db import Base

class SuspiciousHostageContent(Base):
    __tablename__ = "suspicious_hostage_content"
    content_id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String)

    user_quote_id = Column(Integer, ForeignKey("user_quote.user_quote_id", ondelete="CASCADE"))

    user_quote = relationship("UserQuote", back_populates="sentences_hostage")