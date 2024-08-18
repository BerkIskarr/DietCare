import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from message_dialog_mata import MessageDialogMata
from ui_py.nutrition_expert import Ui_Form
import sqlite3

class NutritionExpertMata(QWidget):

    def __init__(self, info, db_path, parent=None):
        super().__init__(parent)  
        self.ui = Ui_Form()  
        self.ui.setupUi(self)  
        self.db_path = db_path
        self.manage_acc = None
        self.manage_record = []
        self.init_info(info)
        self.init_lineEdit()


    def init_info(self, info):
        self.ui.info_acc_l.setText(info[1])
        if not info[2] is None:
            self.ui.info_name_l.setText(info[2])
        if not info[4] is None:
            self.ui.info_sex_l.setText(info[4])
        if not info[5] is None:
            self.ui.info_age_l.setText(info[5])
        if not info[10] is None:
            self.ui.info_ID_l.setText(info[10])

    def init_lineEdit(self):
        self.ui.info_acc_l.setReadOnly(True)
        self.ui.info_name_l.setReadOnly(True)
        self.ui.info_sex_l.setReadOnly(True)
        self.ui.info_age_l.setReadOnly(True)
        self.ui.info_ID_l.setReadOnly(True)

        self.ui.manage_name_l.setReadOnly(True)
        self.ui.manage_sex_l.setReadOnly(True)
        self.ui.manage_age_l.setReadOnly(True)
        self.ui.manage_height_l.setReadOnly(True)
        self.ui.manage_weight_l.setReadOnly(True)

    @pyqtSlot()
    def on_manage_seek_btn_clicked(self):
        self.manage_acc = self.ui.manage_seek_line.text()
        info = self.search_user(self.manage_acc)
        if info != None:
            self.show_user_info(info)
            self.get_user_record(info[0])
            self.show_user_record()
            self.show_water_intake()
        else:
            self.clear_user_info()
            self.manage_record = []


    def search_user(self,acc):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = f'SELECT * FROM account WHERE username=\'{acc}\' and type=\'User\''
        try:
            cur.execute(sql)
            info = cur.fetchone()
            if info == None:
                QMessageBox.information(self, 'Error', f'No User with name \"{acc}\"!',
                                    QMessageBox.Ok, QMessageBox.Ok)
                return None
            else:
                return(info)
        except Exception as e:
            print(e)
            con.rollback()
            QMessageBox.information(self, 'Error', 'Search Error!',
                                    QMessageBox.Ok, QMessageBox.Ok)
            return ()
        finally:
            cur.close()
            con.close()

    def get_user_record(self, id):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = f"SELECT * FROM daily_intake WHERE id = {id}"
        try:
            cur.execute(sql)
            self.manage_record = cur.fetchall()
        except Exception as e:
            print(e)
            con.rollback()
        finally:
            cur.close()
            con.close()

    @pyqtSlot(QtCore.QDate)
    def on_dateEdit_dateChanged(self):
        self.show_user_record()

    @pyqtSlot(int)
    def on_meal_cb_activated(self):
        self.show_user_record()

    def show_user_record(self):
        self.ui.recordBox.clear()
        date = self.ui.dateEdit.date().toString(QtCore.Qt.ISODate)
        meal = self.ui.meal_cb.currentText()
        for r in self.manage_record:
            if r[1] != None and r[3] == date and r[4] == meal:
                self.ui.recordBox.addItem(r[1])

    def show_water_intake(self):
        water_intake = 0
        for r in self.manage_record:
            water_intake += r[2]
        if water_intake > 2000:
            self.ui.progressBar.setValue(2000)
        else:
            self.ui.progressBar.setValue(water_intake)
        self.ui.label_water.setText(f"{water_intake} / 2000 mL")

    def show_user_info(self, info):
        if not info[2] is None:
            self.ui.manage_name_l.setText(info[2])
        if not info[4] is None:
            self.ui.manage_sex_l.setText(info[4])
        if not info[5] is None:
            self.ui.manage_age_l.setText(info[5])
        if not info[6] is None:
            self.ui.manage_height_l.setText(info[6])
        if not info[7] is None:
            self.ui.manage_weight_l.setText(info[7])

    def clear_user_info(self):
        self.ui.manage_name_l.setText('')
        self.ui.manage_sex_l.setText('')
        self.ui.manage_age_l.setText('')
        self.ui.manage_height_l.setText('')
        self.ui.manage_weight_l.setText('')

    @pyqtSlot()
    def on_suggest_btn_clicked(self):
        self.new_ui = MessageDialogMata(self.db_path,self.manage_acc)
        self.new_ui.show()

    @pyqtSlot()
    def on_info_re_btn_clicked(self):
        if self.ui.info_name_l.isReadOnly():
            self.ui.info_name_l.setReadOnly(False)
            self.ui.info_sex_l.setReadOnly(False)
            self.ui.info_age_l.setReadOnly(False)
            self.ui.info_ID_l.setReadOnly(False)
        else:
            self.ui.info_name_l.setReadOnly(True)
            self.ui.info_sex_l.setReadOnly(True)
            self.ui.info_age_l.setReadOnly(True)
            self.ui.info_ID_l.setReadOnly(True)
            is_suc = self.save_info(self.ui.info_acc_l.text(),
                                    self.ui.info_name_l.text(),
                                    self.ui.info_sex_l.text(),
                                    self.ui.info_age_l.text(),
                                    self.ui.info_ID_l.text()
                                    )
            if is_suc:
                QMessageBox.information(self, 'success', 'Modified successfully!',
                                        QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, 'Error', 'Modification failed!',
                                        QMessageBox.Ok, QMessageBox.Ok)

    def save_info(self, username, name, sex, age, certificationID):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = f'UPDATE account SET name = \'{name}\',gender = \'{sex}\',age =  \'{age}\',certificationID = \'{certificationID}\' WHERE username=\'{username}\''
        try:
          
            cur.execute(sql)
            con.commit()
            return True
        except Exception as e:
            print('save err')
            print(e)
            con.rollback()
            return False
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


if __name__ == '__main__':
    app = QApplication(sys.argv) 
    form = NutritionExpertMata() 
    form.show()
    sys.exit(app.exec_())