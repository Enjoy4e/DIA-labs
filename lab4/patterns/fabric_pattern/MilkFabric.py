from __future__ import annotations
from abc import ABC, abstractmethod
from patterns.fabric_pattern.Product import MilkProduct, Cheese, SourCreame


class MilkFabric(ABC):

    @abstractmethod
    def create_milk_product(self) -> MilkProduct:
        pass

    def deliver(self, amount: int) -> list[MilkProduct]:
        products = []
        for i in range(amount):
            products.append(self.create_milk_product())
        print("Products with code name {} were successfully delivered".format(products[0]))
        return products


class CheeseFabric(MilkFabric):

    def create_milk_product(self) -> MilkProduct:
        return Cheese()


class SourCreameFabric(MilkFabric):

    def create_milk_product(self) -> MilkProduct:
        return SourCreame()

