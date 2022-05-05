from __future__ import annotations

from typing import Any, Optional
import aiohttp

from .player import Player
from .player_details import PlayerDetails
from .player_list import PlayerList
from .leaderboard import Leaderboard
from .table_details import TableDetails
from .bonus import Bonus
from .penalty import Penalty


BASE_URL = 'https://www.mk8dx-lounge.com/api'


class LoungeAPIError(Exception):

    __slots__ = (
        'status',
        'messages'
    )

    def __init__(self, status: int, messages: list[str]) -> None:
        self.status: int = status
        self.messages: list[str] = messages


async def get(path: str, params: dict = {}) -> Optional[dict[str, Any]]:
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL + path, params=params) as response:
            if response.status != 200:
                if response.status == 404:
                    raise LoungeAPIError(404, ['Not Found'])
                if response.status == 400:
                    errors = response.json().get('errors', {})
                    raise LoungeAPIError(400, errors.values())
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


async def get_player_list(min_mmr=None, max_mmr=None, season=None) -> Optional[PlayerList]:
    params = {}
    if min_mmr is not None:
        params['minMmr'] = min_mmr
    if max_mmr is not None:
        params['maxMmr'] = max_mmr
    if season is not None:
        params['season'] = season
    data = await get(path='/player/list', params=params)
    if data is None:
        return None
    return PlayerList.loads(data=data)


async def get_leaderboard(
    season: int,
    skip: int = 0,
    page_size: int = 50,
    search=None,
    country=None,
    min_mmr=None,
    max_mmr=None,
    min_events_played=None,
    max_events_played=None
) -> Optional[Leaderboard]:
    params = {'season': season, 'skip': skip, 'pageSize': page_size}
    if search is not None:
        params['search'] = search
    if country is not None:
        params['country'] = country
    if min_mmr is not None:
        params['minMmr'] = min_mmr
    if max_mmr is not None:
        params['maxMmr'] = max_mmr
    if min_events_played is not None:
        params['minEventsPlayed'] = min_events_played
    if max_events_played is not None:
        params['maxEventsPlayed'] = max_events_played
    data = await get(path='/player/leaderboard', params=params)
    if data is None:
        return None
    return Leaderboard.loads(data=data)


async def get_table(table_id: int) -> Optional[TableDetails]:
    params = {'tableId': table_id}
    data = await get(path='/table', params=params)
    if data is None:
        return None
    return TableDetails.loads(data=data)


async def get_list(after=None, before=None, season=None) -> Optional[list[TableDetails]]:
    params = {}
    if after is not None:
        params['from'] = after
    if before is not None:
        params['to'] = before
    if season is not None:
        params['season'] = season
    data = await get(path='/table/list', params=params)
    if data is None:
        return None
    return TableDetails.loads_list(data=data)


async def get_table_unverified(season=None) -> Optional[list[TableDetails]]:
    params = {}
    if season is not None:
        params['season'] = season
    data = await get(path='/table/unverified', params=params)
    if data is None:
        return None
    return TableDetails.loads_list(data=data)


async def get_bonus(id: int) -> Optional[Bonus]:
    params = {'id': id}
    data = await get(path='/bonus', params=params)
    if data is None:
        return None
    return Bonus.loads(data=data)


async def get_bonus_list(
    name: str,
    season=None
) -> Optional[list[Bonus]]:
    params = {'name': name},
    if season is not None:
        params['season'] = season
    data = await get(path='/bonus/list', params=params)
    if data is None:
        return None
    return Bonus.loads_list(data=data)


async def get_penalty(id: int) -> Optional[Penalty]:
    params = {'id': id}
    data = await get(path='/penalty', params=params)
    if data is None:
        return None
    return Penalty.loads(data=data)


async def get_penalty_list(
    name: str,
    is_strike: Optional[bool] = None,
    after=None,
    include_deleted=False,
    season=None
) -> Optional[list[Penalty]]:
    params = {'name': name, 'includeDeleted': str(include_deleted)}
    if is_strike is not None:
        params['isStrike'] = is_strike
    if after is not None:
        params['from'] = after
    if season is not None:
        params['season'] = season
    data = await get(path='/penalty/list', params=params)
    if data is None:
        return None
    return Penalty.loads_list(data=data)
