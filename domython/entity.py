# -*- coding: utf-8 -*-
from abc import ABC
from typing import List, Union, TypeVar, Generic
from .entity_key import EntityKey
from .entity_name import EntityName
from .key import Key


class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


@classproperty
def typed_entity_name(cls):
    return cls._entity_name


class IEntity(ABC):

    _key: Key

    def __init__(self, key: Union[str, int, Key]):
        if not key:
            key = Key.generate_key()
        elif type(key) != Key:
            key = Key(str(key))
        self._key = key

    @property
    def key(self) -> Key:
        return self._key


class EntityBase(IEntity):
    pass


class NamedEntityMixin:
    """Mixin for naming entities

    Raises:
        NotImplementedError: raised with not initiliased _entity_name

    """

    _entity_name: EntityName

    @classproperty
    def entity_name(cls) -> EntityName:
        """Entity name for some use cases

        Raises:
            NotImplementedError: raised if entity name is not set

        Returns:
            EntityName: value object of entity name
        """
        if cls._entity_name:
            if not isinstance(cls._entity_name, EntityName):
                cls._entity_name = EntityName(cls._entity_name)
                cls.entity_name = typed_entity_name
            return cls._entity_name
        raise NotImplementedError()
