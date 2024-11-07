from structural.bridge.implementation import ClassicCar, Car, Engine, SportCar
from structural.bridge.interface import AutoDriveSportCar, AutoDriveClassicCar


def main() -> None:
    # Classic car example
    classic_car: Car = ClassicCar(engine=Engine.DIESEL)
    drive_classic_car: AutoDriveClassicCar = AutoDriveClassicCar(classic_car)

    drive_classic_car.toggle_start()
    drive_classic_car.get_engine_infos()
    drive_classic_car.toggle_start()
    drive_classic_car.toggle_start()

    # Sport car example
    sport_car: Car = SportCar()
    drive_sport_car: AutoDriveSportCar = AutoDriveSportCar(sport_car)

    drive_sport_car.toggle_start()
    drive_sport_car.get_engine_infos()
    drive_sport_car.toggle_sport_drive()
    drive_sport_car.toggle_turbo()
    drive_sport_car.toggle_turbo()  # disabled turbo for nitro
    drive_sport_car.toggle_nitro()


if __name__ == "__main__":
    main()
