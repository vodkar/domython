# -*- coding: utf-8 -*-

"""Value-object dython"""

__author__ = "boombarah"

from abc import ABC, abstractstaticmethod, abstractclassmethod
from enum import EnumMeta, Enum
from typing import Tuple


class ValueObject(ABC):
    pass


# region value object validator mixin


class ValidateResultMeta(EnumMeta):
    OK = "ok"

    def __new__(mcl, name, bases, nmspc):
        bases += (Enum,)
        return super(ValidateResultMeta, mcl).__new__(mcl, name, bases, nmspc)


class ValueObjectValidatorMixin:
    @abstractstaticmethod
    def is_valid(*args, **kwargs) -> ValidateResultMeta:
        """validate input for this value object and returns result

        Raises:
            NotImplementedError: abstract method

        Returns:
            ValidateResultMeta: enumeration result of validating
        """


# endregion

# region try parse
class ValueObjectTryParseMixin:
    """Mixin to add try_parse func with result to value object
        It's comfortable to use this with ValueObjectValidatorMixin

        For example:

        class Address(ValueObjectTryParseMixin, ValueObjectValidatorMixin):
            _street: str
            def __init__(self, street: str):
                self._street = street
            def is_valid(address: str):
                // some logic...
            def try_parse(cls, address):
                result = cls.is_valid(address)
                if result == AddressValidateResult.OK:
                    return (cls(address), result)
                return (None, result)


    Raises:
        NotImplementedError: raised when try_parse not implemented
    """

    @abstractclassmethod
    def try_parse(cls, *args, **kwargs) -> Tuple[ValueObject, ValidateResultMeta]:
        """Try to parse value from args, then returns result of parsing

        Raises:
            NotImplementedError: raised when not implemented

        Returns:
            Tuple[ValueObject, ValidateResultMeta]: new value object or None value if parsing is failed and enumerated result
        """

    def __init__(self) -> None:
        pass


# endregion