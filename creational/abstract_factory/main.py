import logging

from creational.abstract_factory.factories import EngineFactory, GasolineEngineFactory, \
    ElectricEngineFactory
from creational.abstract_factory.vehicle import Vehicle

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])


def main():
    gasoline_factory: EngineFactory = GasolineEngineFactory()
    electric_factory: EngineFactory = ElectricEngineFactory()

    for factory in [gasoline_factory, electric_factory]:
        factory.create_vehicles()
        vehicles: list[Vehicle] = factory.vehicles

        for vehicle in vehicles:
            logging.info(
                f"{vehicle.__class__.__name__} with engine {vehicle.engine} requires license: {vehicle.license()}")


if __name__ == '__main__':
    main()
