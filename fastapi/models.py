from pydantic import BaseModel

class SummaryReq(BaseModel):
    text: str