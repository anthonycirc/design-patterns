from creational.prototype.prototypes import SportCar, BerlinCar


def main() -> None:
    sport_car: SportCar = SportCar(make="Ford", model="Mustang", year=2020)
    berlin_car: BerlinCar = BerlinCar(make="BMW", model="X5", year=2020, doors=5)

    print(sport_car.__dict__)
    print(berlin_car.infos)

    another_sport_car: SportCar = sport_car.clone()
    another_sport_car.make = "Chevrolet"
    another_berlin_car: BerlinCar = berlin_car.clone()
    another_berlin_car.make = "Mercedes"
    another_berlin_car.model = "GLC"

    print(another_sport_car.__dict__)
    print(another_berlin_car.infos)


if __name__ == "__main__":
    main()
