from PySide6 import QtWidgets as qw, QtCore as qc, QtGui as qg
from sys import exit
from typing import List
from dataclasses import dataclass
import os


@dataclass
class Product:
    _name: str
    _v_option: bool
    _vg_option: bool
    _contains_sugar: bool
    _price: float
    _day: int

    # region - Getters and no Setters
    @property
    def name(self) -> str:
        # Name of the product
        return self._name

    @property
    def v_option(self) -> bool:
        # If there is a vegetarian option avaliable
        return self._v_option

    @property
    def vg_option(self) -> bool:
        # If there is a vegan and gluten option avaliable
        return self._vg_option

    @property
    def contains_sugar(self) -> bool:
        # If the product contains sugar
        return self._contains_sugar

    @property
    def price(self) -> float:
        # The price of the product
        return self._price

    @property
    def day(self) -> int:
        # The day the product is avaliable: 0 = No particular day,
        # 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday
        return self._day

    # endregion

    @property
    def file_name(self) -> str:
        # Return the name of the file of the image of the product
        return self.name.lower().replace(" ", "_") + ".jpg"

    def load_photo(self, label: qw.QLabel):
        """Displays the photo in the label"""
        path = os.path.dirname(os.path.abspath(__file__))
        pixmap = qg.QPixmap(f"{path}/{self.file_name}")
        label.setPixmap(pixmap)


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


@dataclass
class Order:
    """List of products in the users order."""

    _products: List[Product]

    @property
    def products(self) -> List[Product]:
        return self._products

    @products.setter
    def products(self, new_products: List[Product]) -> None:
        # Checks that all the items in the list are of type Product
        if all(isinstance(item, Product) for item in new_products):
            self._products = new_products

    def add_product(self, product: Product) -> None:
        self.products = self.products + [product]

    def remove_product(self, product: Product) -> None:
        index = self.products.index(product)
        self.products = [
            self.products[i] for i in range(len(self.products)) if i != index
        ]

    def generate_total(self) -> float:
        return sum(item.price for item in self.products)

    def submit_order(self):
        # Generates the feedback text for the order with prices and names,
        # Contains error message if the order is empty
        text = ""
        if self.products:
            text += "Order Submitted|"
            for product in self.products:
                text += f"{product.name} - ${product.price}\n"
            text += "My services - $5\nAST - $2\nDonations - $1"
            total = self.generate_total() + 8.0
            text += f"\nTotal price (Excl. GST): ${total}"
            text += f"\nTotal price (Incl. GST): ${(total*1.15):.2f}"
            self.products = []
        else:
            text += "Error|"
            text += "No products in the order"
        return text


class KaiUI(qw.QMainWindow):
    """A class to create the main windows for the kai_ui.py program"""

    def __init__(self, parent=None):
        # Initializer
        super().__init__(parent)
        # Add all products in their catogories
        self.products = [
            ProductCategory(
                [
                    Product(
                        "Ham and Egg Sandwich", False, False, False, 3.50, 0
                    ),
                    Product(
                        "Chicken Mayo Sandwich", False, False, False, 3.50, 0
                    ),
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
                    Product(
                        "Vegetarian Rice Bowl", True, True, False, 5.50, 0
                    ),
                ],
                "Sushi",
            ),
            ProductCategory(
                [
                    Product("Soda Can", True, True, True, 2.00, 0),
                    Product("Aloe Vera Drink", True, False, True, 3.50, 0),
                    Product("Chocolate Milk", False, False, True, 3.50, 0),
                    Product("Water Bottle", True, True, False, 2.50, 0),
                    Product(
                        "Instant Hot Chocolate", True, False, True, 1.50, 0
                    ),
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
        self.setWindowTitle("Kai UI")
        self.setCentralWidget(qw.QWidget(self))
        self.setGeometry(300, 100, 400, 530)
        self.order = Order([])
        self.current_food = Product("None", False, False, False, 0, 0)
        # Creates the stacked layout with the base of the three screens needed
        self.screens = qw.QStackedLayout()
        self.screens.addWidget(self._select_foods_screen())
        self.screens.addWidget(self._food_info_screen())
        self.screens.addWidget(self._order_screen())
        self.centralWidget().setLayout(self.screens)

    def _select_foods_screen(self) -> qw.QWidget:
        window = qw.QWidget()
        vbox = qw.QVBoxLayout()
        window.setLayout(vbox)
        # Food display area
        foods = qw.QGroupBox("Foods")
        foods_layout = qw.QVBoxLayout()
        foods.setLayout(foods_layout)
        # Form layout
        form_widget = self._create_form(foods_layout)
        vbox.addWidget(form_widget)
        vbox.addWidget(foods)
        # View order button
        view_order_button = qw.QPushButton("View Order")
        view_order_button.clicked.connect(self._update_order_screen)
        return self._extracted(view_order_button, vbox, window)

    def _create_form(self, foods_layout):
        form = qw.QFormLayout()
        form.setSpacing(40)
        form_widget = qw.QWidget()
        form_widget.setLayout(form)
        # region - Day selection area
        day_select = qw.QComboBox()
        day_select.addItems(
            [
                "--No Selection--",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
            ]
        )
        day_select.currentIndexChanged.connect(
            lambda: self._display_foods(
                day_select.currentIndex(),
                category_select.currentIndex(),
                foods_layout,
            )
        )
        form.addRow("Day:", day_select)
        # endregion
        # region - Catergory selection area
        category_select = qw.QComboBox()
        category_select.addItems(
            ["--No Selection--"] + [item.category for item in self.products]
        )
        category_select.currentIndexChanged.connect(
            lambda: self._display_foods(
                day_select.currentIndex(),
                category_select.currentIndex(),
                foods_layout,
            )
        )
        form.addRow("Category:", category_select)
        # endregion
        return form_widget

    def _display_foods(
        self, day: int, category: int, layout: qw.QVBoxLayout
    ) -> None:
        self._clear_layout(layout)
        if day and category:
            for index, product in enumerate(
                self.products[category - 1].products
            ):
                if category == 4 and product.day == day or category != 4:
                    # If the category of the product is right or
                    # if the day is right on the special items
                    button = qw.QPushButton(product.name)
                    button.clicked.connect(
                        lambda sacrifice="", i=index: self._food_clicked(
                            i, category
                        )
                    )
                    button.setFixedHeight(50)
                    layout.addWidget(button)

    def _food_clicked(self, product_index: int, catergory_index: int) -> None:
        self.current_food = self.products[catergory_index - 1].products[
            product_index
        ]
        self._update_food_info(True)
        self.screens.setCurrentIndex(1)

    def _order_screen(self) -> qw.QWidget:
        window = qw.QWidget()
        vbox = qw.QVBoxLayout()
        window.setLayout(vbox)
        back = qw.QPushButton("Back")
        back.clicked.connect(lambda: self.screens.setCurrentIndex(0))
        buttons = qw.QWidget()
        hbox = qw.QHBoxLayout()
        buttons.setLayout(hbox)
        hbox.addWidget(back)
        self.calc_total = qw.QPushButton("Total: $")
        hbox.addWidget(self.calc_total)
        vbox.addWidget(buttons)
        foods = qw.QGroupBox("Foods")
        self._foods_layout = qw.QVBoxLayout()
        foods.setLayout(self._foods_layout)
        self._update_order_screen()
        vbox.addWidget(foods)
        submit = qw.QPushButton("Submit Order to Canteen")
        submit.clicked.connect(self._submit_order)
        return self._extracted(submit, vbox, window)

    def _order_food_clicked(self, product: Product) -> None:
        self.current_food = product
        self._update_food_info(False)
        self.screens.setCurrentIndex(1)

    def _extracted(
        self, button: qw.QPushButton, vbox: qw.QVBoxLayout, window: qw.QWidget
    ) -> qw.QWidget:
        button.setFixedHeight(50)
        vbox.addStretch()
        vbox.addWidget(button)
        return window

    def _food_info_screen(self) -> qw.QWidget:
        window = qw.QWidget()
        vbox = qw.QVBoxLayout()
        window.setLayout(vbox)
        top_widget = qw.QWidget()
        vbox.addWidget(top_widget)
        hbox = qw.QHBoxLayout()
        top_widget.setLayout(hbox)
        self.back = qw.QPushButton("Back")
        self.back.clicked.connect(lambda: print("Placeholder"))
        self.add_remove = qw.QPushButton()
        self.add_remove.clicked.connect(lambda: print("Placeholder"))
        hbox.addWidget(self.back)
        hbox.addWidget(self.add_remove)
        # Item placement area
        hbox2 = qw.QHBoxLayout()
        vbox2 = qw.QVBoxLayout()
        vbox.addLayout(hbox2)
        hbox2.addStretch()
        vbox2_widget = qw.QWidget()
        vbox2_widget.setLayout(vbox2)
        vbox2_widget.setStyleSheet(
            "QLabel { font-size: 14px; font-family: consolas; }"
        )
        hbox2.addWidget(vbox2_widget)
        hbox2.addStretch()

        # Item image
        self.product_image = qw.QLabel()
        vbox2.addStretch()
        vbox2.addWidget(self.product_image)
        # Item name
        self.product_name = qw.QLabel()
        vbox2.addWidget(self.product_name)
        self.product_name.setAlignment(qc.Qt.AlignCenter)
        # Item details
        self.price = qw.QLabel()
        self.v_option = qw.QLabel()
        self.vg_option = qw.QLabel()
        self.sugar = qw.QLabel()
        vbox2.addSpacing(20)
        vbox2.addWidget(self.price)
        vbox2.addWidget(self.v_option)
        vbox2.addWidget(self.vg_option)
        vbox2.addWidget(self.sugar)
        vbox2.addStretch()
        return window

    def _update_food_info(self, add_to_order: bool) -> None:
        # Button
        self.add_remove.setText(
            "Add to Order" if add_to_order else "Remove from Order"
        )
        self.add_remove.clicked.disconnect()
        self.add_remove.clicked.connect(
            lambda: self._added_to_order(self.current_food, add_to_order)
        )
        self.back.clicked.disconnect()
        if add_to_order:
            self.back.clicked.connect(lambda: self.screens.setCurrentIndex(0))
        else:
            self.back.clicked.connect(lambda: self.screens.setCurrentIndex(2))

        # Item image
        self.current_food.load_photo(self.product_image)
        # Item name
        self.product_name.setText(self.current_food.name)
        # Item details
        self.price.setText(
            f"Price:               ${str(self.current_food.price)}"
        )
        self.v_option.setText(
            f"Vegetarian option:   "
            f"{'✔️' if self.current_food.v_option else '❌'}"
        )
        self.vg_option.setText(
            f"Vegan option:        "
            f"{'✔️' if self.current_food.v_option else '❌'}"
        )
        self.sugar.setText(
            f"Contains sugar:      "
            f"{'✔️' if self.current_food.contains_sugar else '❌'}"
        )

    def _added_to_order(self, Product: Product, add_to_order: bool) -> None:
        if add_to_order:
            self.order.add_product(Product)
        else:
            try:
                self.order.remove_product(Product)
                self._update_order_screen()
            except ValueError:
                print("Product not in order")
        self.screens.setCurrentIndex(0 if add_to_order else 2)

    def _update_order_screen(self):
        self._clear_layout(self._foods_layout)
        for product in self.order.products:
            button = qw.QPushButton(product.name)
            button.clicked.connect(
                lambda sacrifice="", prct=product: self._order_food_clicked(
                    prct
                )
            )
            button.setFixedHeight(50)
            self._foods_layout.addWidget(button)
        self.calc_total.setText(f"Total: ${str(self.order.generate_total())}")
        self.screens.setCurrentIndex(2)

    def _submit_order(self) -> None:
        text = self.order.submit_order().split("|")
        qw.QMessageBox(
            qw.QMessageBox.Icon.Information, text[0], text[1]
        ).exec()
        self._update_order_screen()
        self.screens.setCurrentIndex(0)

    def _clear_layout(self, layout: qw.QBoxLayout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())


def main():
    app = qw.QApplication([])
    win = KaiUI()
    win.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
