from __future__ import annotations

from typing import Any, Optional
from enum import Enum
from datetime import datetime
from dateutil.parser import isoparse
from .rank import Rank


class PlayerDetails:

    __slots__ = (
        'player_id',
        'name',
        'mkc_id',
        'country_code',
        'country_name',
        'switch_fc',
        'is_hidden',
        'season',
        'mmr',
        'max_mmr',
        'overall_rank',
        'events_played',
        'win_rate',
        'wins_last_ten',
        'losses_last_ten',
        'gain_loss_last_ten',
        'largest_gain',
        'largest_gain_table_id',
        'largest_loss',
        'largest_loss_table_id',
        'average_score',
        'average_last_ten',
        'partner_average',
        'mmr_changes',
        'name_history',
        'rank'
    )

    def __init__(
        self,
        player_id: int,
        name: str,
        mkc_id: int,
        is_hidden: bool,
        season: int,
        events_played: int,
        wins_last_ten: int,
        losses_last_ten: int,
        mmr_changes: list[PlayerDetails.MmrChange],
        name_history: list[PlayerDetails.NameChange],
        rank: str,
        country_code: Optional[str] = None,
        country_name: Optional[str] = None,
        switch_fc: Optional[str] = None,
        mmr: Optional[int] = None,
        max_mmr: Optional[int] = None,
        overall_rank: Optional[int] = None,
        win_rate: Optional[float] = None,
        gain_loss_last_ten: Optional[int] = None,
        largest_gain: Optional[int] = None,
        largest_gain_table_id: Optional[int] = None,
        largest_loss: Optional[int] = None,
        largest_loss_table_id: Optional[int] = None,
        average_score: Optional[float] = None,
        average_last_ten: Optional[float] = None,
        partner_average: Optional[float] = None,
    ) -> None:
        self.player_id: int = player_id
        self.name: str = name
        self.mkc_id: int = mkc_id
        self.country_code: Optional[str] = country_code
        self.country_name: Optional[str] = country_name
        self.switch_fc: Optional[str] = switch_fc
        self.is_hidden: bool = is_hidden
        self.season: int = season
        self.mmr: Optional[int] = mmr
        self.max_mmr: Optional[int] = max_mmr
        self.overall_rank: Optional[int] = overall_rank
        self.events_played: int = events_played
        self.win_rate: Optional[float] = win_rate
        self.wins_last_ten: int = wins_last_ten
        self.losses_last_ten: int = losses_last_ten
        self.gain_loss_last_ten: Optional[int] = gain_loss_last_ten
        self.largest_gain: Optional[int] = largest_gain
        self.largest_gain_table_id: Optional[int] = largest_gain_table_id
        self.largest_loss: Optional[int] = largest_loss
        self.largest_loss_table_id: Optional[int] = largest_loss_table_id
        self.average_score: Optional[float] = average_score
        self.average_last_ten: Optional[float] = average_last_ten
        self.partner_average: Optional[float] = partner_average
        self.mmr_changes: list[PlayerDetails.MmrChange] = mmr_changes
        self.name_history: list[PlayerDetails.NameChange] = name_history
        self.rank: str = rank

    @property
    def win_loss_last_ten(self) -> str:
        return f'{self.wins_last_ten} - {self.losses_last_ten}'

    @staticmethod
    def loads(data: dict[str, Any]) -> PlayerDetails:
        return PlayerDetails(
            player_id=data['playerId'],
            name=data['name'],
            mkc_id=data['mkcId'],
            country_code=data.get('countryCode'),
            country_name=data.get('countryName'),
            switch_fc=data.get('switchFc'),
            is_hidden=data['isHidden'],
            season=data['season'],
            mmr=data.get('mmr'),
            max_mmr=data.get('maxMmr'),
            overall_rank=data.get('overallRank'),
            events_played=data['eventsPlayed'],
            win_rate=data.get('winRate'),
            wins_last_ten=data['winsLastTen'],
            losses_last_ten=data['lossesLastTen'],
            gain_loss_last_ten=data.get('gainLossLastTen'),
            largest_gain=data.get('largestGain'),
            largest_gain_table_id=data.get('largestGainTableId'),
            largest_loss=data.get('largestLoss'),
            largest_loss_table_id=data.get('largestLossTableId'),
            average_score=data.get('averageScore'),
            average_last_ten=data.get('averageLastTen'),
            partner_average=data.get('partnerAverage'),
            mmr_changes=PlayerDetails.MmrChange.loads_list(data=data['mmrChanges']),
            name_history=PlayerDetails.NameChange.loads_list(data=data['nameHistory']),
            rank=Rank.from_name(data['rank'])
        )

    class MmrChange:

        __slots__ = (
            'change_id',
            'new_mmr',
            'mmr_delta',
            'reason',
            'time',
            'score',
            'partner_scores',
            'partner_ids',
            'rank',
            'tier',
            'num_teams'
        )

        def __init__(
            self,
            new_mmr: int,
            mmr_delta: int,
            reason: PlayerDetails.MmrChange.Reason,
            time: datetime,
            change_id: Optional[int] = None,
            score: Optional[int] = None,
            partner_scores: Optional[list[int]] = None,
            partner_ids: Optional[list[int]] = None,
            rank: Optional[int] = None,
            tier: Optional[str] = None,
            num_teams: Optional[int] = None
        ) -> None:
            self.change_id: Optional[int] = change_id
            self.new_mmr: int = new_mmr
            self.mmr_delta: int = mmr_delta
            self.reason: PlayerDetails.MmrChange.Reason = reason
            self.time: datetime = time
            self.score: Optional[int] = score
            self.partner_scores: Optional[list[int]] = partner_scores
            self.partner_ids: Optional[list[int]] = partner_ids
            self.rank: Optional[int] = rank
            self.tier: Optional[str] = tier
            self.num_teams: Optional[int] = num_teams

        @staticmethod
        def loads(data: dict[str, Any]) -> PlayerDetails.MmrChange:
            return PlayerDetails.MmrChange(
                change_id=data.get('changeId'),
                new_mmr=data['newMmr'],
                mmr_delta=data['mmrDelta'],
                reason=PlayerDetails.MmrChange.Reason(data['reason']),
                time=isoparse(data['time']),
                score=data.get('score'),
                partner_scores=data.get('partnerScores'),
                partner_ids=data.get('partnerIds'),
                rank=data.get('rank'),
                tier=data.get('tier'),
                num_teams=data.get('numTeams')
            )

        @classmethod
        def loads_list(cls, data: list[dict[str, Any]]) -> list[PlayerDetails.MmrChange]:
            return list(map(lambda m: cls.loads(data=m), data))

        class Reason(Enum):
            PLACEMENT = 'Placement'
            TABLE = 'Table'
            PENALTY = 'Penalty'
            STRIKE = 'Strike'
            BONUS = 'Bonus'
            TABLE_DELETE = 'TableDelete'
            PENALTY_DELETE = 'PenaltyDelete'
            STRIKE_DELETE = 'StrikeDelete'
            BONUS_DELETE = 'BonusDelete'

    class NameChange:

        __slots__ = (
            'name',
            'changed_on',
            'season'
        )

        def __init__(
            self,
            name: str,
            changed_on: datetime,
            season: int
        ) -> None:
            self.name: str = name
            self.changed_on: datetime = changed_on
            self.season: int = season

        @staticmethod
        def loads(data: dict[str, Any]) -> PlayerDetails.NameChange:
            return PlayerDetails.NameChange(
                name=data['name'],
                changed_on=isoparse(data['changedOn']),
                season=data['season']
            )

        @classmethod
        def loads_list(cls, data: list[dict[str, Any]]) -> PlayerDetails.NameChange:
            return list(map(lambda n: cls.loads(data=n), data))
