# -*- coding: utf-8 -*-
from __future__ import annotations

"""Entity name object"""

__author__ = "vodkar"


class EntityName:

    _name: str

    def __init__(self, name: str):
        if " " in name:
            raise ValueError("Can't use spaces in entity names")

        self._name = name

    def __eq__(self, rhs: object) -> bool:
        if isinstance(rhs, EntityName):
            return self._name == rhs._name
        if isinstance(rhs, str):
            return self._name == rhs
        raise ValueError("Can't compare {} with EntityName".format(type(rhs)))

    def __ne__(self, rhs: object) -> bool:
        return not self == rhs

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return "EntityName: {}".format(self._name)

    def __hash__(self):
        return hash(self._name)
