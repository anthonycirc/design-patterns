from creational.builder.builders import CarBuilder, TruckBuilder
from creational.builder.director import Director


def main() -> None:
    car_builder = CarBuilder()
    truck_builder = TruckBuilder()

    print("Building Car:")
    Director.build_product(car_builder)
    car1 = car_builder.get_product()
    print(car1)

    print("\n")

    Director.build_product(car_builder)
    car2 = car_builder.get_product()
    print(car2)

    print("\n")

    print("Building Truck:")
    Director.build_product(truck_builder)
    truck_builder.get_product()
    print(truck_builder.get_product())


if __name__ == '__main__':
    main()
