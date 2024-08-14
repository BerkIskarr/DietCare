from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(452, 280)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QFrame#frame{\n"
"    background-color: rgba(242,242,242,1.000);\n"
"    border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel#label{\n"
"    font: 87 16pt \"Arial Black\";\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(55, 1, 132), stop:1 rgb(109, 7, 234));\n"
"    border-top-right-radius:10px;\n"
"    border-top-left-radius:10px;\n"
"    color:rgba(255,255,255,200);\n"
"}\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        self.close_button = QtWidgets.QPushButton(self.frame)
        self.close_button.setGeometry(QtCore.QRect(410, 10, 25, 25))
        self.close_button.setMinimumSize(QtCore.QSize(25, 25))
        self.close_button.setMaximumSize(QtCore.QSize(25, 25))
        self.close_button.setStyleSheet("QPushButton#close_button{\n"
"    background-color:rgb(255, 10, 2);\n"
"    color::rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#close_button:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#close_button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}\n"
"")
        self.close_button.setObjectName("close_button")
        self.send_btn = QtWidgets.QPushButton(self.frame)
        self.send_btn.setGeometry(QtCore.QRect(240, 210, 180, 40))
        self.send_btn.setMinimumSize(QtCore.QSize(180, 40))
        self.send_btn.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.send_btn.setFont(font)
        self.send_btn.setStyleSheet("QPushButton#send_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#send_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#send_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.send_btn.setObjectName("send_btn")
        self.msg_l = QtWidgets.QTextEdit(self.frame)
        self.msg_l.setGeometry(QtCore.QRect(40, 90, 371, 101))
        self.msg_l.setObjectName("msg_l")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 231, 31))
        self.label_2.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "    message"))
        self.close_button.setText(_translate("Form", "✖"))
        self.send_btn.setText(_translate("Form", "send"))
        self.label_2.setText(_translate("Form", "Your suggestion :"))
