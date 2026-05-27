from pydantic import BaseModel
from typing import List

class TicketSummary(BaseModel):

    summary: str

    business_impact: str

    priority: str

    root_cause: str

    recommended_actions: List[str]