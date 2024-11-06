import logging
from abc import ABC

from creational.builder.vehicle import Car, Truck

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])


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
        logging.info("Building car engine")

    def build_wheels(self) -> None:
        self._car.wheels = "Car Wheels"
        logging.info("Build car wheels")

    def build_chassis(self) -> None:
        self._car.chassis = "Car Chassis"
        logging.info("Build car chassis")

    def build_interior(self) -> None:
        self._car.interior = "Car Interior"
        logging.info("Build car interior")

    def build_seats(self) -> None:
        self._car.seats = "Car Seats"
        logging.info("Build car seats")

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
        logging.info("Building truck engine")

    def build_wheels(self) -> None:
        self._truck.wheels = "Truck Wheels"
        logging.info("Build truck wheels")

    def build_chassis(self) -> None:
        self._truck.chassis = "Truck Chassis"
        logging.info("Build truck chassis")

    def build_interior(self) -> None:
        self._truck.interior = "Truck Interior"
        logging.info("Build truck interior")

    def build_seats(self) -> None:
        self._truck.seats = "Truck Seats"
        logging.info("Build truck seats")

    def get_product(self) -> Truck:
        product: Truck = self._truck
        self.reset()
        return product
