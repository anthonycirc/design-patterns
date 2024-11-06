import logging

from creational.factory.animal import Cat, Dog, Animal
from creational.factory.factories import AnimalFactory

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])


def main():
    # """
    # >>> try:
    # ...     AnimalFactory(str).create_animal("Test")
    # ... except SubclassError as e:
    # ...     print(e)
    # The provided class is not a subclass of the expected class
    # """

    for animal_type in (Cat, Dog):
        animal: Animal = AnimalFactory(animal_type).create_animal(animal_type.__name__)
        logging.info(f"{animal.name} speaks {animal.speak()} and eats {animal.eat()}")


if __name__ == '__main__':
    main()
