# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1361, 713)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.output_box = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_box.sizePolicy().hasHeightForWidth())
        self.output_box.setSizePolicy(sizePolicy)
        self.output_box.setMinimumSize(QtCore.QSize(485, 0))
        self.output_box.setMaximumSize(QtCore.QSize(485, 16777215))
        self.output_box.setObjectName("output_box")
        self.formLayout = QtWidgets.QFormLayout(self.output_box)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.output_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.delta_mean_l = QtWidgets.QLabel(self.output_box)
        self.delta_mean_l.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.delta_mean_l.setObjectName("delta_mean_l")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.delta_mean_l)
        self.label_4 = QtWidgets.QLabel(self.output_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.k_mean_l = QtWidgets.QLabel(self.output_box)
        self.k_mean_l.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.k_mean_l.setObjectName("k_mean_l")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.k_mean_l)
        self.label_8 = QtWidgets.QLabel(self.output_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(150, 0))
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.ki_mean_l = QtWidgets.QLabel(self.output_box)
        self.ki_mean_l.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ki_mean_l.setObjectName("ki_mean_l")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ki_mean_l)
        self.label_9 = QtWidgets.QLabel(self.output_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(150, 0))
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.kob_l = QtWidgets.QLabel(self.output_box)
        self.kob_l.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.kob_l.setObjectName("kob_l")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.kob_l)
        self.line_2 = QtWidgets.QFrame(self.output_box)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.label_13 = QtWidgets.QLabel(self.output_box)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.output_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(150, 0))
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.d_t_l = QtWidgets.QLabel(self.output_box)
        self.d_t_l.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.d_t_l.setObjectName("d_t_l")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.d_t_l)
        self.gridLayout.addWidget(self.output_box, 0, 6, 15, 1)
        self.yi_sb = QtWidgets.QSpinBox(self.centralwidget)
        self.yi_sb.setMinimum(-5)
        self.yi_sb.setMaximum(-3)
        self.yi_sb.setProperty("value", -4)
        self.yi_sb.setObjectName("yi_sb")
        self.gridLayout.addWidget(self.yi_sb, 11, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 4, 15, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.zero_page = QtWidgets.QWidget()
        self.zero_page.setObjectName("zero_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.zero_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.zero_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.stackedWidget.addWidget(self.zero_page)
        self.graph_page = QtWidgets.QWidget()
        self.graph_page.setObjectName("graph_page")
        self.stackedWidget.addWidget(self.graph_page)
        self.gridLayout.addWidget(self.stackedWidget, 1, 5, 14, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.ro_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ro_le.sizePolicy().hasHeightForWidth())
        self.ro_le.setSizePolicy(sizePolicy)
        self.ro_le.setMaximumSize(QtCore.QSize(178, 22))
        self.ro_le.setObjectName("ro_le")
        self.gridLayout.addWidget(self.ro_le, 6, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 0, 1, 1)
        self.czh_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.czh_le.sizePolicy().hasHeightForWidth())
        self.czh_le.setSizePolicy(sizePolicy)
        self.czh_le.setMaximumSize(QtCore.QSize(178, 22))
        self.czh_le.setObjectName("czh_le")
        self.gridLayout.addWidget(self.czh_le, 8, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 7, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.c0_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c0_le.sizePolicy().hasHeightForWidth())
        self.c0_le.setSizePolicy(sizePolicy)
        self.c0_le.setMaximumSize(QtCore.QSize(178, 22))
        self.c0_le.setObjectName("c0_le")
        self.gridLayout.addWidget(self.c0_le, 4, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 9, 0, 1, 1)
        self.mu_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mu_le.sizePolicy().hasHeightForWidth())
        self.mu_le.setSizePolicy(sizePolicy)
        self.mu_le.setMaximumSize(QtCore.QSize(178, 22))
        self.mu_le.setToolTip("")
        self.mu_le.setStatusTip("")
        self.mu_le.setObjectName("mu_le")
        self.gridLayout.addWidget(self.mu_le, 5, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 8, 0, 1, 1)
        self.d_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_le.sizePolicy().hasHeightForWidth())
        self.d_le.setSizePolicy(sizePolicy)
        self.d_le.setMaximumSize(QtCore.QSize(178, 22))
        self.d_le.setObjectName("d_le")
        self.gridLayout.addWidget(self.d_le, 9, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 11, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 12, 0, 1, 1)
        self.yi_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yi_le.sizePolicy().hasHeightForWidth())
        self.yi_le.setSizePolicy(sizePolicy)
        self.yi_le.setMaximumSize(QtCore.QSize(178, 22))
        self.yi_le.setObjectName("yi_le")
        self.gridLayout.addWidget(self.yi_le, 11, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 10, 0, 1, 1)
        self.start_process_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_process_btn.sizePolicy().hasHeightForWidth())
        self.start_process_btn.setSizePolicy(sizePolicy)
        self.start_process_btn.setObjectName("start_process_btn")
        self.gridLayout.addWidget(self.start_process_btn, 14, 0, 1, 4)
        self.czh_sb = QtWidgets.QSpinBox(self.centralwidget)
        self.czh_sb.setMinimum(15)
        self.czh_sb.setMaximum(17)
        self.czh_sb.setProperty("value", 16)
        self.czh_sb.setObjectName("czh_sb")
        self.gridLayout.addWidget(self.czh_sb, 8, 3, 1, 1)
        self.mui_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mui_le.sizePolicy().hasHeightForWidth())
        self.mui_le.setSizePolicy(sizePolicy)
        self.mui_le.setMaximumSize(QtCore.QSize(178, 22))
        self.mui_le.setObjectName("mui_le")
        self.gridLayout.addWidget(self.mui_le, 10, 1, 1, 1)
        self.s_kr_le = QtWidgets.QLineEdit(self.centralwidget)
        self.s_kr_le.setMaximumSize(QtCore.QSize(178, 16777215))
        self.s_kr_le.setObjectName("s_kr_le")
        self.gridLayout.addWidget(self.s_kr_le, 12, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(398, 128, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 13, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 4)
        self.substance_type_cb = QtWidgets.QComboBox(self.centralwidget)
        self.substance_type_cb.setObjectName("substance_type_cb")
        self.substance_type_cb.addItem("")
        self.substance_type_cb.addItem("")
        self.substance_type_cb.addItem("")
        self.substance_type_cb.addItem("")
        self.substance_type_cb.addItem("")
        self.gridLayout.addWidget(self.substance_type_cb, 2, 0, 1, 4)
        self.c0_sb = QtWidgets.QSpinBox(self.centralwidget)
        self.c0_sb.setMinimum(10)
        self.c0_sb.setMaximum(15)
        self.c0_sb.setProperty("value", 12)
        self.c0_sb.setObjectName("c0_sb")
        self.gridLayout.addWidget(self.c0_sb, 4, 3, 1, 1)
        self.ct_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ct_le.sizePolicy().hasHeightForWidth())
        self.ct_le.setSizePolicy(sizePolicy)
        self.ct_le.setMaximumSize(QtCore.QSize(178, 22))
        self.ct_le.setObjectName("ct_le")
        self.gridLayout.addWidget(self.ct_le, 7, 1, 1, 1)
        self.ct_sb = QtWidgets.QSpinBox(self.centralwidget)
        self.ct_sb.setMinimum(15)
        self.ct_sb.setMaximum(17)
        self.ct_sb.setProperty("value", 16)
        self.ct_sb.setObjectName("ct_sb")
        self.gridLayout.addWidget(self.ct_sb, 7, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 11, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 7, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 4, 2, 1, 1)
        self.f_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_le.sizePolicy().hasHeightForWidth())
        self.f_le.setSizePolicy(sizePolicy)
        self.f_le.setMaximumSize(QtCore.QSize(178, 22))
        self.f_le.setObjectName("f_le")
        self.gridLayout.addWidget(self.f_le, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1361, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu_3)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.change_machine_setup_action = QtWidgets.QAction(MainWindow)
        self.change_machine_setup_action.setObjectName("change_machine_setup_action")
        self.set_fullscreen = QtWidgets.QAction(MainWindow)
        self.set_fullscreen.setObjectName("set_fullscreen")
        self.disable_fullscreen = QtWidgets.QAction(MainWindow)
        self.disable_fullscreen.setObjectName("disable_fullscreen")
        self.input_rules_action = QtWidgets.QAction(MainWindow)
        self.input_rules_action.setObjectName("input_rules_action")
        self.change_graph_settings_action = QtWidgets.QAction(MainWindow)
        self.change_graph_settings_action.setObjectName("change_graph_settings_action")
        self.change_graph_setup_action = QtWidgets.QAction(MainWindow)
        self.change_graph_setup_action.setObjectName("change_graph_setup_action")
        self.set_text_size_action = QtWidgets.QAction(MainWindow)
        self.set_text_size_action.setObjectName("set_text_size_action")
        self.enable_animation_act = QtWidgets.QAction(MainWindow)
        self.enable_animation_act.setObjectName("enable_animation_act")
        self.disable_animation_act = QtWidgets.QAction(MainWindow)
        self.disable_animation_act.setObjectName("disable_animation_act")
        self.actionahwdj = QtWidgets.QAction(MainWindow)
        self.actionahwdj.setCheckable(True)
        self.actionahwdj.setObjectName("actionahwdj")
        self.animation_enable_act = QtWidgets.QAction(MainWindow)
        self.animation_enable_act.setCheckable(True)
        self.animation_enable_act.setObjectName("animation_enable_act")
        self.graph_modality_act = QtWidgets.QAction(MainWindow)
        self.graph_modality_act.setCheckable(True)
        self.graph_modality_act.setObjectName("graph_modality_act")
        self.menu.addAction(self.about_action)
        self.menu.addAction(self.input_rules_action)
        self.menu_2.addAction(self.change_machine_setup_action)
        self.menu_2.addAction(self.animation_enable_act)
        self.menu_4.addAction(self.set_fullscreen)
        self.menu_4.addAction(self.disable_fullscreen)
        self.menu_3.addAction(self.menu_4.menuAction())
        self.menu_3.addAction(self.change_graph_setup_action)
        self.menu_3.addAction(self.set_text_size_action)
        self.menu_3.addAction(self.graph_modality_act)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.substance_type_cb, self.c0_le)
        MainWindow.setTabOrder(self.c0_le, self.mu_le)
        MainWindow.setTabOrder(self.mu_le, self.ro_le)
        MainWindow.setTabOrder(self.ro_le, self.ct_le)
        MainWindow.setTabOrder(self.ct_le, self.czh_le)
        MainWindow.setTabOrder(self.czh_le, self.d_le)
        MainWindow.setTabOrder(self.d_le, self.mui_le)
        MainWindow.setTabOrder(self.mui_le, self.yi_le)
        MainWindow.setTabOrder(self.yi_le, self.s_kr_le)
        MainWindow.setTabOrder(self.s_kr_le, self.start_process_btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.output_box.setTitle(_translate("MainWindow", "Выходные характеристики:"))
        self.label_3.setText(_translate("MainWindow", "Оценка толщины диффузного слоя (мм):"))
        self.delta_mean_l.setText(_translate("MainWindow", "Значение"))
        self.label_4.setText(_translate("MainWindow", "Эффективный коэффициент:"))
        self.k_mean_l.setText(_translate("MainWindow", "Значение"))
        self.label_8.setText(_translate("MainWindow", "Коэффициент испарения (только у летучих примесей):"))
        self.ki_mean_l.setText(_translate("MainWindow", "Значение"))
        self.label_9.setText(_translate("MainWindow", "Общий коэффициент распределения\n"
"(только у летучих примесей):"))
        self.kob_l.setText(_translate("MainWindow", "Значение"))
        self.label_13.setText(_translate("MainWindow", "Обратная задача (характеристики установки):"))
        self.label_14.setText(_translate("MainWindow", "Диаметр тигля (мм):"))
        self.d_t_l.setText(_translate("MainWindow", "Значение"))
        self.yi_sb.setStatusTip(_translate("MainWindow", "Разряд числа"))
        self.label.setText(_translate("MainWindow", "Тут будут ваши графики и выходные характеристики"))
        self.label_6.setText(_translate("MainWindow", "Скорость кристаллизации f (мм/мин):"))
        self.label_16.setText(_translate("MainWindow", "Динамическая вязкость (Н*с/м^2)"))
        self.czh_le.setStatusTip(_translate("MainWindow", "Принимает значения от 10^15 до 10^17"))
        self.label_7.setText(_translate("MainWindow", "Начальная концентрация\n"
"примеси Co (cм^-3):"))
        self.label_20.setText(_translate("MainWindow", "Концентрация примеси в твердом\n"
"состоянии (г/л)"))
        self.label_10.setText(_translate("MainWindow", "Плотность жидкости (кг/м^3)"))
        self.c0_le.setStatusTip(_translate("MainWindow", "Принимает значения от 10^10 до 10^15"))
        self.label_18.setText(_translate("MainWindow", "Изменение плотности основного\n"
"вещества (кг/м^3)"))
        self.label_19.setText(_translate("MainWindow", "Концентрация примеси в жидком\n"
"состоянии (г/л)"))
        self.label_17.setText(_translate("MainWindow", "Масса в долях (%)"))
        self.label_11.setText(_translate("MainWindow", "Площадь кристалла (м^2):"))
        self.yi_le.setStatusTip(_translate("MainWindow", "Должен принимать значения от 10^(-5) до 10^(-3)"))
        self.label_21.setText(_translate("MainWindow", "Молярная масса компонента (г/моль)"))
        self.start_process_btn.setToolTip(_translate("MainWindow", "Начать процесс моделирования"))
        self.start_process_btn.setStatusTip(_translate("MainWindow", "Начать процесс моделирования"))
        self.start_process_btn.setText(_translate("MainWindow", "Старт"))
        self.czh_sb.setStatusTip(_translate("MainWindow", "Разряд числа"))
        self.mui_le.setStatusTip(_translate("MainWindow", "Динамическая вязкость примеси, принимает значения от 0.001 до 0.1"))
        self.label_2.setText(_translate("MainWindow", "Введите параметры смеси:"))
        self.substance_type_cb.setItemText(0, _translate("MainWindow", "Выберите примесь"))
        self.substance_type_cb.setItemText(1, _translate("MainWindow", "B - Бром"))
        self.substance_type_cb.setItemText(2, _translate("MainWindow", "P - Фосфор (летучая)"))
        self.substance_type_cb.setItemText(3, _translate("MainWindow", "As - Мышьяк"))
        self.substance_type_cb.setItemText(4, _translate("MainWindow", "Sb - Сурьма (летучая)"))
        self.c0_sb.setStatusTip(_translate("MainWindow", "Разряд числа"))
        self.ct_le.setStatusTip(_translate("MainWindow", "Принимает значения от 10^15 до 10^17"))
        self.ct_sb.setStatusTip(_translate("MainWindow", "Разряд числа"))
        self.label_5.setText(_translate("MainWindow", "* 10 ^"))
        self.label_12.setText(_translate("MainWindow", "* 10 ^"))
        self.label_15.setText(_translate("MainWindow", "* 10 ^"))
        self.label_22.setText(_translate("MainWindow", "* 10 ^"))
        self.f_le.setStatusTip(_translate("MainWindow", "Скорость кристаллизации, принимает значения от 0 до 15 мм/мин"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.menu_2.setTitle(_translate("MainWindow", "Моделирование"))
        self.menu_3.setTitle(_translate("MainWindow", "Вид"))
        self.menu_4.setTitle(_translate("MainWindow", "Полноэкранный режим"))
        self.about_action.setText(_translate("MainWindow", "О программе"))
        self.change_machine_setup_action.setText(_translate("MainWindow", "Изменение параметров установки"))
        self.set_fullscreen.setText(_translate("MainWindow", "Включить"))
        self.disable_fullscreen.setText(_translate("MainWindow", "Выключить"))
        self.input_rules_action.setText(_translate("MainWindow", "Правила ввода"))
        self.change_graph_settings_action.setText(_translate("MainWindow", "Настройка графиков"))
        self.change_graph_setup_action.setText(_translate("MainWindow", "Настройка графиков"))
        self.set_text_size_action.setText(_translate("MainWindow", "Размер шрифта"))
        self.enable_animation_act.setText(_translate("MainWindow", "Включить"))
        self.disable_animation_act.setText(_translate("MainWindow", "Выключить"))
        self.actionahwdj.setText(_translate("MainWindow", "ahwdj"))
        self.animation_enable_act.setText(_translate("MainWindow", "Анимация"))
        self.graph_modality_act.setText(_translate("MainWindow", "Показывать графики в отдельном окне"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
