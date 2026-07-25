from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base


class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)

    sender_device_id = Column(
        Integer,
        ForeignKey("devices.id"),
        nullable=False
    )

    receiver_device_id = Column(
        Integer,
        ForeignKey("devices.id"),
        nullable=False
    )

    file_id = Column(
        Integer,
        ForeignKey("files.id"),
        nullable=False
    )

    status = Column(
        String,
        default="PENDING",
        nullable=False
    )

    progress = Column(
        Float,
        default=0
    )

    transfer_speed = Column(
        Float,
        nullable=True
    )

    started_at = Column(
        DateTime,
        nullable=True
    )

    completed_at = Column(
        DateTime,
        nullable=True
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    sender_device = relationship(
        "Device",
        foreign_keys=[sender_device_id],
        back_populates="sent_transfers"
    )
    receiver_device = relationship(
        "Device",
        foreign_keys=[receiver_device_id],
        back_populates="received_transfers"
    )
    file = relationship("File", back_populates="transfers")