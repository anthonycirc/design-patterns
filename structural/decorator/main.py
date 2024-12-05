from structural.decorator.decorator import Toy as ToyProduct
from structural.decorator.decorator import AddTextra as DecoratorExtraText
from structural.decorator.decorator import TransFormUpper as DecoratorUpper


def main():
    toy: ToyProduct = ToyProduct(description="Toy")
    print(toy.get_description())

    decorator_extra_text: DecoratorExtraText = DecoratorExtraText(product=toy,
                                                                  description="Extra text")
    print(decorator_extra_text.get_description())

    decorator_uppercase: DecoratorUpper = DecoratorUpper(product=decorator_extra_text)
    print(decorator_uppercase.get_description())


if __name__ == '__main__':
    main()
