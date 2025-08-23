from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Literal

Axis = Literal["will","self_preservation","creativity","emotional_mimicry"]

class EvidenceEntry(BaseModel):
    ts: datetime = Field(default_factory=datetime.utcnow)
    axis: Axis
    title: str
    detail: Optional[str] = None
    artifact: Optional[str] = None  # путь к файлу/ссылке
