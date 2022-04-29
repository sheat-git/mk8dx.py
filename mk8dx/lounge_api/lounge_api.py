from __future__ import annotations

from typing import Any, Optional
import aiohttp

from .details import PlayerDetails
from .player import Player


BASE_URL = 'https://www.mk8dx-lounge.com/api'


async def get(path: str, params: dict = {}) -> Optional[dict[str, Any]]:
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL + path, params=params) as response:
            if response.status != 200:
                return None
            return await response.json()


async def get_player(
    id=None,
    name=None,
    mkc_id=None,
    discord_id=None,
    season=None
) -> Optional[Player]:
    params = {}
    if id is not None:
        params['id'] = id
    elif name is not None:
        params['name'] = name
    elif mkc_id is not None:
        params['mkcId'] = mkc_id
    elif discord_id is not None:
        params['discordId'] = discord_id
    else:
        return None
    if season is not None:
        params['season'] = season
    data = await get(path='/player', params=params)
    if data is None:
        return None
    return Player.loads(data=data)


async def get_player_details(id=None, name=None, season=None) -> Optional[PlayerDetails]:
    params = {}
    if id is not None:
        params['id'] = id
    elif name is not None:
        params['name'] = name
    else:
        return None
    if season is not None:
        params['season'] = season
    data = await get(path='/player/details', params=params)
    if data is None:
        return None
    return PlayerDetails.loads(data=data)
