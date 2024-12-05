from structural.composite.interface import Box as CompositeBox
from structural.composite.interface import Toy as CompositeToy
from structural.composite.interface import Drink as CompositeDrink


def main():
    box: CompositeBox = CompositeBox(price=8.0)
    toy: CompositeToy = CompositeToy(price=1.0, brand="Test")
    drink: CompositeDrink = CompositeDrink(price=8.0, flavor="strawberry")

    box.add(toy)
    box.add(drink)
    print(box.count_objects())
    print(box.calcul_total_price())

    box.remove(toy)
    print(box.count_objects())
    print(box.calcul_total_price())

    print(drink.calcul_total_price())

    other_box = CompositeBox(price=10.0)
    other_box.add(toy)
    box.add(other_box)

    print(box.calcul_total_price())


if __name__ == '__main__':
    main()
