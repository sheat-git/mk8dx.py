from __future__ import annotations

from typing import Optional

from ..lounge_api import get
from .table_details import TableDetails


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
