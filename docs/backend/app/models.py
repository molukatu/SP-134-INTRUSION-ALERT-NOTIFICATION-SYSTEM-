from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="Viewer")  # Admin, Analyst, Viewer
    created_at = Column(DateTime, default=datetime.utcnow)

class Flow(Base):
    __tablename__ = "flows"
    id = Column(Integer, primary_key=True)
    src_ip = Column(String, nullable=False)
    dst_ip = Column(String, nullable=False)
    src_port = Column(Integer)
    dst_port = Column(Integer)
    protocol = Column(String)
    packets = Column(Integer)
    bytes = Column(Integer)
    duration = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    alerts = relationship("Alert", back_populates="flow")

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    flow_id = Column(Integer, ForeignKey("flows.id"))
    type = Column(String, nullable=False)  # Port Scan, Brute Force, etc
    severity = Column(String, nullable=False)  # Low, Medium, High, Critical
    confidence = Column(Float, default=0.0)
    status = Column(String, default="New")  # New, Investigating, Confirmed, False Positive, Resolved
    created_at = Column(DateTime, default=datetime.utcnow)
    flow = relationship("Flow", back_populates="alerts")
    notifications = relationship("Notification", back_populates="alert")

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True)
    alert_id = Column(Integer, ForeignKey("alerts.id"))
    channel = Column(String, nullable=False)  # email / sms
    recipient = Column(String, nullable=False)
    status = Column(String, default="sent")
    sent_at = Column(DateTime, default=datetime.utcnow)
    alert = relationship("Alert", back_populates="notifications")
