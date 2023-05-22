import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QDialog
from PyQt5.QtCore import Qt
import sys
import calculation


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
        plot_widget.setBackground((227, 227, 227))
        pen = pg.mkPen(color=(31, 17, 140), width=2)    # pen painter
        plot_widget.plot(x, y, pen=pen)
        new_layout.addWidget(plot_widget)
        self.setLayout(new_layout)

    def fill_first_graph(self, substance_type, mu, ro, w_kr):
        x0 = np.arange(start=0, stop=10000, step=1)
        y0 = np.empty(x0.size)
        for i in range(x0.size):
            y0[i] = calculation.diff_layer_thickness(substance_type, mu, ro, w_kr, x0[i])
        self.add_plot(x0, y0, "Распределение примеси по длине кристаллов", "Axis Y title", "x title")

    def fill_second_graph(self, k, c0):
        x0 = np.arange(start=0, stop=1, step=0.001)
        y0 = np.empty(x0.size)
        for i in range(x0.size):
            y0[i] = calculation.C_t(k, c0, x0[i])
        self.add_plot(x0, y0, "Зависимость толщины диффузного слоя от скорости вращения кристалла относительно тигля",
                      "Axis Y title", "x title")
