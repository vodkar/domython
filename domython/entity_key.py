# -*- coding: utf-8 -*-
from __future__ import annotations

"""Unique entity key"""

__author__ = "vodkar"

from .entity_name import EntityName
from typing import Union
from .key import Key


class EntityKey:
    _entity_name: EntityName
    _key: Key

    # region constructors
    def __init__(self, entity_name: Union[str, EntityName], key: Union[int, str, Key]):
        if not isinstance(entity_name, EntityName):
            entity_name = EntityName(entity_name)
        self._entity_name = entity_name
        if type(key) != Key:
            key = Key(key)
        self._key = key

    @classmethod
    def from_str(cls, s: str) -> EntityKey:
        t_arr = s.split("-")
        if len(t_arr) != 2:
            raise ValueError(
                "EntityKey require following format <entity_name>-<entity_key>"
            )

        return cls(t_arr[0], t_arr[1])

    # endregion

    @property
    def key(self) -> Key:
        return self._key

    @property
    def entity_name(self):
        return self._entity_name

    # region overided
    def __eq__(self, rhs: object) -> bool:
        if isinstance(rhs, EntityKey):
            return self._entity_name == rhs._entity_name and self._key == rhs._key

        raise ValueError("Can't compare EntityKey and {} type".format(type(rhs)))

    def __ne__(self, rhs: object):
        return not self == rhs

    def __str__(self):
        return "{}-{}".format(self._entity_name, self._key)

    def __hash__(self):
        return hash(str(self._entity_name) + str(self._key))

    # endregion
