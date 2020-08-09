# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page07.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets

from page08 import Ui_Form_8
from page09 import Ui_Form_9
from page11 import Ui_Form_11
from page12 import Ui_Form_12


class Ui_Form_7(object):
    def prev_window(self, prev):
        self.prev = prev

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 362)
        self.form = Form
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #self.pushButton = QtWidgets.QPushButton(Form)
        #self.pushButton.setGeometry(QtCore.QRect(180, 290, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        #self.pushButton.setFont(font)
        #self.pushButton.setObjectName("pushButton")
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
        self.label.setText(_translate("Form", "누가 마피아일까요???"))
        #self.pushButton.setText(_translate("Form", "사형 집행~"))

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
        isAlive = self.data[index]["alive"]

        if isAlive:
            if my_position == "마피아":
                self.page = Ui_Form_9() # 시민 승리
                self.form.hide()
            elif my_position == "시민":
                self.data = []
                with open('data.json', 'r') as outfile:
                    self.data = json.load(outfile)

                self.data[index]["alive"] = False

                with open('data.json', 'w') as f:
                    json.dump(self.data, f)

                aliveNum = 0

                for d in self.data:
                    if d["position"] == "시민":
                        if d["alive"] == True:
                            aliveNum += 1

                if aliveNum == 1: # 마피아 승리
                    self.page = Ui_Form_11()
                    self.form.hide()
                else: # 시민이 죽고 계속 진행
                    self.page = Ui_Form_8()
                    self.page.prev_window(self.prev)


            self.page_form = QtWidgets.QWidget()
            self.page.setupUi(self.page_form)
            self.page_form.show()
            self.form.hide()
        else:
            self.page12 = Ui_Form_12()
            self.page12_form = QtWidgets.QWidget()
            self.page12.setupUi(self.page12_form)
            self.page12_form.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_7()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
