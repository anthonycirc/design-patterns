from creational.builder.builders import VehicleBuilder


class Director:
    @staticmethod
    def build_product(builder: VehicleBuilder ) -> None:
        builder.build_engine()
        builder.build_wheels()
        builder.build_chassis()
        builder.build_interior()
        builder.build_seats()