# -*- coding: utf-8 -*-

"""Basic Key Type"""

__author__ = "vodkar"

from typing import Union
from uuid import uuid4


class Key:

    _key: str

    def __init__(self, key: Union[str, int]):
        self._key = str(key)

    @classmethod
    def generate_key(cls):
        return cls(str(uuid4()))

    @property
    def key(self) -> str:
        return self._key

    def __int__(self) -> int:
        return int(self._key)

    def __str__(self):
        return self._key

    def __repr__(self):
        return "Key: {}".format(self._key)
