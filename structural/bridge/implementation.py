from abc import ABC
from enum import StrEnum, auto


class Engine(StrEnum):
    """
    Enumeration of engine types
    """
    ELECTRIC = auto()
    GASOLINE = auto()
    DIESEL = auto()
    HYBRID = auto()


class Car(ABC):
    """
    Concrete implementation of Car
    """

    def __init__(self, engine: Engine) -> None:
        self._start = False
        self._engine = engine

    def start(self) -> None:
        self._start = True
        print("Car is started")

    def stop(self) -> None:
        self._start = False
        print("Car is stopped")

    def is_started(self) -> bool:
        return self._start

    def get_engine(self) -> Engine:
        print(f"{self.__class__.__name__} engine is {self._engine}")
        return self._engine


class ClassicCar(Car):
    ...


class SportCar(Car):
    """
    Concrete implementation of SportCar
    """

    def __init__(self, engine: Engine = Engine.GASOLINE) -> None:
        super().__init__(engine)
        self._sport_drive = False
        self._turbo = False
        self._nitro = False

    def start(self) -> None:
        super().start()
        print("SportCar is started")

    def stop(self) -> None:
        super().stop()
        print("SportCar is stopped")

    def enabled_sport_drive(self) -> None:
        self._sport_drive = True
        print("Sport mode enabled")

    def disabled_sport_drive(self) -> None:
        self._sport_drive = False
        print("Sport mode disabled")

    def enabled_turbo(self) -> None:
        self._turbo = True
        print("Turbo enabled")

    def disabled_turbo(self) -> None:
        self._turbo = False
        print("Turbo disabled")

    def enabled_nitro(self) -> None:
        self._nitro = True
        print("Nitro activated")

    def disabled_nitro(self) -> None:
        self._nitro = False
        print("Nitro disabled")
