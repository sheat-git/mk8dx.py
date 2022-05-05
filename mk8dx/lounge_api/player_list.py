from __future__ import annotations

from typing import Optional, Any


class PlayerList:

    __slots__ = (
        'players'
    )

    def __init__(self, players: list[PlayerList.Player]) -> None:
        self.players = players

    @staticmethod
    def loads(data: dict[str, Any]) -> PlayerList:
        return PlayerList(
            players=PlayerList.Player.loads_list(data=data)
        )

    class Player:

        __slots__ = (
            'name',
            'mkc_id',
            'mmr',
            'discord_id',
            'events_played'
        )

        def __init__(
            self,
            name: str,
            mkc_id: int,
            events_played: int,
            mmr: Optional[int],
            discord_id: Optional[str]
        ) -> None:
            self.name: str = name
            self.mkc_id: int = mkc_id
            self.mmr: Optional[int] = mmr
            self.discord_id: Optional[str] = discord_id
            self.events_played: int = events_played

        @staticmethod
        def loads(data: dict[str, Any]) -> PlayerList.Player:
            return PlayerList.Player(
                name=data['name'],
                mkc_id=data['mkcId'],
                mmr=data.get('mmr'),
                discord_id=data.get('discordId'),
                events_played=data['eventsPlayed']
            )

        @classmethod
        def loads_list(cls, data: list[dict[str, Any]]) -> list[PlayerList.Player]:
            return list(map(lambda p: cls.loads(p), data))
