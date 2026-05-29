from pydantic import BaseModel

class ThreatRequest(BaseModel):

    dur: float

    sbytes: float

    dbytes: float

    sttl: int

    dttl: int

    sport: int

    dsport: int

    service: int