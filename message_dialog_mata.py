import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from ui_py.message_dialog import Ui_Form
import sqlite3


class MessageDialogMata(QWidget):

    def __init__(self, db_path, username, parent=None):
        super().__init__(parent) 
        self.ui = Ui_Form()  
        self.ui.setupUi(self)  
        self.db_path = db_path
        self.username = username

    # def show_user_list(self):
    #     con = sqlite3.connect(self.db_path)
    #     cur = con.cursor()
    #     sql = f'SELECT * FROM account WHERE type=\'User\''
    #     try:
    #         cur.execute(sql)
    #         info = cur.fetchall()
    #         return info
    #     except Exception as e:
    #         print(e)
    #         con.rollback()
    #         return []
    #     finally:
    #         cur.close()
    #         con.close()

    @pyqtSlot()
    def on_send_btn_clicked(self):
        msg = self.ui.msg_l.toPlainText()
        t_info = self.q_username(self.username)
        if len(t_info) == 0 or t_info[0] is None:
            l_list = [msg]
            is_suc = self.send_info(self.username, l_list)
            if is_suc:
                self.close()
            else:
                QMessageBox.information(self, 'Error', 'Send Fail!',
                                        QMessageBox.Ok, QMessageBox.Ok)
        else:
            n_info_list = []
            for i in range(len(t_info)):
                str_info = t_info[i]
                t_info = str_info.replace('-', '').replace('[', '').replace(']', '')
                n_info_list.append(t_info)
            n_info_list.append(msg)
            is_suc = self.send_info(self.username, n_info_list)
            if is_suc:
                self.close()
            else:
                QMessageBox.information(self, 'Error', 'Send Fail!',
                                        QMessageBox.Ok, QMessageBox.Ok)

    def send_info(self, username, msg):
        msg = str(msg)
        msg = msg.replace('\'', '-')
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = f'UPDATE account SET infos = \'{msg}\' WHERE username=\'{username}\''
        try:
            cur.execute(sql)
            con.commit()
            return True
        except Exception as e:
            print(e)
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()

    def q_username(self, username):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = f'SELECT infos FROM account WHERE username=\'{username}\''
        try:
            cur.execute(sql)
            info = cur.fetchone()
            return info
        except Exception as e:
            print(e)
            con.rollback()
            return ()
        finally:
            cur.close()
            con.close()


    @pyqtSlot()
    def on_close_button_clicked(self):
        self.close()

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
