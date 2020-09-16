# -*- coding: utf-8 -*-
from abc import ABC
from typing import List, Union
from .entity_key import EntityKey
from .entity_name import EntityName
from .key import Key


class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


@classproperty
def typed_entity_name(cls):
    return cls._entity_name


class Entity(ABC):

    _entity_key: EntityKey
    _entity_name: EntityName

    def __init__(self, key: Union[str, int, Key]):
        if type(key) != Key:
            key = Key(key)
        self._key = EntityKey(self.entity_name, key)

    @classproperty
    def entity_name(cls) -> EntityName:
        if cls._entity_name:
            if not isinstance(cls._entity_name, EntityName):
                cls._entity_name = EntityName(cls._entity_name)
        else:
            cls._entity_name = EntityName(str(cls))
        cls.entity_name = typed_entity_name
        return cls._entity_name

    @property
    def entity_key(self) -> EntityKey:
        return self._entity_key

    @property
    def key(self) -> Key:
        return self._entity_key.key
