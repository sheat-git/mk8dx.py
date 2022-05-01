from __future__ import annotations

from typing import Any, Optional
import aiohttp


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
