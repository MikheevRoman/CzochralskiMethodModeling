from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QInputDialog, QFontDialog, QVBoxLayout, QLabel
from mainwindow import Ui_MainWindow
from graph_viewer import GraphWidget
from machine_param_dlg import *
from graph_settings import *
from anime import playing_animation
import calculation
import sys
import pygame


# реализовать защиту от дурака и независимость ввода параметров
# сброс выведенных значений после повторного моделирования
class MainWindow(QMainWindow, Ui_MainWindow):
    # Dж - коэффициент диффузии в сплаве
    # параметры примеси
    substance_type = 0.0
    mu = 0.0
    ro = 0.0
    c_t = 0.0  # [1E+15, 1E+17]
    c_zh = 0.0  #
    f = 0.0  # [0, 15]
    c0 = 0.0  # [1E+10, 1E+15]
    s_kr = 0.0  # задается площадь кристалла
    # alpha = 0.0  # коэффициент испарения из жидкой фазы
    # machine setup
    w_kr = -1.0  # [0, 100]
    w_t = -1.0  # [0, 15]

    # SYSTEM SETTINGS
    animation_enabled = False
    graph_modality = False  # false - widget, true - window

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Моделирование выращивания кристаллов кремния методом Чохральского")

        self.start_process_btn.clicked.connect(lambda: self.start_process())
        self.set_fullscreen.triggered.connect(lambda: self.showFullScreen())
        self.disable_fullscreen.triggered.connect(lambda: self.showMaximized())
        self.change_machine_setup_action.triggered.connect(lambda: self.change_setup())
        self.change_graph_setup_action.triggered.connect(lambda: self.change_graph_settings())
        self.about_action.triggered.connect(lambda: QMessageBox.about(self, "О программе", "Разработана студентами "
                                                                                           "СПбГУТ"))
        self.graph_modality_act.triggered.connect(lambda: self.set_graph_modality())
        self.animation_enable_act.triggered.connect(lambda: self.set_animation())
        self.input_rules_action.triggered.connect(lambda: QMessageBox.about(self, "Правила ввода данных", "Для ввода "
                                                                                                          "чисел формата a*10^n используйте "
                                                                                                          "экспоненциальную форму записи числа: "
                                                                                                          "например, "
                                                                                                          "число 2.1*10^15 вводите как 2.1E+15, "
                                                                                                          "число 3.45*10^(-7) - как 3.45E-7"))
        self.set_text_size_action.triggered.connect(lambda: self.set_text_size())

    def set_graph_modality(self):
        self.graph_modality = not self.graph_modality

    def set_animation(self):
        self.animation_enabled = not self.animation_enabled

    # настройка шрифта
    def set_text_size(self):
        font = QFontDialog.getFont(self)[0]
        lst = [self.label_2, self.label_6, self.label_7, self.label_16, self.label_10, self.label_20, self.label_19,
               self.label_18, self.label_21, self.label_17, self.label_11, self.label_3, self.label_4, self.label_8,
               self.label_9, self.label_13, self.label_14, self.delta_mean_l, self.k_mean_l, self.ki_mean_l, self.kob_l,
               self.d_t_l, self.label]  # вносим в список надписи
        for label in lst:
            label.setFont(font)
        self.substance_type_cb.setFont(font)
        self.start_process_btn.setFont(font)
        self.output_box.setFont(font)

    def float_check(self):  # проверка
        superMegaString3000 = self.f_le.text() + self.c0_le.text() + self.mu_le.text() + self.ro_le.text() \
                              + self.ct_le.text() + self.czh_le.text() + self.d_le.text() + self.mui_le.text() \
                              + self.yi_le.text() + self.s_kr_le.text()
        for char in superMegaString3000:
            if not (char == '.' or char == '-' or char == 'E' or char == 'e' or char == '+' or char.isdigit()):
                return True
        return False

    def dumb_defence(self):
        if self.w_t == -1.0 or self.w_kr == -1.0:
            QMessageBox.warning(self, "Ошибка", "Вы не задали параметры установки, посмотрите \"Изменение "
                                                "параметров установки\" в разделе \"Моделирование\" на панели "
                                                "инструментов")
            return False
        if self.substance_type_cb.currentIndex() == 0:
            QMessageBox.warning(self, "Ошибка", "Вы не выбрали примесь")
            return False
        if self.float_check():
            QMessageBox.warning(self, "Ошибка", "Вы ввели число неправильно, посмотрите \"Правила ввода\""
                                                "в разделе \"Справка\"")
            return False
        if float(self.f_le.text()) < 0 or float(self.f_le.text()) > 15:
            QMessageBox.warning(self, "Ошибка", "Вы ввели недопустимую скорость кристаллизации f (мм/мин)")
            return False
        if float(self.c0_le.text()) < 1E+10 or float(self.c0_le.text()) > 1E+15:
            QMessageBox.warning(self, "Ошибка", "Вы ввели недопустимую начальную концентрацию примеси Co (cм^-3)")
            return False
        if float(self.ct_le.text()) < 1E+15 or float(self.ct_le.text()) > 1E+17:
            QMessageBox.warning(self, "Ошибка", "Вы ввели недопустимую концентрацию примеси в твердом состоянии (Cт)")
            return False
        if float(self.mui_le.text()) < 1E-3 or float(self.mui_le.text()) > 1E-1:
            QMessageBox.warning(self, "Ошибка", "Вы ввели недопустимую молярную массу приместого компонента (mu_i)")
            return False
        if float(self.yi_le.text()) < 0.1E-4 or float(self.yi_le.text()) > 10E-4:
            QMessageBox.warning(self, "Ошибка", "Вы ввели недопустимую молярную массу в долях (yi)")
            return False
        return True

    def set_parametrs_from_le(self):
        if self.f_le.text() == "":
            self.f_le.setText(str((0 + 15) / 2))
        if self.c0_le.text() == "":
            self.c0_le.setText("{:.0e}".format((1E+10 + 1E+15) / 2))
        if self.mu_le.text() == "":
            self.mu_le.setText(str(1))
        if self.ro_le.text() == "":
            self.ro_le.setText(str(1))
        if self.ct_le.text() == "":
            self.ct_le.setText(str((1E+15 + 1E+17) / 2))
        if self.czh_le.text() == "":
            self.czh_le.setText(str(1E+17))
        if self.d_le.text() == "":
            self.d_le.setText(str(1))
        if self.czh_le.text() == "":
            self.czh_le.setText(str(1))
        if self.mui_le.text() == "":
            self.mui_le.setText(str((1E-3 + 1E-1) / 2))
        if self.yi_le.text() == "":
            self.yi_le.setText(str((1E-5 + 1E-3) / 2))

    def show_about(self):
        QMessageBox.about(self, "О программе", "Разработана студентами СПбГУТ")

    def change_setup(self):
        dlg = MachineParametersDialog()
        dlg.exec()
        self.w_t = dlg.w_t
        self.w_kr = dlg.w_kr

    def change_graph_settings(self):
        dlg = GraphSettings()
        dlg.exec()

    def start_process(self):
        self.set_parametrs_from_le()
        # защита от дурака
        if not self.dumb_defence():
            return

        self.substance_type = self.substance_type_cb.currentIndex()
        self.mu = float(self.mu_le.text())
        self.ro = float(self.ro_le.text())
        self.c_t = float(self.ct_le.text())
        self.c_zh = float(self.czh_le.text())
        self.f = float(self.f_le.text())
        self.c0 = float(self.c0_le.text())

        delta = calculation.diff_layer_thickness(self.substance_type, self.mu, self.ro, self.w_kr, self.w_t)
        k = calculation.impurity_distribution_coef(self.c_t, self.c_zh, self.substance_type, self.f, delta)

        # ui output setup
        self.delta_mean_l.setText(str(delta.__round__(3)))
        self.k_mean_l.setText(str(k.__round__(3)))
        if self.substance_type == 2 or self.substance_type == 4:
            ki = calculation.k_i(self.substance_type)
            k_ob = calculation.k_ob(k, ki)
            self.ki_mean_l.setText(str(ki.__round__(3)))
            self.kob_l.setText(str(k_ob.__round__(3)))
            if self.s_kr_le.text() != "":
                self.s_kr = float(self.s_kr_le.text())
                D_t = calculation.D_t(self.s_kr, ki, k, self.f)
                self.d_t_l.setText(str(D_t.__round__(3)))
            elif self.s_kr_le.text() == "":
                pass
            else:
                QMessageBox.warning(self, "Ошибка", "Для решения обратной задачи должны быть введены все параметры")
                return
        else:
            self.ki_mean_l.setText("-")
            self.kob_l.setText("-")

        if self.s_kr_le.text() == "":
            self.d_t_l.setText("-")

        if self.animation_enabled:
            playing_animation(self.w_t, self.w_kr)  # проигрывание анимации

        graph = GraphWidget()
        graph.data_collection()
        graph.fill_first_graph(self.substance_type, self.mu, self.ro, self.w_kr)
        graph.fill_second_graph(k, self.c0)

        self.stackedWidget.addWidget(QtWidgets.QWidget())   # добавляем пустой виджет в стек-виджет
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)
        if self.graph_modality:  # если график в отдельном окне
            layout = QVBoxLayout()
            self.stackedWidget.currentWidget().setLayout(layout)
            graph.exec()
        else:   # если график в главном окне
            self.stackedWidget.currentWidget().setLayout(graph.return_graph_layout())
            graph.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
