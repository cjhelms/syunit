from __future__ import annotations
import typing
import typing_extensions


class Unit:
    def __init__(self, value: float) -> None:
        self._value = value

    def __float__(self) -> float:
        return self._value


T = typing.TypeVar("T", bound=Unit)


class BinaryOperatableUnit(Unit):
    def __mul__(self, other: T) -> Multiply[typing_extensions.Self, T]:
        return Multiply[typing_extensions.Self, T](self._value * other._value)

    def __truediv__(self, other: T) -> Divide[typing_extensions.Self, T]:
        return Divide[typing_extensions.Self, T](self._value / other._value)


class Meters(BinaryOperatableUnit):
    ...


class Seconds(BinaryOperatableUnit):
    ...


T1 = typing.TypeVar("T1")
T2 = typing.TypeVar("T2")


class Multiply(typing.Generic[T1, T2], BinaryOperatableUnit):
    ...


class Divide(typing.Generic[T1, T2], BinaryOperatableUnit):
    ...
