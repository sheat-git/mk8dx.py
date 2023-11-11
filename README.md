# mk8dx

This library has Mogi, Race, Track, and Cup classes.
And mk8dx.lounge_api is fully lounge api wrapper.
(pond's fork will be a little bit different from main branch) //pond comment
## install

```bash
pip install mk8dx
```

## sample

### Track

```python
from mk8dx import Track

mks = Track.from_nick('マリカス') # => Track.MKS
dcl = Track.from_nick('dcl') # => Track.DCL

print(mks.abbr)         # MKS
print(mks.name)         # Mario Kart Stadium
print(mks.full_name)    # Mario Kart Stadium
print(dcl.abbr_ja)      # チーズ
print(dcl.name_ja)      # チーズランド
print(dcl.full_name_ja) # GBA チーズランド
```

### lounge_api

```python
from mk8dx import lounge_api

async def getMaxScore(name: str, season: int) -> Optional[int]:
    player = await lounge_api.get_player_details(name=name, season=season)
    max_score = -1
    for mmr_change in player.mmr_changes:
        if mmr_change.score is not None and max_score < mmr_change.score:
            max_score = mmr_change.score
    if max_score == -1:
        return None
    return max_score
```
