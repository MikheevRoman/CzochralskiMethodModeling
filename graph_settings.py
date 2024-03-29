import json
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QColorDialog
from graph_settings_ui import Ui_Dialog
from graph_viewer import GraphWidget


class GraphSettings(QDialog, Ui_Dialog):
    pen_color = QColor()
    background_color = QColor()
    axis_label_color = QColor()
    pen_width = 2

    background_color_rgb = (227, 227, 227)
    pen_color_rgb = (31, 17, 140)
    axis_label_color_rgb = (100, 100, 100)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pen_width_le.setText(str(self.pen_width))

        self.ok_btn.clicked.connect(lambda: self.accept_settings())
        self.cancel_btn.clicked.connect(lambda: self.close())
        self.set_pen_solor_btn.clicked.connect(lambda: self.set_pen_color())
        self.set_background_color_btn.clicked.connect(lambda: self.set_background_color())
        self.axis_label_color_btn.clicked.connect(lambda: self.set_axis_label_color())

    def set_pen_color(self):  # выбор цвета пера
        selected_color = QColorDialog.getColor(self.pen_color)

        if selected_color.isValid():
            self.pen_color_rgb = (selected_color.red(), selected_color.green(), selected_color.blue())
            print(self.pen_color_rgb)

    def set_background_color(self):  # выбор цвета фона
        selected_color = QColorDialog.getColor(self.background_color)

        if selected_color.isValid():
            self.background_color_rgb = (selected_color.red(), selected_color.green(), selected_color.blue())
            print(self.background_color_rgb)

    def set_axis_label_color(self):
        selected_color = QColorDialog.getColor(self.axis_label_color)
        if selected_color.isValid():
            self.axis_label_color_rgb = (selected_color.red(), selected_color.green(), selected_color.blue())

    def accept_settings(self):  # ок, (сохранить изменения)
        self.pen_width = int(self.pen_width_le.text())

        # словарь для записи новых настроек графика в json
        data = {
            "background_color": self.background_color_rgb,  # цвет заднего фона графиков
            "pen_color": self.pen_color_rgb,  # цвет пера
            "pen_width": self.pen_width,  # ширина пера
            "axis_label_color": self.axis_label_color_rgb
        }

        # запись настроек графика в json
        json_file_path = "graph_variables.json"
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file)

        self.close()
