from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(462, 748)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 461, 751))
        self.frame.setStyleSheet("QFrame#frame{\n"
"    background-color: rgba(242,242,242,1.000);\n"
"    border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setItalic(False)
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
        self.close_button.setGeometry(QtCore.QRect(420, 10, 25, 25))
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
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 441, 681))
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
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(30, 250, 291, 21))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border:2px solid grey;\n"
"    border-radius:5px;\n"
"    background-color:#FFFFFF;\n"
"    text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    background:QLinearGradient(x1:0,y1:0,x2:2,y2:0,stop:0 #666699,stop:1 #DB7093);\n"
"}")
        self.progressBar.setMaximum(2000)
        self.progressBar.setProperty("value", 200)
        self.progressBar.setObjectName("progressBar")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 381, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setMinimumSize(QtCore.QSize(150, 25))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 2, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_7.addWidget(self.dateEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.meal_cb = QtWidgets.QComboBox(self.layoutWidget)
        self.meal_cb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meal_cb.sizePolicy().hasHeightForWidth())
        self.meal_cb.setSizePolicy(sizePolicy)
        self.meal_cb.setMinimumSize(QtCore.QSize(84, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.meal_cb.setFont(font)
        self.meal_cb.setStyleSheet("QComboBox#meal_cb{\n"
"    background-color:rgb(9, 186, 0);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QComboBox#meal_cb:hover{\n"
"    background-color:rgb(11, 222, 0);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QComboBox#meal_cb:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:(11, 222, 0);\n"
"}")
        self.meal_cb.setObjectName("meal_cb")
        self.meal_cb.addItem("")
        self.meal_cb.addItem("")
        self.meal_cb.addItem("")
        self.meal_cb.addItem("")
        self.horizontalLayout_7.addWidget(self.meal_cb)
        self.add_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.add_btn.setMinimumSize(QtCore.QSize(100, 25))
        self.add_btn.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("QPushButton#add_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#add_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#add_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_7.addWidget(self.add_btn)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 270, 381, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.clearWater_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.clearWater_btn.setFont(font)
        self.clearWater_btn.setStyleSheet("QPushButton#clearWater_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#clearWater_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#clearWater_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.clearWater_btn.setObjectName("clearWater_btn")
        self.horizontalLayout_9.addWidget(self.clearWater_btn)
        self.add200_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.add200_btn.setFont(font)
        self.add200_btn.setStyleSheet("QPushButton#add200_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#add200_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#add200_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.add200_btn.setObjectName("add200_btn")
        self.horizontalLayout_9.addWidget(self.add200_btn)
        self.add400_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.add400_btn.setFont(font)
        self.add400_btn.setStyleSheet("QPushButton#add400_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#add400_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#add400_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.add400_btn.setObjectName("add400_btn")
        self.horizontalLayout_9.addWidget(self.add400_btn)
        self.add800_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.add800_btn.setFont(font)
        self.add800_btn.setStyleSheet("QPushButton#add800_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#add800_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#add800_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.add800_btn.setObjectName("add800_btn")
        self.horizontalLayout_9.addWidget(self.add800_btn)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(330, 250, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(9, 186, 0);\n"
"border-radius:5px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 59, 381, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.searchBar = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.searchBar.setObjectName("searchBar")
        self.verticalLayout_3.addWidget(self.searchBar)
        self.suggestionBox = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.suggestionBox.setObjectName("suggestionBox")
        self.verticalLayout_3.addWidget(self.suggestionBox)
        self.selectedItemsBox = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.selectedItemsBox.setObjectName("selectedItemsBox")
        self.verticalLayout_3.addWidget(self.selectedItemsBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 320, 181, 341))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.searchBar_meal_selection = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.searchBar_meal_selection.setObjectName("searchBar_meal_selection")
        self.horizontalLayout_8.addWidget(self.searchBar_meal_selection)
        self.meal_cb_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.meal_cb_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meal_cb_2.sizePolicy().hasHeightForWidth())
        self.meal_cb_2.setSizePolicy(sizePolicy)
        self.meal_cb_2.setMinimumSize(QtCore.QSize(40, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        self.meal_cb_2.setFont(font)
        self.meal_cb_2.setStyleSheet("QComboBox#meal_cb{\n"
"    background-color:rgb(9, 186, 0);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QComboBox#meal_cb:hover{\n"
"    background-color:rgb(11, 222, 0);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QComboBox#meal_cb:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:(11, 222, 0);\n"
"}")
        self.meal_cb_2.setObjectName("meal_cb_2")
        self.meal_cb_2.addItem("")
        self.meal_cb_2.addItem("")
        self.meal_cb_2.addItem("")
        self.meal_cb_2.addItem("")
        self.horizontalLayout_8.addWidget(self.meal_cb_2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.suggestionBox_meal_selection = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.suggestionBox_meal_selection.setObjectName("suggestionBox_meal_selection")
        self.verticalLayout_13.addWidget(self.suggestionBox_meal_selection)
        self.treeWidget_meal_breakfast = QtWidgets.QTreeWidget(self.verticalLayoutWidget_3)
        self.treeWidget_meal_breakfast.setObjectName("treeWidget_meal_breakfast")
        self.verticalLayout_13.addWidget(self.treeWidget_meal_breakfast)
        self.treeWidget_lunch_meal = QtWidgets.QTreeWidget(self.verticalLayoutWidget_3)
        self.treeWidget_lunch_meal.setObjectName("treeWidget_lunch_meal")
        self.verticalLayout_13.addWidget(self.treeWidget_lunch_meal)
        self.treeWidget_dinner_meal = QtWidgets.QTreeWidget(self.verticalLayoutWidget_3)
        self.treeWidget_dinner_meal.setObjectName("treeWidget_dinner_meal")
        self.verticalLayout_13.addWidget(self.treeWidget_dinner_meal)
        self.treeWidget_snack_meal = QtWidgets.QTreeWidget(self.verticalLayoutWidget_3)
        self.treeWidget_snack_meal.setObjectName("treeWidget_snack_meal")
        self.verticalLayout_13.addWidget(self.treeWidget_snack_meal)
        self.record_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.record_btn.setMinimumSize(QtCore.QSize(100, 25))
        self.record_btn.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.record_btn.setFont(font)
        self.record_btn.setStyleSheet("QPushButton#record_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#record_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#record_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.record_btn.setObjectName("record_btn")
        self.verticalLayout_13.addWidget(self.record_btn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(230, 320, 191, 341))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.treeWidget_breakfast = QtWidgets.QTreeWidget(self.verticalLayoutWidget_4)
        self.treeWidget_breakfast.setObjectName("treeWidget_breakfast")
        self.verticalLayout_14.addWidget(self.treeWidget_breakfast)
        self.treeWidget_lunch = QtWidgets.QTreeWidget(self.verticalLayoutWidget_4)
        self.treeWidget_lunch.setObjectName("treeWidget_lunch")
        self.verticalLayout_14.addWidget(self.treeWidget_lunch)
        self.treeWidget_dinner = QtWidgets.QTreeWidget(self.verticalLayoutWidget_4)
        self.treeWidget_dinner.setObjectName("treeWidget_dinner")
        self.verticalLayout_14.addWidget(self.treeWidget_dinner)
        self.treeWidget_snack = QtWidgets.QTreeWidget(self.verticalLayoutWidget_4)
        self.treeWidget_snack.setObjectName("treeWidget_snack")
        self.verticalLayout_14.addWidget(self.treeWidget_snack)
        self.recommend_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.recommend_btn.setMinimumSize(QtCore.QSize(150, 25))
        self.recommend_btn.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.recommend_btn.setFont(font)
        self.recommend_btn.setStyleSheet("QPushButton#recommend_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#recommend_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#recommend_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.recommend_btn.setObjectName("recommend_btn")
        self.verticalLayout_14.addWidget(self.recommend_btn, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tab_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 70, 441, 571))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_5 = QtWidgets.QLabel(self.tab_8)
        self.label_5.setGeometry(QtCore.QRect(90, 240, 271, 21))
        self.label_5.setObjectName("label_5")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.save_btn = QtWidgets.QPushButton(self.tab_2)
        self.save_btn.setGeometry(QtCore.QRect(340, 630, 100, 25))
        self.save_btn.setMinimumSize(QtCore.QSize(100, 25))
        self.save_btn.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("QPushButton#save_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#save_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#save_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 441, 63))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.horizontalLayoutWidget_2)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(150, 25))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 2, 1), QtCore.QTime(23, 59, 59)))
        self.dateEdit_2.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2024, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout_4.addWidget(self.dateEdit_2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.horizontalLayoutWidget_2)
        self.dateEdit_3.setMinimumSize(QtCore.QSize(150, 25))
        self.dateEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 3, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_3.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2024, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit_3.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 9, 13), QtCore.QTime(16, 0, 0)))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.verticalLayout_5.addWidget(self.dateEdit_3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.save_btn_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.save_btn_2.setMinimumSize(QtCore.QSize(100, 25))
        self.save_btn_2.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.save_btn_2.setFont(font)
        self.save_btn_2.setMouseTracking(True)
        self.save_btn_2.setStyleSheet("QPushButton#save_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#save_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#save_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.save_btn_2.setObjectName("save_btn_2")
        self.horizontalLayout_10.addWidget(self.save_btn_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setMinimumSize(QtCore.QSize(0, 0))
        self.tab_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab_3.setObjectName("tab_3")
        self.warn_num = QtWidgets.QPushButton(self.tab_3)
        self.warn_num.setGeometry(QtCore.QRect(390, 10, 25, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warn_num.sizePolicy().hasHeightForWidth())
        self.warn_num.setSizePolicy(sizePolicy)
        self.warn_num.setMinimumSize(QtCore.QSize(25, 25))
        self.warn_num.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.warn_num.setFont(font)
        self.warn_num.setStyleSheet("QPushButton#warn_num{\n"
"    background-color:rgb(255, 0, 0);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#warn_num:hover{\n"
"    background-color:rgb(255, 0, 0);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#warn_num:pressed{\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.warn_num.setObjectName("warn_num")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 401, 427))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acc = QtWidgets.QLabel(self.layoutWidget1)
        self.acc.setMinimumSize(QtCore.QSize(150, 40))
        self.acc.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        self.acc.setFont(font)
        self.acc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.acc.setObjectName("acc")
        self.horizontalLayout.addWidget(self.acc)
        self.acc_l = QtWidgets.QLineEdit(self.layoutWidget1)
        self.acc_l.setMinimumSize(QtCore.QSize(150, 40))
        self.acc_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.acc_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.acc_l.setObjectName("acc_l")
        self.horizontalLayout.addWidget(self.acc_l)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name = QtWidgets.QLabel(self.layoutWidget1)
        self.name.setMinimumSize(QtCore.QSize(150, 40))
        self.name.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        self.name.setFont(font)
        self.name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name.setObjectName("name")
        self.horizontalLayout_2.addWidget(self.name)
        self.name_l = QtWidgets.QLineEdit(self.layoutWidget1)
        self.name_l.setMinimumSize(QtCore.QSize(150, 40))
        self.name_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.name_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.name_l.setObjectName("name_l")
        self.horizontalLayout_2.addWidget(self.name_l)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.age = QtWidgets.QLabel(self.layoutWidget1)
        self.age.setMinimumSize(QtCore.QSize(150, 40))
        self.age.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        self.age.setFont(font)
        self.age.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.age.setObjectName("age")
        self.horizontalLayout_14.addWidget(self.age)
        self.age_l = QtWidgets.QLineEdit(self.layoutWidget1)
        self.age_l.setMinimumSize(QtCore.QSize(150, 40))
        self.age_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.age_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.age_l.setText("")
        self.age_l.setObjectName("age_l")
        self.horizontalLayout_14.addWidget(self.age_l)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sex = QtWidgets.QLabel(self.layoutWidget1)
        self.sex.setMinimumSize(QtCore.QSize(150, 40))
        self.sex.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        self.sex.setFont(font)
        self.sex.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sex.setObjectName("sex")
        self.horizontalLayout_3.addWidget(self.sex)
        self.sex_l = QtWidgets.QLineEdit(self.layoutWidget1)
        self.sex_l.setMinimumSize(QtCore.QSize(150, 40))
        self.sex_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.sex_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.sex_l.setObjectName("sex_l")
        self.horizontalLayout_3.addWidget(self.sex_l)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.height = QtWidgets.QLabel(self.layoutWidget1)
        self.height.setMinimumSize(QtCore.QSize(150, 40))
        self.height.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        self.height.setFont(font)
        self.height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.height.setObjectName("height")
        self.horizontalLayout_4.addWidget(self.height)
        self.height_l = QtWidgets.QLineEdit(self.layoutWidget1)
        self.height_l.setMinimumSize(QtCore.QSize(150, 40))
        self.height_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.height_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.height_l.setObjectName("height_l")
        self.horizontalLayout_4.addWidget(self.height_l)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.weight = QtWidgets.QLabel(self.layoutWidget1)
        self.weight.setMinimumSize(QtCore.QSize(150, 40))
        self.weight.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        self.weight.setFont(font)
        self.weight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weight.setObjectName("weight")
        self.horizontalLayout_5.addWidget(self.weight)
        self.weight_l = QtWidgets.QLineEdit(self.layoutWidget1)
        self.weight_l.setMinimumSize(QtCore.QSize(150, 40))
        self.weight_l.setMaximumSize(QtCore.QSize(1000, 40))
        self.weight_l.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgb(50, 50, 50);\n"
"padding-bottom:7px;")
        self.weight_l.setObjectName("weight_l")
        self.horizontalLayout_5.addWidget(self.weight_l)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clear_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.clear_btn.setMinimumSize(QtCore.QSize(100, 25))
        self.clear_btn.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("QPushButton#clear_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#clear_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#clear_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_6.addWidget(self.clear_btn)
        self.re_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.re_btn.setMinimumSize(QtCore.QSize(100, 25))
        self.re_btn.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.re_btn.setFont(font)
        self.re_btn.setStyleSheet("QPushButton#re_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#re_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#re_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.re_btn.setObjectName("re_btn")
        self.horizontalLayout_6.addWidget(self.re_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 450, 401, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_dietary_goal = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_dietary_goal.setFont(font)
        self.label_dietary_goal.setObjectName("label_dietary_goal")
        self.verticalLayout_6.addWidget(self.label_dietary_goal, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_exercise = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_exercise.setFont(font)
        self.label_exercise.setObjectName("label_exercise")
        self.verticalLayout_7.addWidget(self.label_exercise, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_exercise = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_exercise.setObjectName("comboBox_exercise")
        self.comboBox_exercise.addItem("")
        self.comboBox_exercise.addItem("")
        self.comboBox_exercise.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_exercise)
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_calorie = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_calorie.setFont(font)
        self.label_calorie.setObjectName("label_calorie")
        self.verticalLayout_8.addWidget(self.label_calorie, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_calorie = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_calorie.setObjectName("comboBox_calorie")
        self.comboBox_calorie.addItem("")
        self.comboBox_calorie.addItem("")
        self.comboBox_calorie.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox_calorie)
        self.horizontalLayout_11.addLayout(self.verticalLayout_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_sugar = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_sugar.setFont(font)
        self.label_sugar.setObjectName("label_sugar")
        self.verticalLayout_9.addWidget(self.label_sugar, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_sugar = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_sugar.setObjectName("comboBox_sugar")
        self.comboBox_sugar.addItem("")
        self.comboBox_sugar.addItem("")
        self.comboBox_sugar.addItem("")
        self.verticalLayout_9.addWidget(self.comboBox_sugar)
        self.horizontalLayout_12.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_salt = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_salt.setFont(font)
        self.label_salt.setObjectName("label_salt")
        self.verticalLayout_10.addWidget(self.label_salt, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_salt = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_salt.setObjectName("comboBox_salt")
        self.comboBox_salt.addItem("")
        self.comboBox_salt.addItem("")
        self.comboBox_salt.addItem("")
        self.verticalLayout_10.addWidget(self.comboBox_salt)
        self.horizontalLayout_12.addLayout(self.verticalLayout_10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_potassium = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_potassium.setFont(font)
        self.label_potassium.setObjectName("label_potassium")
        self.verticalLayout_11.addWidget(self.label_potassium, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_potassium = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_potassium.setObjectName("comboBox_potassium")
        self.comboBox_potassium.addItem("")
        self.comboBox_potassium.addItem("")
        self.comboBox_potassium.addItem("")
        self.verticalLayout_11.addWidget(self.comboBox_potassium)
        self.horizontalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_vegan = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_vegan.setFont(font)
        self.label_vegan.setObjectName("label_vegan")
        self.verticalLayout_12.addWidget(self.label_vegan, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_vegan = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_vegan.setObjectName("comboBox_vegan")
        self.comboBox_vegan.addItem("")
        self.comboBox_vegan.addItem("")
        self.verticalLayout_12.addWidget(self.comboBox_vegan)
        self.horizontalLayout_13.addLayout(self.verticalLayout_12)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.save_dietargoal_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.save_dietargoal_btn.setMinimumSize(QtCore.QSize(100, 35))
        self.save_dietargoal_btn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.save_dietargoal_btn.setFont(font)
        self.save_dietargoal_btn.setMouseTracking(True)
        self.save_dietargoal_btn.setStyleSheet("QPushButton#re_btn{\n"
"    background-color:rgb(55, 1, 132);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#re_btn:hover{\n"
"    background-color:rgba(2,62,118,150);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#re_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,62,118,100);\n"
"}")
        self.save_dietargoal_btn.setObjectName("save_dietargoal_btn")
        self.verticalLayout_6.addWidget(self.save_dietargoal_btn, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "    User"))
        self.close_button.setText(_translate("Form", "✖"))
        self.meal_cb.setCurrentText(_translate("Form", "Breakfast"))
        self.meal_cb.setItemText(0, _translate("Form", "Breakfast"))
        self.meal_cb.setItemText(1, _translate("Form", "Lunch"))
        self.meal_cb.setItemText(2, _translate("Form", "Dinner"))
        self.meal_cb.setItemText(3, _translate("Form", "Snack"))
        self.add_btn.setText(_translate("Form", "add"))
        self.clearWater_btn.setText(_translate("Form", "Clear"))
        self.add200_btn.setText(_translate("Form", "Add 200ml"))
        self.add400_btn.setText(_translate("Form", "Add 400ml"))
        self.add800_btn.setText(_translate("Form", "Add 800ml"))
        self.label_2.setText(_translate("Form", " of 2000ml"))
        self.meal_cb_2.setCurrentText(_translate("Form", "Breakfast"))
        self.meal_cb_2.setItemText(0, _translate("Form", "Breakfast"))
        self.meal_cb_2.setItemText(1, _translate("Form", "Lunch"))
        self.meal_cb_2.setItemText(2, _translate("Form", "Dinner"))
        self.meal_cb_2.setItemText(3, _translate("Form", "Snack"))
        self.treeWidget_meal_breakfast.headerItem().setText(0, _translate("Form", "Breakfast"))
        self.treeWidget_lunch_meal.headerItem().setText(0, _translate("Form", "Lunch"))
        self.treeWidget_dinner_meal.headerItem().setText(0, _translate("Form", "Dinner"))
        self.treeWidget_snack_meal.headerItem().setText(0, _translate("Form", "Snack"))
        self.record_btn.setText(_translate("Form", "Record"))
        self.treeWidget_breakfast.headerItem().setText(0, _translate("Form", "Breakfast"))
        self.treeWidget_lunch.headerItem().setText(0, _translate("Form", "Lunch"))
        self.treeWidget_dinner.headerItem().setText(0, _translate("Form", "Dinner"))
        self.treeWidget_snack.headerItem().setText(0, _translate("Form", "Snack"))
        self.recommend_btn.setText(_translate("Form", "Recommend"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "DietRecord"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "Daily Average"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "Weekly Average"))
        self.label_5.setText(_translate("Form", "Please select date and generate the report!"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Form", "Monthly Average"))
        self.save_btn.setText(_translate("Form", "Export"))
        self.label_3.setText(_translate("Form", "Start Date:"))
        self.label_4.setText(_translate("Form", "End Date:"))
        self.save_btn_2.setText(_translate("Form", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Report"))
        self.warn_num.setText(_translate("Form", "0"))
        self.acc.setText(_translate("Form", "Username :"))
        self.name.setText(_translate("Form", "Name :"))
        self.age.setText(_translate("Form", "Age :"))
        self.sex.setText(_translate("Form", "Gender :"))
        self.height.setText(_translate("Form", "Height :"))
        self.weight.setText(_translate("Form", "Weight :"))
        self.clear_btn.setText(_translate("Form", "Clear"))
        self.re_btn.setText(_translate("Form", "Modify"))
        self.label_dietary_goal.setText(_translate("Form", "Dietary Goal"))
        self.label_exercise.setText(_translate("Form", "Exercise:"))
        self.comboBox_exercise.setCurrentText(_translate("Form", "Not Active"))
        self.comboBox_exercise.setItemText(0, _translate("Form", "Not Active"))
        self.comboBox_exercise.setItemText(1, _translate("Form", "Active (1-4 days)"))
        self.comboBox_exercise.setItemText(2, _translate("Form", "Very Active (5-7 days)"))
        self.label_calorie.setText(_translate("Form", "Calorie Goal:"))
        self.comboBox_calorie.setItemText(0, _translate("Form", "Maintain Weigth"))
        self.comboBox_calorie.setItemText(1, _translate("Form", "Lose Weight"))
        self.comboBox_calorie.setItemText(2, _translate("Form", "Gain Weight"))
        self.label_sugar.setText(_translate("Form", "Sugar Goal:"))
        self.comboBox_sugar.setCurrentText(_translate("Form", "Normal Sugar Intake"))
        self.comboBox_sugar.setItemText(0, _translate("Form", "Normal Sugar Intake"))
        self.comboBox_sugar.setItemText(1, _translate("Form", "Low Sugar Intake"))
        self.comboBox_sugar.setItemText(2, _translate("Form", "High Sugar Intake"))
        self.label_salt.setText(_translate("Form", "Salt Goal:"))
        self.comboBox_salt.setItemText(0, _translate("Form", "Normal Salt Intake"))
        self.comboBox_salt.setItemText(1, _translate("Form", "Low Salt Intake"))
        self.comboBox_salt.setItemText(2, _translate("Form", "High Salt Intake"))
        self.label_potassium.setText(_translate("Form", "Potassium Goal:"))
        self.comboBox_potassium.setCurrentText(_translate("Form", "Normal Potassium Intake"))
        self.comboBox_potassium.setItemText(0, _translate("Form", "Normal Potassium Intake"))
        self.comboBox_potassium.setItemText(1, _translate("Form", "Low Potassium Intake"))
        self.comboBox_potassium.setItemText(2, _translate("Form", "High Potassium Intake"))
        self.label_vegan.setText(_translate("Form", "Are You Vegan?"))
        self.comboBox_vegan.setItemText(0, _translate("Form", "No"))
        self.comboBox_vegan.setItemText(1, _translate("Form", "Yes"))
        self.save_dietargoal_btn.setText(_translate("Form", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Information"))
