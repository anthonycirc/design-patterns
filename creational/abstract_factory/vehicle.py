from abc import ABC, abstractmethod
from enum import StrEnum, auto


class StatusEnum(StrEnum):
    """
    Enum for Status
    """
    STARTED = auto()
    STOPPED = auto()


class EngineEnum(StrEnum):
    """
    Enum for Fuel
    """
    GASOLINE = auto()
    ELECTRIC = auto()


class Vehicle(ABC):
    """
    Abstract class for Vehicle
    """

    def __init__(self):
        self._status: StatusEnum = StatusEnum.STOPPED
        self._engine: EngineEnum | None = None

    @property
    def status(self) -> str:
        return self._status

    @property
    def engine(self) -> EngineEnum | None:
        return self._engine

    def start(self) -> str:
        self._status = StatusEnum.STARTED
        return "Starting the vehicle"

    def stop(self) -> str:
        self._status = StatusEnum.STOPPED
        return "Stopping the vehicle"

    @abstractmethod
    def license(self) -> bool:
        ...


class Car(Vehicle):
    """
    Class for Car which inherits from Vehicle
    """

    def __init__(self, engine: EngineEnum):
        super().__init__()
        self._engine = engine

    def license(self) -> bool:
        return True


class Truck(Car):
    """
    Class for Truck which inherits from Vehicle
    """

    ...


class Bus(Car):
    """
    Class for Bus which inherits from Vehicle
    """
    ...


class Scooter(Vehicle):
    """
    Class for Scooter which inherits from Vehicle
    """

    def __init__(self, engine: EngineEnum):
        super().__init__()
        self._engine = engine

    def license(self) -> bool:
        return False
