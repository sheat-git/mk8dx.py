from __future__ import annotations

from typing import Optional

from ..lounge_api import get
from .penalty import Penalty


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