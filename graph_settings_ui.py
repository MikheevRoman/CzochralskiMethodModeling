# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy)
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.cancel_btn, 5, 2, 1, 1)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_btn.sizePolicy().hasHeightForWidth())
        self.ok_btn.setSizePolicy(sizePolicy)
        self.ok_btn.setObjectName("ok_btn")
        self.gridLayout.addWidget(self.ok_btn, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        self.pen_width_le = QtWidgets.QLineEdit(Dialog)
        self.pen_width_le.setObjectName("pen_width_le")
        self.gridLayout.addWidget(self.pen_width_le, 1, 1, 1, 2)
        self.set_pen_solor_btn = QtWidgets.QPushButton(Dialog)
        self.set_pen_solor_btn.setObjectName("set_pen_solor_btn")
        self.gridLayout.addWidget(self.set_pen_solor_btn, 2, 1, 1, 2)
        self.set_background_color_btn = QtWidgets.QPushButton(Dialog)
        self.set_background_color_btn.setObjectName("set_background_color_btn")
        self.gridLayout.addWidget(self.set_background_color_btn, 3, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройка графиков"))
        self.label.setText(_translate("Dialog", "Толщина пера:"))
        self.label_2.setText(_translate("Dialog", "Цвет пера:"))
        self.label_3.setText(_translate("Dialog", "Цвет фона:"))
        self.cancel_btn.setText(_translate("Dialog", "Отмена"))
        self.ok_btn.setText(_translate("Dialog", "Ок"))
        self.set_pen_solor_btn.setText(_translate("Dialog", "Выбрать"))
        self.set_background_color_btn.setText(_translate("Dialog", "Выбрать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())