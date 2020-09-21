# -*- coding: utf-8 -*-

"""Repository interface for domython"""

__author__ = "Кирилл Гладких"

from .aggreagate_root import IAggregateRoot
from .entity import IEntity
from .key import Key
from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar("T", IAggregateRoot, IEntity)


class IRepository(Generic[T], ABC):
    @abstractmethod
    def find_by_key(self, key: Key) -> T:
        """Try to find object by key

        Args:
            key (Key): object key

        Returns:
            T: some object
        """
