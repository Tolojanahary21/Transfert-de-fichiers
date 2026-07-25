from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_uuid = Column(String, unique=True, nullable=False, index=True)
    device_name = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    os = Column(String, nullable=False)
    status = Column(String, default="OFFLINE")
    last_seen = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    files = relationship("File", back_populates="device")

    sent_transfers = relationship(
        "Transfer",
        foreign_keys="Transfer.sender_device_id",
        back_populates="sender_device"
    )
    received_transfers = relationship(
        "Transfer",
        foreign_keys="Transfer.receiver_device_id",
        back_populates="receiver_device"
    )