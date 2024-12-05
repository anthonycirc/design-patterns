from abc import ABC, abstractmethod

class Product(ABC):
    """
    Represents an abstract base class for a product with a description
    """
    def __init__(self, description: str | None = None):
        self._description = description

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError


class Toy(Product):
    """
    Represents a toy product with a description attribute
    """
    def __init__(self, description: str | None = None):
        super().__init__(description)

    def get_description(self) -> str:
        return self._description


class Decorator(Product):
    """
    Represents a decorator in a product design pattern, which allows
    additional functionality to be attached dynamically to a product
    object
    """
    def __init__(self, product: Product, description: str | None = None):
        super().__init__(description)
        self._product = product

    def get_description(self) -> str:
        return f'{self._product.get_description()} {self._description}'


class AddTextra(Decorator):
    """
    Provides additional text or description to a product by extending the
    functionality of the 'Decorator' base class
    """
    def __init__(self, product: Product, description: str | None = None):
        super().__init__(product, description)


class TransFormUpper(Decorator):
    """
    The TransFormUpper class is a decorator that modifies the behavior of a
    Product object by transforming its description to uppercase
    """
    def __init__(self, product: Product):
        super().__init__(product)

    def get_description(self) -> str:
        return self._product.get_description().upper()
