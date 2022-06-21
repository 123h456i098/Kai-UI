from PySide6 import QtWidgets as qw


class FoodSelection(qw.QWidget):
    def __init__(self):
        super().__init__()
        vbox = qw.QVBoxLayout()
        self.setLayout(vbox)
        # Food display area
        foods = qw.QGroupBox("Foods")
        self.foods_layout = qw.QVBoxLayout()
        foods.setLayout(self.foods_layout)
        # Form layout
        self._create_form()
        vbox.addWidget(self.form_widget)
        vbox.addWidget(foods)
        # View order button
        self.view_order_button = qw.QPushButton("View Order")
        self.view_order_button.setFixedHeight(50)
        vbox.addStretch()
        vbox.addWidget(self.view_order_button)

    def _create_form(self):
        form = qw.QFormLayout()
        form.setSpacing(40)
        self.form_widget = qw.QWidget()
        self.form_widget.setLayout(form)
        # Day selection area
        self.day_select = qw.QComboBox()
        form.addRow("Day:", self.day_select)
        # Catergory selection area
        self.category_select = qw.QComboBox()
        form.addRow("Category:", self.category_select)
