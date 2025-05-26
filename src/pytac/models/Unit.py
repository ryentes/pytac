from pydantic import BaseModel
from typing import Optional, Union, List
from pytac.models.Ability import Ability
from pytac.models.UnitItem import UnitItem

class Unit(BaseModel):
    id: str
    name: Optional[Union[None, str]]=None
    faction: Optional[Union[None, str]]=None
    grandAlliance: Optional[Union[None, str]]=None
    progressionIndex: int
    xp: int
    xpLevel: int
    rank: int
    abilities: List[Ability]
    upgrades: List
    items: List[UnitItem]
    shards: int
