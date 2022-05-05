from __future__ import annotations

from typing import Any, Optional
from datetime import datetime
from dateutil.parser import isoparse


class Penalty:

    __slots__ = (
        'id',
        'season',
        'awarded_on',
        'is_strike',
        'prev_mmr',
        'new_mmr',
        'amount',
        'deleted_on',
        'player_id',
        'player_name'
    )

    def __init__(
        self,
        id: int,
        season: int,
        awarded_on: datetime,
        is_strike: bool,
        prev_mmr: int,
        new_mmr: int,
        amount: int,
        player_id: int,
        player_name: str,
        deleted_on: Optional[datetime] = None
    ) -> None:
        self.id: int = id
        self.season: int = season
        self.awarded_on: datetime = awarded_on
        self.is_strike: bool = is_strike
        self.prev_mmr: int = prev_mmr
        self.new_mmr: int = new_mmr
        self.amount: int = amount
        self.deleted_on: Optional[datetime] = deleted_on
        self.player_id: int = player_id
        self.player_name: str = player_name

    @staticmethod
    def loads(data: dict[str, Any]) -> Penalty:
        deleted_on_text = data.get('deletedOn')
        if deleted_on_text is None:
            deleted_on = None
        else:
            deleted_on = isoparse(deleted_on_text)
        return Penalty(
            id=data['id'],
            season=data['season'],
            awarded_on=isoparse(data['awardedOn']),
            is_strike=data['isStrike'],
            prev_mmr=data['prevMmr'],
            new_mmr=data['newMmr'],
            amount=data['amount'],
            deleted_on=deleted_on,
            player_id=data['playerId'],
            player_name=data['playerName']
        )

    @classmethod
    def loads_list(cls, data: list[dict[str, Any]]) -> list[Penalty]:
        return list(map(lambda p: cls.loads(p), data))
