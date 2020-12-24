from __future__ import annotations
from abc import ABC, abstractmethod
from patterns.method_pattern.Unit import Elf, Orc


class BaseAI(ABC):
    """Base class"""

    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def gather_army(self):
        pass

    def attack(self, target: BaseAI):
        """default method"""
        return "Attacking {}".format(target)

    def turn(self, target: BaseAI):
        print(self.build_structures())
        print(self.gather_army())
        print(self.attack(target))


class ElfBaseAI(BaseAI):


    def __init__(self, money):
        self.__money = money
        self.__unit = Elf()
        self.__building_cost = 500
        self.built_structures = 0
        self.army = []
        self.__unit_cost = 200

    def build_structures(self):
        amount = int((self.__money/2) / self.__building_cost)
        self.built_structures = amount
        return "{} structures were built".format(self.built_structures)

    def gather_army(self):
        amount = int((self.__money/2)/self.__unit_cost)
        for i in range(amount):
            self.army.append(Elf())
        return "{} elves were recruited".format(len(self.army))

    def __repr__(self):
        return "ElfBase"


class OrcBaseAI(BaseAI):


    def __init__(self, money):
        self.__money = money
        self.__unit = Orc()
        self.__building_cost = 300
        self.built_structures = 0
        self.army = []
        self.__unit_cost = 100

    def build_structures(self):
        amount = int((self.__money / 3) / self.__building_cost)
        self.built_structures = amount
        return "{} structures were built".format(self.built_structures)

    def gather_army(self):
        amount = int((self.__money * 2 / 3) / self.__unit_cost)
        for i in range(amount):
            self.army.append(Elf())
        return "{} orcs were recruited".format(len(self.army))

    def __repr__(self):
        return "OrcBase"





