from pydantic import BaseModel, Field
from typing import Literal


class Listing(BaseModel):
    id: str
    dealer_id: str
    status: Literal["draft", "pending_review", "published", "rejected"]
    missing_fields: list[str] = Field(default_factory=list)
