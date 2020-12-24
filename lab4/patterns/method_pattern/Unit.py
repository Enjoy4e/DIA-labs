from __future__ import annotations
from abc import ABC, abstractmethod


class Unit(ABC):

    @abstractmethod
    def __repr__(self):
        pass


class Elf(Unit):
    def __init__(self):
        self.__unit = "elf"

    def __repr__(self):
        return self.__unit


class Orc(Unit):
    def __init__(self):
        self.__unit = "orc"

    def __repr__(self):
        return self.__unit
