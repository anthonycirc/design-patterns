from abc import ABC
from typing import Self

from creational.builder.vehicle import Car, Truck


class VehicleBuilder(ABC):

    def reset(self) -> None:
        ...

    def build_engine(self) -> None:
        ...

    def build_wheels(self) -> None:
        ...

    def build_chassis(self) -> None:
        ...

    def build_interior(self) -> None:
        ...

    def build_seats(self) -> None:
        ...


class CarBuilder(VehicleBuilder):
    _car: Car | None = None

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    def build_engine(self) -> None:
        self._car.engine = "Car Engine"
        print("Building car engine")

    def build_wheels(self) -> None:
        self._car.wheels = "Car Wheels"
        print("Build car wheels")

    def build_chassis(self) -> None:
        self._car.chassis = "Car Chassis"
        print("Build car chassis")

    def build_interior(self) -> None:
        self._car.interior = "Car Interior"
        print("Build car interior")

    def build_seats(self) -> None:
        self._car.seats = "Car Seats"
        print("Build car seats")

    def get_product(self) -> Car:
        product: Car = self._car
        self.reset()
        return product

class TruckBuilder(VehicleBuilder):
    _truck: Truck | None = None

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._truck = Truck()

    def build_engine(self) -> None:
        self._truck.engine = "Truck Engine"
        print("Building truck engine")

    def build_wheels(self) -> None:
        self._truck.wheels = "Truck Wheels"
        print("Build truck wheels")

    def build_chassis(self) -> None:
        self._truck.chassis = "Truck Chassis"
        print("Build truck chassis")

    def build_interior(self) -> None:
        self._truck.interior = "Truck Interior"
        print("Build truck interior")

    def build_seats(self) -> None:
        self._truck.seats = "Truck Seats"
        print("Build truck seats")

    def get_product(self) -> Truck:
        product: Truck = self._truck
        self.reset()
        return product
