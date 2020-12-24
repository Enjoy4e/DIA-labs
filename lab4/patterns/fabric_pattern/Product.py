from __future__ import annotations
from abc import ABC, abstractmethod


class MilkProduct(ABC):

    @abstractmethod
    def __repr__(self) -> str:
        pass


class Cheese(MilkProduct):

    def __repr__(self) -> str:
        return "Cheese"


class SourCreame(MilkProduct):

    def __repr__(self) -> str:
        return "SourCreame"