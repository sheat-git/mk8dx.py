from __future__ import annotations

import string
from typing import Optional
from .race import Race
from .data import Track


class Mogi:

    __slots__ = (
        '__tags',
        '__format',
        '__races'
    )

    def __init__(self, tags: list[str], format: int) -> None:
        self.__tags: list[str] = tags
        self.__format: int = format
        self.__races: list[Race] = []

    @property
    def tags(self) -> list[str]:
        return self.__tags

    @property
    def format(self) -> int:
        return self.__format

    @property
    def races(self) -> list[Race]:
        return self.__races

    @property
    def sum_scores(self) -> list[int]:
        sum_scores: list[int] = [0]*(12//self.format)
        for race in self.races:
            if race.is_valid():
                for i, score in enumerate(race.scores):
                    sum_scores[i] += score
        return sum_scores

    def add_racedata_from_text(self, text: str, track: Optional[Track] = None) -> None:
        if (not self.races) or (self.races and self.races[-1].is_valid()):
            self.__races.append(Race(format=self.format, track=track))
        self.__races[-1].add_ranks_from_text(text=text)

    def set_track(self, track: Track, race_num: Optional[int] = None) -> bool:
        if not self.races:
            return False
        if race_num is None:
            self.__races[-1].track = track
            return True
        if len(self.races) < race_num:
            return False
        self.__races[race_num-1].track = track
        return True

    def back(self) -> Optional[Race]:
        if not self.races:
            return None
        return self.races.pop(-1)

    @classmethod
    def start(cls, tags: list[str] = [], format: Optional[int] = None) -> Mogi:
        if format is None:
            if len(tags) in {2, 3, 4, 6}:
                return cls(tags=tags, format=12//len(tags))
            if len(tags) in {1, 5}:
                return cls(tags=tags+['AA'], format=12//(len(tags)+1))
            if len(tags) == 0:
                return cls(tags=['AA', 'BB'], format=6)
            return cls(tags=tags[:6], format=2)
        if format not in {2, 3, 4, 6}:
            if format > 4:
                format = 6
            else:
                format = 2
        if len(tags) == 12//format:
            return cls(tags=tags, format=format)
        if len(tags) > 12//format:
            return cls(tags=tags[:12//format], format=format)
        return cls(
            tags=[string.ascii_uppercase[i]*2 for i in range(12//format-len(tags))]+tags,
            format=format
        )
