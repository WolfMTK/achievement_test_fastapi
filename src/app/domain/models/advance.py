from dataclasses import dataclass

from .advance_id import AdvanceId


@dataclass
class Advances:
    id: AdvanceId
    name: str
    number_points: str
    description: str
