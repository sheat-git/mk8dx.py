from __future__ import annotations

from typing import Optional

from ..lounge_api import get
from .player import Player
from .player_details import PlayerDetails
from .player_list import PlayerList
from .leaderboard import Leaderboard


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