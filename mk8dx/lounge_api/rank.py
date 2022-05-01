from __future__ import annotations, division

from enum import Enum
from typing import Optional, Union


class Rank:

    __slots__ = (
        'division',
        'level'
    )

    def __init__(
        self,
        division: Rank.Division,
        level: Optional[int] = None
    ) -> None:
        self.division: Rank.Division = division
        self.level: Optional[int] = level

    @property
    def name(self) -> str:
        if self.level is None:
            return self.division.value
        return f'{self.division.value} {self.level}'

    @staticmethod
    def loads(data: dict[str, Union[str, int]]) -> Rank:
        return Rank(
            division=Rank.Division(data['division']),
            level=data.get('level')
        )
    
    @staticmethod
    def from_name(name: str) -> Optional[Rank]:
        if ' ' in name:
            division, level = name.split(' ', maxsplit=1)
            if not level.isdecimal():
                return None
            return Rank(division=Rank.Division(division), level=int(level))
        return Rank(division=Rank.Division(name))
    
    def __str__(self) -> str:
        return self.name
    
    class Division(Enum):
        GRANDMASTER = 'Grandmaster'
        MASTER = 'Master'
        DIAMOND = 'Diamond'
        SAPPHIRE = 'Sapphire'
        PLATINUM = 'Platinum'
        GOLD = 'Gold'
        SILVER = 'Silver'
        BRONZE = 'Bronze'
        IRON = 'Iron'
        PLACEMENT = 'Placement'
        UNKNOWN = 'Unknown'