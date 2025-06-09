from pydantic import BaseModel
from typing import Optional

class ThreatModel(BaseModel):
    cve_id: str
    description: str
    published: str
    modified: str
    cvss_score: Optional[float]
    cvss_severity: Optional[str]
    cpe: Optional[list]
    cwe: Optional[str]
    source: str
    kev: Optional[bool]
