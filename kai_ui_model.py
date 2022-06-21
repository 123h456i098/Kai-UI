from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    _name: str
    _v_option: bool
    _vg_option: bool
    _contains_sugar: bool
    _price: float
    _day: int

    @property
    def name(self) -> str:
        return self._name

    @property
    def v_option(self) -> bool:
        # Vegetarian friendly
        return self._v_option

    @property
    def vg_option(self) -> bool:
        # Vegan friendly
        return self._vg_option

    @property
    def contains_sugar(self) -> bool:
        return self._contains_sugar

    @property
    def price(self) -> float:
        return self._price

    @property
    def day(self) -> int:
        # The day the product is avaliable: 0 = No particular day,
        # 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday
        return self._day


@dataclass
class ProductCategory:
    """Stores the products of a category in a list."""

    _products: List[Product]
    _category: str

    @property
    def products(self) -> List[Product]:
        return self._products

    @property
    def category(self) -> str:
        return self._category


# Where to put order? model or controller as it is changing
# @dataclass
# class Order:
#     _products: List[Product]

PRODUCTS = [
    ProductCategory(
        [
            Product("Ham and Egg Sandwich", False, False, False, 3.50, 0),
            Product("Chicken Mayo Sandwich", False, False, False, 3.50, 0),
            Product("Egg Sandwich", True, False, False, 3.00, 0),
            Product("Beef Sandwich", False, False, False, 3.80, 0),
            Product("Salad Sandwich", True, True, False, 3.20, 0),
        ],
        "Sandwiches",
    ),
    ProductCategory(
        [
            Product("Chicken (3pc)", False, False, False, 4.50, 0),
            Product("Tuna (3pc)", False, False, False, 4.50, 0),
            Product("Avocado (3pc)", True, True, False, 4.80, 0),
            Product("Chicken Rice Bowl", False, False, False, 5.50, 0),
            Product("Vegetarian Rice Bowl", True, True, False, 5.50, 0),
        ],
        "Sushi",
    ),
    ProductCategory(
        [
            Product("Soda Can", True, True, True, 2.00, 0),
            Product("Aloe Vera Drink", True, False, True, 3.50, 0),
            Product("Chocolate Milk", False, False, True, 3.50, 0),
            Product("Water Bottle", True, True, False, 2.50, 0),
            Product("Instant Hot Chocolate", True, False, True, 1.50, 0),
        ],
        "Drinks",
    ),
    ProductCategory(
        [
            Product("Kale Moa", False, False, True, 6.00, 1),
            Product("Potjiekos", False, False, False, 6.00, 2),
            Product("Hangi", True, True, False, 6.00, 3),
            Product("Paneer Tikka Masala", True, False, True, 6.00, 4),
            Product("Chow Mein", True, True, False, 6.00, 5),
        ],
        "Special Items of the Day",
    ),
]
