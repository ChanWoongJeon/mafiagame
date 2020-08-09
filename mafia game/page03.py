# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page03.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets

from page04 import Ui_Form_4
from page05 import Ui_Form_5
from page06 import Ui_Form_6


class Ui_Form_3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 362)
        self.form = Form
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 290, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.nextButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 100, 411, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_2.clicked.connect(partial(self.check_position, 0))
        self.pushButton_3.clicked.connect(partial(self.check_position, 1))
        self.pushButton_4.clicked.connect(partial(self.check_position, 2))
        self.pushButton_5.clicked.connect(partial(self.check_position, 3))
        self.pushButton_6.clicked.connect(partial(self.check_position, 4))
        self.pushButton_7.clicked.connect(partial(self.check_position, 5))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "각자 자신의 이름을 눌러 역할 확인!"))
        self.pushButton.setText(_translate("Form", "첫째날 기기~"))

        self.data = []
        with open('data.json', 'r') as outfile:
            self.data = json.load(outfile)

        self.pushButton_2.setText(_translate("Form", self.data[0]["name"]))
        self.pushButton_3.setText(_translate("Form", self.data[1]["name"]))
        self.pushButton_4.setText(_translate("Form", self.data[2]["name"]))
        self.pushButton_5.setText(_translate("Form", self.data[3]["name"]))
        self.pushButton_6.setText(_translate("Form", self.data[4]["name"]))
        self.pushButton_7.setText(_translate("Form", self.data[5]["name"]))

    def check_position(self, index):
        # 새로운 창 띄우기
        my_position = self.data[index]["position"]
        if my_position == "마피아":
            self.page_5 = Ui_Form_5() # 마피아 Form
        elif my_position == "시민":
            self.page_5 = Ui_Form_4() # 시민 Form

        self.page_5_form = QtWidgets.QWidget()
        self.page_5.setupUi(self.page_5_form)
        self.page_5_form.show()

    def nextButton(self):
        self.page06 = Ui_Form_6()
        self.page06_form = QtWidgets.QWidget()
        self.page06.setupUi(self.page06_form)
        self.page06_form.show()
        self.form.hide()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
