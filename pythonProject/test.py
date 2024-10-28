import sys
from PyQt6 import uic
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from pymorphy3 import MorphAnalyzer


class passManager(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('passManager.ui', self)
		self.initUI()

	def initUI(self):
		self.addPass.clicked.connect(self.addPassClick)
		self.readLoginBtn.clicked.connect(self.readLoginBtnClick)
		self.run.clicked.connect(self.openFile)
		self.stop.clicked.connect(self.closeFile)

		self.stop.setVisible(False)
		self.label.setVisible(False)
		self.label_3.setVisible(False)
		self.newPassIsFrom.setVisible(False)
		self.newPass.setVisible(False)
		self.addPass.setVisible(False)

	def addPassClick(self):
		print(f'{self.newPassIsFrom.text()}###@~KEYnPASSWORD~@###23042008BadKonstB{self.newPass.text()}', file=self.f)

	def openFile(self):
		self.f = open('passwords.txt', 'a')
		self.run.setEnabled(False)
		self.stop.setVisible(True)
		self.label.setVisible(True)
		self.label_3.setVisible(True)
		self.newPassIsFrom.setVisible(True)
		self.newPass.setVisible(True)
		self.addPass.setVisible(True)

	def closeFile(self):
		self.f.close()
		self.run.setEnabled(True)
		self.stop.setVisible(False)
		self.label.setVisible(False)
		self.label_3.setVisible(False)
		self.newPassIsFrom.setVisible(False)
		self.newPass.setVisible(False)
		self.addPass.setVisible(False)



	def readLoginBtnClick(self):
		if not self.readLogin.text():
			msg = QMessageBox()
			msg.setIcon(msg.icon().Critical)
			msg.setInformativeText("Значение в поле 'Логин' не указано")
			msg.setWindowTitle("Error")
			msg.show()
			msg.exec()
		elif self.readLogin.text() not in open('passwords.txt', 'r').read():
			msg = QMessageBox()
			msg.setIcon(msg.icon().Critical)
			msg.setInformativeText("Пароля по такому ключу нет")
			msg.setWindowTitle("Error")
			msg.show()
			msg.exec()
		else:
			f = open('passwords.txt', 'r').read()
			login = self.readLogin.text()
			a = f.index(login)
			sep = '###@~KEYnPASSWORD~@###23042008BadKonstB'
			strToEnd = f[a::]
			pw = strToEnd[len(login) + len(sep):f.find('\n')]
			self.answer.setText(pw)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	mc = passManager()
	mc.show()
	sys.exit(app.exec())
