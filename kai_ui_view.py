from PySide6 import QtWidgets as qw
from kai_ui_view_food_selection import FoodSelection
from kai_ui_view_food_info import FoodInformation
from kai_ui_view_order import OrderScreen
from sys import exit


class View(qw.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Kai UI")
        self.setCentralWidget(qw.QWidget())
        self.setGeometry(300, 100, 400, 530)

        # Create the stacked layout
        self.screens = qw.QStackedLayout()
        self.screens.addWidget(FoodSelection())
        self.screens.addWidget(FoodInformation())
        self.screens.addWidget(OrderScreen())
        self.centralWidget().setLayout(self.screens)


def main():
    app = qw.QApplication([])
    win = View()
    win.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
