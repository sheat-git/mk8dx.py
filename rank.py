from __future__ import annotations

from typing import Optional


SCORES = (15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)


class Rank:

    __slots__ = (
        '__data'
    )

    def __init__(self, data: Optional[tuple[(bool,)*12]] = None) -> None:
        if data is None:
            self.__data: tuple[(bool,)*12] = (False,)*12
        else:
            self.__data: tuple[(bool,)*12] = data

    @property
    def data(self) -> tuple[(bool,)*12]:
        return self.__data

    @property
    def list(self) -> list[int]:
        return [i+1 for i in range(12) if self.data[i]]

    @property
    def score(self) -> int:
        s = 0
        for i in range(12):
            if self.data[i]:
                s += SCORES[i]
        return s

    @staticmethod
    def get_unfilled(ranks: list[Rank]) -> tuple[(bool,)*12]:
        def check_unfilled(i: int) -> bool:
            for rank in ranks:
                if rank.data[i]:
                    return False
            return True
        return tuple(check_unfilled(i) for i in range(12))

    @classmethod
    def from_list(cls, rank_list: list[int]) -> Rank:
        return cls(data = tuple(i+1 in rank_list for i in range(12)))
