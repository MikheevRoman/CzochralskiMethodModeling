import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QVBoxLayout, QDialog
import calculation
import json


class GraphWidget(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графики")
        self.showMaximized()
        self.setMinimumSize(600, 400)
        layout = QVBoxLayout()
        self.setLayout(layout)

    def add_plot(self, x, y, title="", axis_x_title="", axis_y_title=""):
        new_layout = self.layout()
        plot_widget = pg.PlotWidget()
        plot_widget.setTitle(title, color=(0, 0, 0))
        styles = {'color': 'g', 'font-size': '16px'}
        plot_widget.setLabel('left', axis_y_title, **styles)
        plot_widget.setLabel('bottom', axis_x_title, **styles)
        plot_widget.setBackground(self.background_color)
        pen = pg.mkPen(color=self.pen_color, width=self.width)    # pen painter
        plot_widget.plot(x, y, pen=pen)
        new_layout.addWidget(plot_widget)
        self.setLayout(new_layout)

    def fill_first_graph(self, substance_type, mu, ro, w_kr):
        x0 = np.arange(start=0, stop=10000, step=1)
        y0 = np.empty(x0.size)
        for i in range(x0.size):
            y0[i] = calculation.diff_layer_thickness(substance_type, mu, ro, w_kr, x0[i])
        self.add_plot(x0, y0, "Распределение примеси по длине кристаллов", "Коэффициент распределения", "Длина кристалла")

    def fill_second_graph(self, k, c0):
        x0 = np.arange(start=0, stop=1, step=0.001)
        y0 = np.empty(x0.size)
        for i in range(x0.size):
            y0[i] = calculation.C_t(k, c0, x0[i])
        self.add_plot(x0, y0, "Зависимость толщины диффузного слоя от скорости вращения кристалла относительно тигля",
                      "Толщина диффузного слоя", "Скорость вращения кристалла")

    def data_collection(self):  # метод для считывания настроек графика из json

        # открытие файла json для чтения
        json_file_path = "graph_variables.json"
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        # считывание настроек графика из json
        self.background_color = tuple(data["background_color"])  # задний фон графиков
        self.pen_color = tuple(data["pen_color"])  # (цвет пера)
        self.width = data["pen_width"]  # (ширина пера)
