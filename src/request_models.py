from pydantic import BaseModel
from datetime import timedelta, date
from enum import IntEnum
class StopRequest(BaseModel):
    lat: str
    lon: str
    count: int 