from pydantic import BaseModel
from typing import Optional, Union

class  UnitItem(BaseModel):
    slotId: str
    level: int
    id: str
    name: Optional[Union[None, str]]=None
    rarity: Optional[Union[None, str]]=None