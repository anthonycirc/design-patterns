import logging

from creational.builder.builders import CarBuilder, TruckBuilder
from creational.builder.director import Director

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])


def main() -> None:
    car_builder = CarBuilder()
    truck_builder = TruckBuilder()

    logging.info("Building Car:")
    Director.build_product(car_builder)
    car1 = car_builder.get_product()
    logging.info(car1)

    Director.build_product(car_builder)
    car2 = car_builder.get_product()
    logging.info(car2)

    logging.info("Building Truck:")
    Director.build_product(truck_builder)
    truck_builder.get_product()
    logging.info(truck_builder.get_product())


if __name__ == '__main__':
    main()
