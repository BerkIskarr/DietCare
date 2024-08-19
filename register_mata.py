import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot, QRegExp
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QAction, QLineEdit

from ui_py.register_ui import Ui_Form
import sqlite3


class RegisterMata(QWidget):

    def __init__(self, db_path, parent=None):
        super().__init__(parent) 
        self.password_count = 1
        self.account_count = 1
        self.name_count = 1
        self.ui = Ui_Form()  
        self.ui.setupUi(self) 
        self.db_path = db_path
        self.ui.comboBox.addItem('User')
        self.ui.comboBox.addItem('Expert')
        self.ui.comboBox.addItem('Administrator')

    @pyqtSlot()
    def on_register_btn_clicked(self):
        if len(self.ui.lineEdit_name.text()) == 0 or len(self.ui.lineEdit_password.text()) == 0:
            QMessageBox.information(self, 'Error', 'Registration information cannot be empty!',
                                                QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.is_exist(self.ui.lineEdit_name.text()):
                con = sqlite3.connect(self.db_path)

                cur = con.cursor()

                sql = 'insert into account(username,password,type) values(?,?,?)'
                try:
                    cur.execute(sql, (self.ui.lineEdit_name.text(), self.ui.lineEdit_password.text(), self.ui.comboBox.currentText()))

                    con.commit()
                    QMessageBox.information(self, 'success', 'Registration was successful!',
                                            QMessageBox.Ok, QMessageBox.Ok)
                    self.close()
                except Exception as e:
                    print(e)
                    QMessageBox.information(self, 'Error', 'Registration information cannot be empty!',
                                            QMessageBox.Ok, QMessageBox.Ok)
                    con.rollback()
                finally:
                    cur.close()
                    con.close()

    def is_exist(self, username):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = f'SELECT * FROM account WHERE username=\'{username}\''
        try:

            cur.execute(sql)

            info = cur.fetchone()
            if not info is None:
                QMessageBox.information(self, 'Error', 'The username already exists!',
                                        QMessageBox.Ok, QMessageBox.Ok)
                return False
            else:
                return True
        except Exception as e:
            print(e)
            con.rollback()
            return True
        finally:
            cur.close()
            con.close()

    @pyqtSlot()
    def on_exit_btn_clicked(self):
        self.close()

    @pyqtSlot()
    def on_close_button_clicked(self):
        self.close()

    def action_confirm_account(self):
        self.confirm_account()
        if self.account_count == 0:
            QMessageBox.information(self, 'Congratulations', 'This account is valid!')

    def confirm_name(self):
        self.ui.tip_name.setText("Your name")
        self.ui.tip_name.setStyleSheet("color:black;")
        self.name_count = 0

        name = self.ui.lineEdit_name.text()
        if len(name) == 0:
            QMessageBox.warning(self, "Warning", "User Name is empty!")
            self.ui.tip_name.setText("User Name is empty!")
            self.ui.tip_name.setStyleSheet("color:red;") 
            self.name_count = 1

    def confirm_account(self):
        account_str = "Length of 5-15 characters, consisting of numbers and letters."
        self.ui.tip_account.setText(account_str)
        self.ui.tip_account.setStyleSheet("color:black;")
        self.account_count = 0
        account = self.ui.lineEdit_account.text()
        if len(account) == 0:
            account_str = "Account is empty"
        elif len(account) < 5:
            account_str = "Account is less than 5 characters"
        else:
            # count = judge_account(account)  
            if count == 1:
                account_str = "The account is used."
        if account_str != "Length of 5-15 characters, consisting of numbers and letters.":
            QMessageBox.warning(self, "Warning", account_str)
            self.ui.tip_account.setText(account_str)
            self.ui.tip_account.setStyleSheet("color:red;") 
            self.account_count = 1

    def confirm_password(self):
        self.ui.tip_password.setText("Length of 6-15 characters, consisting of numbers and letters.")
        self.ui.tip_confirmpassword.setText("Confirm")
        self.ui.tip_password.setStyleSheet("color:black;")
        self.ui.tip_confirmpassword.setStyleSheet("color:black;")
        self.password_count = 0
        password = self.ui.lineEdit_password.text()
        if len(password) == 0:
            QMessageBox.warning(self, "Warning", "Password is empty")
            self.ui.tip_password.setText("Password is empty")
            self.ui.tip_password.setStyleSheet("color:red;")
            self.password_count = 1
        elif len(password) < 6:
            QMessageBox.warning(self, "Warning", " less than 5 characters")
            self.ui.tip_password.setText(" less than 5 characters")
            self.ui.tip_password.setStyleSheet("color:red;")
            self.password_count = 1
        elif password != con_password:
            reply = QMessageBox.critical(self, 'Wrong', 'The passwords entered do not match.',
                                         QMessageBox.Retry, QMessageBox.Retry)
            self.ui.tip_confirmpassword.setText("The passwords entered do not match.")
            self.ui.tip_confirmpassword.setStyleSheet("color:red;") 
            if reply == QMessageBox.Retry:
                self.ui.lineEdit_password.clear()
                self.password_count = 1

    def action_confirm_account(self):
        self.confirm_account()
        if self.account_count == 0:
            QMessageBox.information(self, 'Congratulations', 'This account is valid!')

    def add_account(self):
        name = self.ui.lineEdit_name.text() 
        password = self.ui.lineEdit_password.text()
        print(f"Account->{name},Password->{password}")

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
    form = RegisterMata()  
    form.show()
    sys.exit(app.exec_())
