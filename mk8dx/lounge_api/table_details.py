from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from dateutil.parser import isoparse


class TableDetails:

    __slots__ = (
        'id',
        'season',
        'created_on',
        'verified_on',
        'deleted_on',
        'num_teams',
        'url',
        'tier',
        'teams',
        'table_message_id',
        'update_message_id',
        'author_id'
    )

    def __init__(
        self,
        id: int,
        season: int,
        created_on: datetime,
        num_teams: int,
        url: str,
        tier: str,
        teams: list[TableDetails.Team],
        verified_on: Optional[datetime] = None,
        deleted_on: Optional[datetime] = None,
        table_message_id: Optional[str] = None,
        update_message_id: Optional[str] = None,
        author_id: Optional[str] = None
    ) -> None:
        self.id: int = id
        self.season: int = season
        self.created_on: datetime = created_on
        self.verified_on: Optional[datetime] = verified_on
        self.deleted_on: Optional[datetime] = deleted_on
        self.num_teams: int = num_teams
        self.url: str = url
        self.tier: str = tier
        self.teams: list[TableDetails.Team] = teams
        self.table_message_id: Optional[str] = table_message_id
        self.update_message_id: Optional[str] = update_message_id
        self.author_id: Optional[str] = author_id

    @staticmethod
    def loads(data: dict[str, Any]) -> TableDetails:
        verified_on_text = data.get('verifiedOn')
        deleted_on_text = data.get('deletedOn')
        if verified_on_text is None:
            verified_on = None
        else:
            verified_on = isoparse(verified_on_text)
        if deleted_on_text is None:
            deleted_on = None
        else:
            deleted_on = isoparse(deleted_on_text)
        return TableDetails(
            id=data['id'],
            season=data['season'],
            created_on=isoparse(data['createdOn']),
            verified_on=verified_on,
            deleted_on=deleted_on,
            num_teams=data['numTeams'],
            url=data['url'],
            tier=data['tier'],
            teams=TableDetails.Team.loads_list(data=data['teams']),
            table_message_id=data.get('tableMessageId'),
            update_message_id=data.get('updateMessageId'),
            author_id=data.get('authorId')
        )

    @classmethod
    def loads_list(cls, data: list[dict[str, Any]]) -> list[TableDetails]:
        return list(map(lambda t: cls.loads(t), data))

    class Team:

        __slots__ = (
            'rank',
            'scores'
        )

        def __init__(
            self,
            rank: int,
            scores: list[TableDetails.Score]
        ) -> None:
            self.rank: int = rank
            self.scores: list[TableDetails.Score] = scores

        @staticmethod
        def loads(data: dict[str, Any]) -> TableDetails.Team:
            return TableDetails.Team(
                rank=data['rank'],
                scores=TableDetails.Score.loads_list(data=data['scores'])
            )

        @classmethod
        def loads_list(cls, data: list[dict[str, Any]]) -> list[TableDetails.Team]:
            return list(map(lambda t: cls.loads(t), data))

    class Score:

        __slots__ = (
            'score',
            'multiplier',
            'prev_mmr',
            'new_mmr',
            'delta',
            'player_id',
            'player_name',
            'player_discord_id',
            'player_country_code'
        )

        def __init__(
            self,
            score: int,
            multiplier: float,
            player_id: int,
            player_name: str,
            prev_mmr: Optional[int] = None,
            new_mmr: Optional[int] = None,
            delta: Optional[int] = None,
            player_discord_id: Optional[str] = None,
            player_country_code: Optional[str] = None,
        ) -> None:
            self.score: int = score
            self.multiplier: float = multiplier
            self.prev_mmr: Optional[int] = prev_mmr
            self.new_mmr: Optional[int] = new_mmr
            self.delta: Optional[int] = delta
            self.player_id: int = player_id
            self.player_name: str = player_name
            self.player_discord_id: Optional[str] = player_discord_id
            self.player_country_code: Optional[str] = player_country_code

        @staticmethod
        def loads(data: dict[str, Any]) -> TableDetails.Score:
            return TableDetails.Score(
                score=data['score'],
                multiplier=data['multiplier'],
                prev_mmr=data.get('prevMmr'),
                new_mmr=data.get('newMmr'),
                delta=data.get('delta'),
                player_id=data['playerId'],
                player_name=data['playerName'],
                player_discord_id=data.get('playerDiscordId'),
                player_country_code=data.get('playerCountryCode')
            )

        @classmethod
        def loads_list(cls, data: list[dict[str, Any]]) -> list[TableDetails.Score]:
            return list(map(lambda s: cls.loads(s), data))
