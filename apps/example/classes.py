from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Example:
    string: str
    integer: int
    decimal: float 
    id: int = None
    date: datetime = field(default=datetime.now())

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id

