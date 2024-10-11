from abc import ABC
from typing import Self


class CarPrototype(ABC):
    def __init__(self, make: str | None, model: str | None, year: int | None):
        self.type = "Car"
        self.make = make
        self.model = model
        self.year = year

    def clone(self) -> Self:
        ...


class SportCar(CarPrototype):
    def __init__(self, make: str | None, model: str | None, year: int | None):
        super().__init__(make, model, year)

    def clone(self) -> Self:
        return SportCar(self.make, self.model, self.year)


class BerlinCar(CarPrototype):
    def __init__(self, make: str | None, model: str | None, year: int | None,
                 doors: int | None):
        super().__init__(make, model, year)
        self.doors = doors

    @property
    def infos(self):
        return self.__dict__

    def clone(self) -> Self:
        return BerlinCar(self.make, self.model, self.year, self.doors)
