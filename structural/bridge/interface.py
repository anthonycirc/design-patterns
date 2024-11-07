from abc import ABC

from structural.bridge.implementation import Car, SportCar, Engine


class AutoDriveCar(ABC):
    """
    Interface for Car with auto drive
    """

    def __init__(self, car: Car) -> None:
        self._car = car

    def toggle_start(self) -> None:
        """
        Toggle start/stop car
        :return: None
        """
        self._car.stop() if self._car.is_started() else self._car.start()

    def get_engine_infos(self) -> None:
        """
        Get engine infos
        :return: None
        """
        self._car.get_engine()


class AutoDriveClassicCar(AutoDriveCar):
    """
    Interface for ClassicCar with auto drive
    """
    ...


class AutoDriveSportCar(AutoDriveCar):
    """
    Interface for SportCar with auto drive
    """

    def toggle_sport_drive(self) -> None:
        """
        Activate sport drive
        :return: None
        """

        if not isinstance(self._car, SportCar):
            raise Exception("This feature is only available for SportCar")

        if not self._car.is_started():
            raise Exception("Car is not started")

        if self._car.get_engine() != Engine.GASOLINE:
            raise Exception("Sport drive is only available for gasoline engine")

        self._car.disabled_sport_drive() if self._car.sport_drive else self._car.enabled_sport_drive()

    def toggle_turbo(self) -> None:
        """
        Activate turbo
        :return: None
        """
        if not isinstance(self._car, SportCar):
            raise Exception("This feature is only available for SportCar")

        if not self._car.sport_drive:
            raise Exception("Turbo is only available in sport drive mode")

        self._car.disabled_turbo() if self._car.turbo else self._car.enabled_turbo()

    def toggle_nitro(self) -> None:
        """
        Activate nitro
        :return: None
        """
        if not isinstance(self._car, SportCar):
            raise Exception("This feature is only available for SportCar")

        if not self._car.sport_drive or self._car.turbo:
            raise Exception(
                "Nitro is only available in sport drive mode with turbo disabled")

        self._car.disabled_nitro() if self._car.nitro else self._car.enabled_nitro()
