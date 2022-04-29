from __future__ import annotations

from typing import Optional


class Player:

    __slots__ = (
        'id',
        'name',
        'mkc_id',
        'discord_id',
        'country_code',
        'switch_fc',
        'is_hidden',
        'mmr',
        'max_mmr'
    )

    def __init__(
        self,
        id: int,
        name: str,
        mkc_id: int,
        discord_id: Optional[str] = None,
        country_code: Optional[str] = None,
        switch_fc: Optional[str] = None,
        is_hidden: bool = False,
        mmr: Optional[int] = None,
        max_mmr: Optional[int] = None
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.mkc_id: int = mkc_id
        self.discord_id: Optional[str] = discord_id
        self.country_code: Optional[str] = country_code
        self.switch_fc: Optional[str] = switch_fc
        self.is_hidden: bool = is_hidden
        self.mmr: Optional[int] = mmr
        self.max_mmr: Optional[int] = max_mmr

    @staticmethod
    def loads(data: dict) -> Player:
        return Player(
            id=data['id'],
            name=data['name'],
            mkc_id=data['mkcId'],
            discord_id=data.get('discordId'),
            country_code=data.get('countryCode'),
            switch_fc=data.get('switchFc'),
            is_hidden=data['isHidden'],
            mmr=data.get('mmr'),
            max_mmr=data.get('maxMmr')
        )
