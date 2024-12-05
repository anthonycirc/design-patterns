from abc import ABC, abstractmethod


class Interface(ABC):
    """
    Represents an abstract base class (ABC) interface that requires subclasses
    to implement the `execute` method. This class is designed to identify
    objects that share a common behavior or capability
    """

    def __init__(self):
        self._price = None

    @abstractmethod
    def calcul_total_price(self) -> float:
        raise NotImplementedError


class Box(Interface):
    """
    Represents a container that can hold objects implementing the Interface and
    provides functionality to manage these objects, calculate their total price,
    and count them
    """

    def __init__(self, price: float) -> None:
        super().__init__()
        self._price = price
        self._objects: list[Interface] = []

    def calcul_total_price(self) -> float:
        return sum(obj.calcul_total_price() for obj in self._objects) + self._price

    def add(self, obj: Interface) -> None:
        self._objects.append(obj)

    def remove(self, obj: Interface) -> None:
        self._objects.remove(obj)

    def count_objects(self) -> int:
        return len(self._objects)


class Toy(Interface):
    """
    Represents a toy product with a specified price.
    """

    def __init__(self, price: float, brand: str | None = None) -> None:
        super().__init__()
        self._price = price
        self._brand = brand

    def calcul_total_price(self) -> float:
        return self._price


class Drink(Interface):
    """
    Represents a beverage with a specific flavor and price
    """

    def __init__(self, price: float, flavor: str) -> None:
        super().__init__()
        self._price = price
        self.flavor = flavor

    def calcul_total_price(self) -> float:
        return self._price + 8
