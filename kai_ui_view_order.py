from PySide6 import QtWidgets as qw


class OrderScreen(qw.QWidget):
    def __init__(self):
        super().__init__()
        vbox = qw.QVBoxLayout()
        self.setLayout(vbox)
        # Top buttons
        buttons = qw.QWidget()
        hbox = qw.QHBoxLayout()
        buttons.setLayout(hbox)
        back = qw.QPushButton("Back")
        calc_total = qw.QPushButton("Total: $")
        hbox.addWidget(back)
        hbox.addWidget(calc_total)
        vbox.addWidget(buttons)
        # Foods area
        foods = qw.QGroupBox("Foods")
        foods_layout = qw.QVBoxLayout()
        foods.setLayout(foods_layout)
        vbox.addWidget(foods)
        # Submit button
        submit = qw.QPushButton("Submit Order to Canteen")
        submit.setFixedHeight(50)
        vbox.addStretch()
        vbox.addWidget(submit)
