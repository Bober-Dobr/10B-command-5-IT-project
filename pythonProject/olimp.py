import sys
from PyQt6 import uic
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from pymorphy3 import MorphAnalyzer
import datetime


class MoneyCalc(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design_for_MoneyCalc_project.ui', self)
        self.morph = MorphAnalyzer()

        self.sumInp.setValidator(QRegularExpressionValidator(QRegularExpression(r'\d+')))
        self.sumInp.textEdited.connect(self.textEdit)

        self.setDream.clicked.connect(self.setDreamClicked)

        self.setDreamConf.clicked.connect(self.setDreamConfClicked)

        self.dreamCost.setValidator(QRegularExpressionValidator(QRegularExpression(r'\d+')))

        self.fillPiggyConf.setVisible(False)
        self.fillPiggySum.setVisible(False)
        self.fillPiggySum.setValidator(QRegularExpressionValidator(QRegularExpression(r'\d+')))
        self.fillPiggyConf.clicked.connect(self.fillPiggy)
        self.fiillPiggy.clicked.connect(self.fillPiggyButton)

        self.setNames()


    def textEdit(self):
        if self.sender() is self.sumInp:
            self.rub_1.setText(self.morph.parse('рубль')[0].make_agree_with_number(int(self.sumInp.text())).word)

    def setDreamClicked(self):
        self.dreamInp.setVisible(not self.dreamInp.isVisible())
        self.setDreamConf.setVisible(not self.setDreamConf.isVisible())
        self.dreamCost.setVisible(not  self.dreamCost.isVisible())

    def setDreamConfClicked(self):
        try:
            p = self.dreamInp.text()[0]
            p1 = int(self.dreamCost.text())
            self.dreamName.setText(self.dreamInp.text())
            f = open('data.txt', 'r')
            f1 = open('data1.txt', 'w')
            for i in f.readlines():
                if 'dreamCost' in i or "dreamName" in i:
                    continue
                f1.write(f'{i}')
            f1.write(f'dreamCost = {int(self.dreamCost.text())}\n')
            f1.write(f'dreamName = {self.dreamInp.text()}\n')
            f1.close()
            f = open('data.txt', 'w')
            f1 = open('data1.txt', 'r')
            for i in f1.readlines():
                f.write(i)
            f.close()
            f1.close()
            f = open('data.txt', 'r').read()
            ind = f.index('dreamCost = ') + len('dreamCost = ')
            dr_cost = int(f[ind:ind + f[ind::].index('\n')])
            self.progressBar.setValue(self.lcdNumber.intValue() // dr_cost)
        except IndexError:
            msg = QMessageBox()
            msg.setIcon(msg.icon().Critical)
            msg.setInformativeText("Введите название мечты")
            msg.setWindowTitle("Error")
            msg.show()
            msg.exec()
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(msg.icon().Critical)
            msg.setInformativeText("Указана некорректная цена")
            msg.setWindowTitle("Error")
            msg.show()
            msg.exec()

    def setNames(self):
        data = open('data.txt', 'r').read()
        if 'dreamName' in data:
            ind = data.index('dreamName = ')
            indl = (data[ind::]).find('\n') + ind
            self.dreamName.setText(data[ind + len('dreamName = '):indl])
            self.dreamInp.setVisible(False)
            self.dreamCost.setVisible(False)
            self.setDreamConf.setVisible(False)

    def fillPiggyButton(self):
        self.fillPiggyConf.setVisible(not self.fillPiggyConf.isVisible())
        self.fillPiggySum.setVisible(not self.fillPiggySum.isVisible())

    def fillPiggy(self):
        if not self.fillPiggySum.text() or int(self.fillPiggySum.text()) > self.lcdNumber_2.intValue():
            msg = QMessageBox()
            msg.setIcon(msg.icon().Critical)
            msg.setInformativeText("Некорректное знаечние дял пополнения")
            msg.setWindowTitle("Error")
            msg.show()
            msg.exec()
        else:
            today = datetime.date.today()
            calendar = open('calendar.txt', 'r')
            calendar1 = open("calendar1.txt", 'w')
            c = calendar.readlines()
            if str(today) in ''.join(c):
                for i in range(len(c) - 1):
                    calendar1.write(c[i])
                calendar1.write(f'{c[-1].strip('\n')} &{int(self.fillPiggySum.text())}\n')
                calendar.close()
                calendar1.close()
                calendar = open('calendar.txt', 'w')
                calendar1 = open('calendar1.txt', 'r').readlines()
                for i in calendar1:
                    calendar.write(i)
                calendar.close()
            else:
                open('calendar.txt', 'a').write(f'{str(today)} &{int(self.fillPiggySum.text())}\n')
            self.lcdNumber.display(str(int(self.fillPiggySum.text()) + int(self.lcdNumber.intValue())))
            f = open('data.txt', 'r').read()
            try:
                ind = f.index('dreamCost = ') + len('dreamCost = ')
                dr_cost = int(f[ind:ind + f[ind::].index('\n')])
                self.progressBar.setValue(self.lcdNumber.intValue() // dr_cost)
            except ValueError:
                msg = QMessageBox()
                msg.setIcon(msg.icon().Information)
                msg.setInformativeText("Стоимость мечты не задана, поэто прогресс-бар пока не работает :(")
                msg.setWindowTitle("Важно!")
                msg.show()
                msg.exec()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MoneyCalc()
    mc.show()
    sys.exit(app.exec())