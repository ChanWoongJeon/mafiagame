# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page06.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets

from page07 import Ui_Form_7


class Ui_Form_6(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(513, 348)
        self.form = Form
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 50, 331, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        # self.label.setFont(font)
        # self.label.setObjectName("label")
        # self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        #self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        #self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_4.setObjectName("label_4")
        #self.verticalLayout.addWidget(self.label_4)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.finish_buttton)
        # self.pushButton.setEnabled(False)

        # t = threading.Thread(target=self.timeout)
        # t.daemon = True
        # t.start()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #self.label.setText(_translate("Form", "n"))
        self.label_2.setText(_translate("Form", "아침이 밝았습니다!"))
        self.label_3.setText(_translate("Form", " 토론을 진행해주세요!"))
        #self.label_4.setText(_translate("Form", "카운트다운"))
        self.pushButton.setText(_translate("Form", "토론 다 끝났어~ 스킵!"))

    # def timeout(self):
    #     self.pushButton.setEnabled(False)
    #     time.sleep(3)
    #     self.pushButton.setEnabled(True)

    def finish_buttton(self):
        self.page07 = Ui_Form_7()
        self.page07_form = QtWidgets.QWidget()
        self.page07.prev_window(self.form)
        self.page07.setupUi(self.page07_form)
        self.page07_form.show()
        self.form.hide()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_6()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
