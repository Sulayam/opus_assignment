from pydantic import BaseModel
from typing import List


class DocumentRequirementsRequest(BaseModel):
    vendor_id: str
    country: str


class DocumentRequirementsResponse(BaseModel):
    vendor_id: str
    country: str
    required_documents: List[str]

class DocumentRequirementsResponse(BaseModel):
    vendor_id: str
    country: str
    required_documents: List[str]
    document_count: int
