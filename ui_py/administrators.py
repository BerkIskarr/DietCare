from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(452, 581)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 451, 581))
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
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 431, 511))
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
" \n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
" \n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"    width: 100px;\n"
"}\n"
" \n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
" \n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setMinimumSize(QtCore.QSize(0, 0))
        self.tab.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.manage_seek_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.manage_seek_line.setMinimumSize(QtCore.QSize(100, 40))
        self.manage_seek_line.setMaximumSize(QtCore.QSize(400, 40))
        self.manage_seek_line.setStyleSheet("border-radius:5px;\n"
"border:1px solid rgba(169,169,169,1.000);")
        self.manage_seek_line.setObjectName("manage_seek_line")
        self.horizontalLayout_7.addWidget(self.manage_seek_line)
        self.manage_seek_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.manage_seek_btn.setMinimumSize(QtCore.QSize(90, 40))
        self.manage_seek_btn.setMaximumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.manage_seek_btn.setFont(font)
        self.manage_seek_btn.setStyleSheet("QPushButton#manage_seek_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#manage_seek_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#manage_seek_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.manage_seek_btn.setObjectName("manage_seek_btn")
        self.horizontalLayout_7.addWidget(self.manage_seek_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.manage_name = QtWidgets.QLabel(self.layoutWidget)
        self.manage_name.setMinimumSize(QtCore.QSize(150, 40))
        self.manage_name.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.manage_name.setFont(font)
        self.manage_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.manage_name.setObjectName("manage_name")
        self.horizontalLayout_9.addWidget(self.manage_name)
        self.manage_name_l = QtWidgets.QLineEdit(self.layoutWidget)
        self.manage_name_l.setMinimumSize(QtCore.QSize(150, 40))
        self.manage_name_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.manage_name_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;\n"
"")
        self.manage_name_l.setText("")
        self.manage_name_l.setObjectName("manage_name_l")
        self.horizontalLayout_9.addWidget(self.manage_name_l)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.manage_sex = QtWidgets.QLabel(self.layoutWidget)
        self.manage_sex.setMinimumSize(QtCore.QSize(150, 40))
        self.manage_sex.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.manage_sex.setFont(font)
        self.manage_sex.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.manage_sex.setObjectName("manage_sex")
        self.horizontalLayout_10.addWidget(self.manage_sex)
        self.manage_sex_l = QtWidgets.QLineEdit(self.layoutWidget)
        self.manage_sex_l.setMinimumSize(QtCore.QSize(150, 40))
        self.manage_sex_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.manage_sex_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.manage_sex_l.setObjectName("manage_sex_l")
        self.horizontalLayout_10.addWidget(self.manage_sex_l)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.manage_age = QtWidgets.QLabel(self.layoutWidget)
        self.manage_age.setMinimumSize(QtCore.QSize(150, 40))
        self.manage_age.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.manage_age.setFont(font)
        self.manage_age.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.manage_age.setObjectName("manage_age")
        self.horizontalLayout_13.addWidget(self.manage_age)
        self.manage_age_l = QtWidgets.QLineEdit(self.layoutWidget)
        self.manage_age_l.setMinimumSize(QtCore.QSize(150, 40))
        self.manage_age_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.manage_age_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.manage_age_l.setText("")
        self.manage_age_l.setObjectName("manage_age_l")
        self.horizontalLayout_13.addWidget(self.manage_age_l)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.manage_height = QtWidgets.QLabel(self.layoutWidget)
        self.manage_height.setMinimumSize(QtCore.QSize(150, 40))
        self.manage_height.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.manage_height.setFont(font)
        self.manage_height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.manage_height.setObjectName("manage_height")
        self.horizontalLayout_8.addWidget(self.manage_height)
        self.manage_height_l = QtWidgets.QLineEdit(self.layoutWidget)
        self.manage_height_l.setMinimumSize(QtCore.QSize(150, 40))
        self.manage_height_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.manage_height_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.manage_height_l.setText("")
        self.manage_height_l.setObjectName("manage_height_l")
        self.horizontalLayout_8.addWidget(self.manage_height_l)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.manage_weight = QtWidgets.QLabel(self.layoutWidget)
        self.manage_weight.setMinimumSize(QtCore.QSize(150, 40))
        self.manage_weight.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.manage_weight.setFont(font)
        self.manage_weight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.manage_weight.setObjectName("manage_weight")
        self.horizontalLayout_11.addWidget(self.manage_weight)
        self.manage_weight_l = QtWidgets.QLineEdit(self.layoutWidget)
        self.manage_weight_l.setMinimumSize(QtCore.QSize(150, 40))
        self.manage_weight_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.manage_weight_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.manage_weight_l.setText("")
        self.manage_weight_l.setObjectName("manage_weight_l")
        self.horizontalLayout_11.addWidget(self.manage_weight_l)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.manage_re_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.manage_re_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.manage_re_btn.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.manage_re_btn.setFont(font)
        self.manage_re_btn.setStyleSheet("QPushButton#manage_re_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#manage_re_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#manage_re_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.manage_re_btn.setObjectName("manage_re_btn")
        self.horizontalLayout_12.addWidget(self.manage_re_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setMinimumSize(QtCore.QSize(0, 0))
        self.tab_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 40, 411, 441))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.info_acc = QtWidgets.QLabel(self.layoutWidget_3)
        self.info_acc.setMinimumSize(QtCore.QSize(150, 40))
        self.info_acc.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_acc.setFont(font)
        self.info_acc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.info_acc.setObjectName("info_acc")
        self.horizontalLayout.addWidget(self.info_acc)
        self.info_acc_l = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.info_acc_l.setMinimumSize(QtCore.QSize(150, 40))
        self.info_acc_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.info_acc_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.info_acc_l.setObjectName("info_acc_l")
        self.horizontalLayout.addWidget(self.info_acc_l)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.info_name = QtWidgets.QLabel(self.layoutWidget_3)
        self.info_name.setMinimumSize(QtCore.QSize(150, 40))
        self.info_name.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_name.setFont(font)
        self.info_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.info_name.setObjectName("info_name")
        self.horizontalLayout_2.addWidget(self.info_name)
        self.info_name_l = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.info_name_l.setMinimumSize(QtCore.QSize(150, 40))
        self.info_name_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.info_name_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.info_name_l.setObjectName("info_name_l")
        self.horizontalLayout_2.addWidget(self.info_name_l)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.info_age = QtWidgets.QLabel(self.layoutWidget_3)
        self.info_age.setMinimumSize(QtCore.QSize(150, 40))
        self.info_age.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_age.setFont(font)
        self.info_age.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.info_age.setObjectName("info_age")
        self.horizontalLayout_14.addWidget(self.info_age)
        self.info_age_l = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.info_age_l.setMinimumSize(QtCore.QSize(150, 40))
        self.info_age_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.info_age_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.info_age_l.setText("")
        self.info_age_l.setObjectName("info_age_l")
        self.horizontalLayout_14.addWidget(self.info_age_l)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.info_sex = QtWidgets.QLabel(self.layoutWidget_3)
        self.info_sex.setMinimumSize(QtCore.QSize(150, 40))
        self.info_sex.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_sex.setFont(font)
        self.info_sex.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.info_sex.setObjectName("info_sex")
        self.horizontalLayout_3.addWidget(self.info_sex)
        self.info_sex_l = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.info_sex_l.setMinimumSize(QtCore.QSize(150, 40))
        self.info_sex_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.info_sex_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.info_sex_l.setObjectName("info_sex_l")
        self.horizontalLayout_3.addWidget(self.info_sex_l)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.info_ID = QtWidgets.QLabel(self.layoutWidget_3)
        self.info_ID.setMinimumSize(QtCore.QSize(150, 40))
        self.info_ID.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_ID.setFont(font)
        self.info_ID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.info_ID.setObjectName("info_ID")
        self.horizontalLayout_4.addWidget(self.info_ID)
        self.info_ID_l = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.info_ID_l.setMinimumSize(QtCore.QSize(150, 40))
        self.info_ID_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.info_ID_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.info_ID_l.setObjectName("info_ID_l")
        self.horizontalLayout_4.addWidget(self.info_ID_l)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.info_re_btn = QtWidgets.QPushButton(self.layoutWidget_3)
        self.info_re_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.info_re_btn.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.info_re_btn.setFont(font)
        self.info_re_btn.setStyleSheet("QPushButton#info_re_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#info_re_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#info_re_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.info_re_btn.setObjectName("info_re_btn")
        self.horizontalLayout_6.addWidget(self.info_re_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "    Administrator"))
        self.close_button.setText(_translate("Form", "✖"))
        self.manage_seek_btn.setText(_translate("Form", "Search"))
        self.manage_name.setText(_translate("Form", "Name :"))
        self.manage_sex.setText(_translate("Form", "Gender :"))
        self.manage_age.setText(_translate("Form", "Age :"))
        self.manage_height.setText(_translate("Form", "Height :"))
        self.manage_weight.setText(_translate("Form", "Weight :"))
        self.manage_re_btn.setText(_translate("Form", "Modify"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Manage"))
        self.info_acc.setText(_translate("Form", "Username :"))
        self.info_name.setText(_translate("Form", "Name :"))
        self.info_age.setText(_translate("Form", "Age :"))
        self.info_sex.setText(_translate("Form", "Gender:"))
        self.info_ID.setText(_translate("Form", "EmployeeID:"))
        self.info_re_btn.setText(_translate("Form", "Modify"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Information"))
