from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class for Animal
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def speak(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def eat(self) -> str:
        raise NotImplementedError


class Cat(Animal):
    """
    Class for Cat which inherits from Animal
    """

    def speak(self) -> str:
        return "Meow"

    def eat(self) -> str:
        return "Fish"


class Dog(Animal):
    """
    Class for Dog which inherits from Animal
    """

    def speak(self) -> str:
        return "Woof"

    def eat(self) -> str:
        return "Meat"
