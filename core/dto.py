from dataclasses import dataclass, field
from typing import List
#todo
from django.db.models.fields import Field
@dataclass(frozen=True)
class PhotoDataclass:
    id: int
    image: str

@dataclass(frozen=True)
class ProductDataclass:
    id: int
    name: str
    description: str
    photos: List['ProductDataclass'] = field(default_factory=list)