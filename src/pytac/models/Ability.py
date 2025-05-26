from pydantic import BaseModel, computed_field, model_validator
from typing import Optional, Union, Dict, Any
import json # for dev purposes only; replace with api call

class Ability(BaseModel):
    id: str
    level: Optional[Union[None, int]]=None
    tooltip: Optional[Union[None, str]]=None
    type: Optional[Union[None, str]]=None

    def supplement_info(self, other: "Ability") -> "Ability":
        m = self.model_dump(
            exclude_unset=True
        ) | other.model_dump(
            exclude_unset=True
        )
        return(Ability(**m))


