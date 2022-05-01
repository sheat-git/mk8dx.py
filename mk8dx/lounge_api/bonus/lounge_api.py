from __future__ import annotations

from typing import Optional

from ..lounge_api import get
from .bonus import Bonus


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
