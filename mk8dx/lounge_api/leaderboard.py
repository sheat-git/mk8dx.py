from __future__ import annotations

from typing import Optional, Any
from .rank import Rank


class Leaderboard:

    __slots__ = (
        'total_players',
        'data'
    )

    def __init__(
        self,
        total_players: int,
        data: list[Leaderboard.Player]
    ) -> None:
        self.total_players: int = total_players
        self.data: list[Leaderboard.Player] = data

    @staticmethod
    def loads(data: dict[str, Any]) -> Leaderboard:
        return Leaderboard(
            total_players=data['totalPlayers'],
            data=Leaderboard.Player.loads_list(data=data.get('data'))
        )

    class Player:

        __slots__ = (
            'id',
            'overall_rank',
            'country_code',
            'name',
            'mmr',
            'max_mmr',
            'win_rate',
            'wins_last_ten',
            'losses_last_ten',
            'gain_loss_last_ten',
            'events_played',
            'largest_gain',
            'largest_loss',
            'mmr_rank',
            'max_mmr_rank'
        )

        def __init__(
            self,
            id: int,
            name: str,
            wins_last_ten: int,
            losses_last_ten: int,
            events_played: int,
            overall_rank: Optional[int] = None,
            country_code: Optional[str] = None,
            mmr: Optional[int] = None,
            max_mmr: Optional[int] = None,
            win_rate: Optional[float] = None,
            gain_loss_last_ten: Optional[int] = None,
            largest_gain: Optional[int] = None,
            largest_loss: Optional[int] = None,
            mmr_rank: Optional[Rank] = None,
            max_mmr_rank: Optional[Rank] = None
        ) -> None:
            self.id: int = id
            self.overall_rank: Optional[int] = overall_rank
            self.country_code: Optional[str] = country_code
            self.name: str = name
            self.mmr: Optional[int] = mmr
            self.max_mmr: Optional[int] = max_mmr
            self.win_rate: Optional[float] = win_rate
            self.wins_last_ten: int = wins_last_ten
            self.losses_last_ten: int = losses_last_ten
            self.gain_loss_last_ten: Optional[int] = gain_loss_last_ten
            self.events_played: int = events_played
            self.largest_gain: Optional[int] = largest_gain
            self.largest_loss: Optional[int] = largest_loss
            self.mmr_rank: Optional[Rank] = mmr_rank
            self.max_mmr_rank: Optional[Rank] = max_mmr_rank

        @staticmethod
        def laods(data: dict[str, Any]) -> Leaderboard.Player:
            mmr_rank_data = data.get('mmrRank')
            max_mmr_rank_data = data.get('maxMmrRank')
            if mmr_rank_data is None:
                mmr_rank = None
            else:
                mmr_rank = Rank.loads(data=mmr_rank_data)
            if max_mmr_rank_data is None:
                max_mmr_rank = None
            else:
                max_mmr_rank = Rank.loads(data=max_mmr_rank_data)
            return Leaderboard.Player(
                id=data['id'],
                overall_rank=data.get('overallRank'),
                country_code=data.get('countryCode'),
                name=data['name'],
                mmr=data.get('mmr'),
                max_mmr=data.get('maxMmr'),
                win_rate=data.get('winRate'),
                wins_last_ten=data['winsLastTen'],
                losses_last_ten=data['lossesLastTen'],
                gain_loss_last_ten=data.get('gainLossLastTen'),
                events_played=data['eventsPlayed'],
                largest_gain=data.get('largestGain'),
                largest_loss=data.get('largestLoss'),
                mmr_rank=mmr_rank,
                max_mmr_rank=max_mmr_rank,
            )

        @classmethod
        def loads_list(cls, data: list[dict[str, Any]]) -> list[Leaderboard.Player]:
            return list(map(lambda p: cls.laods(data=p), data))
