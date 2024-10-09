from abc import ABC, abstractmethod

from creational.abstract_factory.vehicle import Vehicle, Car, Truck, Scooter, Bus, \
    EngineEnum


class EngineFactory(ABC):

    def __init__(self):
        self._vehicles: list[Vehicle] = []

    def create_vehicle(self) -> None:
        self._vehicles = [
            self.create_car(),
            self.create_truck(),
            self.create_scooter(),
            self.create_bus()
        ]

    def get_vehicles(self) -> list[Vehicle]:
        return self._vehicles

    @abstractmethod
    def create_car(self) -> Vehicle:
        ...

    @abstractmethod
    def create_truck(self) -> Vehicle:
        ...

    @abstractmethod
    def create_scooter(self) -> Vehicle:
        ...

    @abstractmethod
    def create_bus(self) -> Vehicle:
        ...


class GasolineEngineFactory(EngineFactory):
    def create_car(self) -> Vehicle:
        return Car(engine=EngineEnum.GASOLINE)

    def create_truck(self) -> Vehicle:
        return Truck(engine=EngineEnum.GASOLINE)

    def create_scooter(self) -> Vehicle:
        return Scooter(engine=EngineEnum.GASOLINE)

    def create_bus(self) -> Vehicle:
        return Bus(engine=EngineEnum.GASOLINE)


class ElectricEngineFactory(EngineFactory):
    def create_car(self) -> Vehicle:
        return Car(engine=EngineEnum.ELECTRIC)

    def create_truck(self) -> Vehicle:
        return Truck(engine=EngineEnum.ELECTRIC)

    def create_scooter(self) -> Vehicle:
        return Scooter(engine=EngineEnum.ELECTRIC)

    def create_bus(self) -> Vehicle:
        return Bus(engine=EngineEnum.ELECTRIC)
