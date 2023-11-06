from PyQt5.QtWidgets import QDialog, QMessageBox
from machine_param_dlg_ui import Ui_Dialog
from main import MainWindow


class MachineParametersDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Параметры установки")
        if MainWindow.w_kr != 0.0 and MainWindow.w_t != 0.0:
            self.w_t_le.setText(str(MainWindow.w_t))
            self.w_kr_le.setText(str(MainWindow.w_kr))

        self.setup_settings_btn.clicked.connect(lambda: self.set_parameters())

    w_t = 0.0
    w_kr = 0.0

    def set_parameters(self):
        if self.w_t_le.text() == "" or self.w_kr_le.text() == "":
            QMessageBox.warning(self, "Ошибка", "Вы не ввели параметры установки")
            self.w_t_le.setText(str(self.w_t))
            self.w_kr_le.setText(str(self.w_kr))
            return

        self.w_t = float(self.w_t_le.text())
        self.w_kr = float(self.w_kr_le.text())
        MainWindow.w_t = self.w_t
        MainWindow.w_kr = self.w_kr
        self.close()
