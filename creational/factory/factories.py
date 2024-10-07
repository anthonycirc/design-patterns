from typing import Type

from creational.factory.animal import Animal
from creational.factory.exceptions import SubclassError


class AnimalFactory:
    """
    Factory class for creating animals
    """

    def __init__(self, animal_type: Type[Animal]) -> None:
        """
        Initialize the factory class with the given animal type
        """
        self.animal_type = animal_type

    def create_animal(self, name: str) -> Animal:
        """
        Create an animal object of the given type with the given name
        :param name: str
        :return: Animal object of the given type
        """

        if not issubclass(self.animal_type, Animal):
            raise SubclassError()
        return self.animal_type(name)
