import os
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from administrators_mata import AdministratorsMata
from nutrition_expert_mata import NutritionExpertMata
from ordinary_users_mata import OrdinaryUsersMata
from ui_py.login_ui import Ui_Form
from register_mata import RegisterMata
import sqlite3


class LoginMata(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  
        script_path = os.path.abspath(__file__)
        script_directory = os.path.dirname(script_path)
        self.db_path = os.path.join(script_directory, 'diet_tool.db')
        self.main_ui = None
        self._ui = None
        self.new_ui = None
        self.ui = Ui_Form()  
        self.ui.setupUi(self) 


    @pyqtSlot()
    def on_login_btn_clicked(self):
        account = self.ui.login_acc.text()
        psw = self.ui.login_psw.text()
        t_info = self.verify_account_password(account, psw)
        if len(t_info) != 0:
            if t_info[11] == 'User':
                self.new_ui = OrdinaryUsersMata(t_info, self.db_path)
            elif t_info[11] == 'Expert':
                self.new_ui = NutritionExpertMata(t_info, self.db_path)
            elif t_info[11] == 'Administrator':
                self.new_ui = AdministratorsMata(t_info, self.db_path)
            self.new_ui.show()
            self.close()

    def verify_account_password(self, acc, psw):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = f'SELECT * FROM account WHERE username=\'{acc}\''
        try:
            
            cur.execute(sql)
            
            info = cur.fetchone()
            if info[3] == psw:
                return info
            else:
                QMessageBox.information(self, 'Error', 'Password Error!',
                                    QMessageBox.Ok, QMessageBox.Ok)
                return ()
        except Exception as e:
            print(e)
            con.rollback()
            QMessageBox.information(self, 'Error', 'Account Password Error!',
                                    QMessageBox.Ok, QMessageBox.Ok)
            return ()
        finally:
            cur.close()
            con.close()



    @pyqtSlot()
    def on_register_btn_clicked(self):
        self._ui = RegisterMata(self.db_path)
        self._ui.show()

    @pyqtSlot()
    def on_exit_btn_clicked(self):
        self.close()

    @pyqtSlot()
    def on_close_button_clicked(self):
        self.close()

    def err_msg_dialog(self, msg):
        QMessageBox.about(self, "Attention!", msg)

    def mouseMoveEvent(self, e: QtGui.QMouseEvent):
        try:
            if (e.x() >= 10 and e.x() <= 451 and e.y() >= 0 and e.y() < 60):
                self._endPos = e.pos() - self._startPos
                self.move(self.pos() + self._endPos)
        except Exception as e:
            pass

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        try:
            if e.button() == QtCore.Qt.LeftButton:
                self._isTracking = True
                self._startPos = QtCore.QPoint(e.x(), e.y())
        except Exception as e:
            pass

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        try:
            if e.button() == QtCore.Qt.LeftButton:
                self._isTracking = False
                self._startPos = None
                self._endPos = None
        except Exception as e:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)  
    form = LoginMata() 
    form.show()
    sys.exit(app.exec_())
