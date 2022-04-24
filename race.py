from __future__ import annotations

from typing import Optional
from data import Track
from rank import Rank


class Race:

    __slots__ = (
        '__ranks',
        'track'
    )

    def __init__(self, format: int, track: Optional[Track] = None) -> None:
        self.__ranks: list[Optional[Rank]] = [None] * (12//format)
        self.track: Optional[Track] = track

    @property
    def ranks(self) -> list[Optional[Rank]]:
        return self.__ranks

    @property
    def format(self) -> int:
        return 12 // len(self.__ranks)
