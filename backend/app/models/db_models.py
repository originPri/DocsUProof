from sqlalchemy import Column, String, Text, DateTime, Enum as SQLEnum, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
import uuid

from app.core.database import Base

class DocumentStatus(enum.Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    COMPLETED = "completed"
    ERROR = "error"

class RiskLevel(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    documents = relationship("Document", back_populates="user", cascade="all, delete-orphan")
    conversations = relationship("Conversation", back_populates="user", cascade="all, delete-orphan")



class Document(Base):
    """Uploaded rental contract documents"""
    __tablename__ = "documents"
    
    id = Column(String, primary_key=True)
    filename = Column(String, nullable=False)
    state = Column(String, nullable=False)
    detected_state = Column(String, nullable=True)
    text = Column(Text, nullable=False)
    status = Column(SQLEnum(DocumentStatus), default=DocumentStatus.UPLOADED)
    error_message = Column(Text, nullable=True)
    
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)  # ADD THIS
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="documents")  # ADD THIS
    analysis = relationship("Analysis", back_populates="document", uselist=False, cascade="all, delete-orphan")
    chats = relationship("ChatHistory", back_populates="document", cascade="all, delete-orphan")
    conversations = relationship("Conversation", back_populates="document", cascade="all, delete-orphan")


class Analysis(Base):
    __tablename__ = "analysis"
    
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, ForeignKey("documents.id"), nullable=False)
    
    # Analysis results
    total_clauses = Column(Integer, default=0)
    illegal_clauses = Column(Integer, default=0)
    high_risk_clauses = Column(Integer, default=0)
    medium_risk_clauses = Column(Integer, default=0)
    risk_level = Column(SQLEnum(RiskLevel), default=RiskLevel.LOW)
    
    # Financial details
    rent_amount = Column(Integer, nullable=True)
    bond_amount = Column(Integer, nullable=True)
    
    # Full analysis JSON
    clauses = Column(JSONB, nullable=True)  # JSON string
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    document = relationship("Document", back_populates="analysis")


class Conversation(Base):
    """Conversation threads"""
    __tablename__ = "conversations"
    
    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    document_id = Column(String, ForeignKey("documents.id", ondelete="SET NULL"), nullable=True)
    title = Column(String, nullable=False, default="New Conversation")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="conversations")
    document = relationship("Document", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan")

class Message(Base):
    """Messages within conversations"""
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    conversation_id = Column(String, ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    conversation = relationship("Conversation", back_populates="messages")

class ChatHistory(Base):
    __tablename__ = "chat_history"
    
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, ForeignKey("documents.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    state = Column(String, nullable=False)
    laws_retrieved = Column(Integer, default=0)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    document = relationship("Document", back_populates="chats")