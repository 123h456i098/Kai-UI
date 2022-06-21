from PySide6 import QtWidgets as qw, QtCore as qc


class FoodInformation(qw.QWidget):
    def __init__(self):
        super().__init__()
        vbox = qw.QVBoxLayout()
        self.setLayout(vbox)
        self._top_bar(vbox)
        self._item_information_area(vbox)
        # Add item information
        self._item_image()
        self._item_name()
        self._item_details()

    def _item_details(self):
        self.price = qw.QLabel("Item price")
        self.v_option = qw.QLabel("Vegetarian option")
        self.vg_option = qw.QLabel("Vegan option")
        self.sugar = qw.QLabel("Contains sugar")
        self.vbox2.addSpacing(20)
        self.vbox2.addWidget(self.price)
        self.vbox2.addWidget(self.v_option)
        self.vbox2.addWidget(self.vg_option)
        self.vbox2.addWidget(self.sugar)
        self.vbox2.addStretch()

    def _item_name(self):
        self.product_name = qw.QLabel("Item name")
        self.vbox2.addWidget(self.product_name)
        self.product_name.setAlignment(qc.Qt.AlignCenter)

    def _item_image(self):
        self.product_image = qw.QLabel("Item image")
        self.vbox2.addStretch()
        self.vbox2.addWidget(self.product_image)

    def _item_information_area(self, vbox):
        hbox2 = qw.QHBoxLayout()
        self.vbox2 = qw.QVBoxLayout()
        vbox.addLayout(hbox2)
        hbox2.addStretch()
        vbox2_widget = qw.QWidget()
        vbox2_widget.setLayout(self.vbox2)
        vbox2_widget.setStyleSheet(
            "QLabel { font-size: 14px; font-family: consolas; }"
        )
        hbox2.addWidget(vbox2_widget)
        hbox2.addStretch()

    def _top_bar(self, vbox):
        top_widget = qw.QWidget()
        vbox.addWidget(top_widget)
        hbox = qw.QHBoxLayout()
        top_widget.setLayout(hbox)
        self.back_button = qw.QPushButton("Back")
        self.add_remove_button = qw.QPushButton()
        hbox.addWidget(self.back_button)
        hbox.addWidget(self.add_remove_button)
