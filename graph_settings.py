from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QColorDialog
from graph_settings_ui import Ui_Dialog


class GraphSettings(QDialog, Ui_Dialog):
    pen_color = QColor()
    background_color = QColor()
    pen_width = 2

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pen_width_le.setText(str(self.pen_width))

        self.ok_btn.clicked.connect(lambda: self.accept_settings())
        self.cancel_btn.clicked.connect(lambda: self.close())
        self.set_pen_solor_btn.clicked.connect(lambda: self.set_pen_color())
        self.set_background_color_btn.clicked.connect(lambda: self.set_background_color())

    def set_pen_color(self):    # выбор цвета пера
        if QColor.isValid(QColorDialog.getColor(self.pen_color)):
            print(self.pen_color)

    def set_background_color(self):    # выбор цвета фона
        if QColor.isValid(QColorDialog.getColor(self.background_color)):
            print(self.background_color)

    def accept_settings(self):
        self.pen_width = int(self.pen_width_le.text())
        # MainGraphSettings.pen_color = self.pen_color
        # MainGraphSettings.pen_width = self.pen_width
        # MainGraphSettings.background_color = self.background_color
        self.close()
