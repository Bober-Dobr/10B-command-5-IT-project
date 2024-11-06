# -*- coding: utf-8 -*-
import sys
from threading import settrace
from screeninfo import get_monitors
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import QRegularExpression, Qt
from PyQt6.QtGui import QRegularExpressionValidator, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QWidget, QInputDialog
from pymorphy3 import MorphAnalyzer
import datetime
import math


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1210, 892)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.groupBox.setObjectName("groupBox")
        self.dreamName = QtWidgets.QLabel(parent=self.groupBox)
        self.dreamName.setGeometry(QtCore.QRect(30, 190, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dreamName.setFont(font)
        self.dreamName.setObjectName("dreamName")
        self.progressBar = QtWidgets.QProgressBar(parent=self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(30, 220, 391, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.setDream = QtWidgets.QPushButton(parent=self.groupBox)
        self.setDream.setGeometry(QtCore.QRect(30, 260, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setDream.setFont(font)
        self.setDream.setObjectName("setDream")
        self.piggy = QtWidgets.QLCDNumber(parent=self.groupBox)
        self.piggy.setGeometry(QtCore.QRect(30, 80, 191, 41))
        self.piggy.setObjectName("piggy")
        self.rub_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.rub_2.setGeometry(QtCore.QRect(240, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rub_2.setFont(font)
        self.rub_2.setObjectName("rub_2")
        self.dreamInp = QtWidgets.QLineEdit(parent=self.groupBox)
        self.dreamInp.setGeometry(QtCore.QRect(310, 270, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dreamInp.setFont(font)
        self.dreamInp.setObjectName("dreamInp")
        self.dreamCost = QtWidgets.QLineEdit(parent=self.groupBox)
        self.dreamCost.setGeometry(QtCore.QRect(310, 310, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dreamCost.setFont(font)
        self.dreamCost.setObjectName("dreamCost")
        self.setDreamConf = QtWidgets.QPushButton(parent=self.groupBox)
        self.setDreamConf.setGeometry(QtCore.QRect(360, 350, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setDreamConf.setFont(font)
        self.setDreamConf.setObjectName("setDreamConf")
        self.breakPiggyBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.breakPiggyBtn.setGeometry(QtCore.QRect(30, 140, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.breakPiggyBtn.setFont(font)
        self.breakPiggyBtn.setObjectName("breakPiggyBtn")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 270, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(250, 310, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.rub_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.rub_7.setGeometry(QtCore.QRect(510, 320, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rub_7.setFont(font)
        self.rub_7.setObjectName("rub_7")
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.sumInp = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.sumInp.setGeometry(QtCore.QRect(30, 120, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sumInp.setFont(font)
        self.sumInp.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.sumInp.setText("")
        self.sumInp.setObjectName("sumInp")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 50, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.addInpSum = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.addInpSum.setGeometry(QtCore.QRect(30, 180, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addInpSum.setFont(font)
        self.addInpSum.setObjectName("addInpSum")
        self.addOutSum = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.addOutSum.setGeometry(QtCore.QRect(170, 180, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addOutSum.setFont(font)
        self.addOutSum.setObjectName("addOutSum")
        self.rub_1 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.rub_1.setGeometry(QtCore.QRect(240, 130, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rub_1.setFont(font)
        self.rub_1.setObjectName("rub_1")
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.sincePeriod = QtWidgets.QDateEdit(parent=self.groupBox_4)
        self.sincePeriod.setGeometry(QtCore.QRect(60, 90, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sincePeriod.setFont(font)
        self.sincePeriod.setObjectName("sincePeriod")
        self.forPeriod = QtWidgets.QDateEdit(parent=self.groupBox_4)
        self.forPeriod.setGeometry(QtCore.QRect(210, 90, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.forPeriod.setFont(font)
        self.forPeriod.setObjectName("forPeriod")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(40, 80, 47, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(180, 80, 47, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.periodConf = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.periodConf.setGeometry(QtCore.QRect(350, 90, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.periodConf.setFont(font)
        self.periodConf.setObjectName("periodConf")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(50, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(50, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.LCDin = QtWidgets.QLCDNumber(parent=self.groupBox_4)
        self.LCDin.setGeometry(QtCore.QRect(160, 140, 111, 31))
        self.LCDin.setObjectName("LCDin")
        self.LCDout = QtWidgets.QLCDNumber(parent=self.groupBox_4)
        self.LCDout.setGeometry(QtCore.QRect(160, 180, 111, 31))
        self.LCDout.setObjectName("LCDout")
        self.rub_4 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.rub_4.setGeometry(QtCore.QRect(290, 150, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rub_4.setFont(font)
        self.rub_4.setObjectName("rub_4")
        self.rub_5 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.rub_5.setGeometry(QtCore.QRect(290, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rub_5.setFont(font)
        self.rub_5.setObjectName("rub_5")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(50, 220, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.LCDpiggy = QtWidgets.QLCDNumber(parent=self.groupBox_4)
        self.LCDpiggy.setGeometry(QtCore.QRect(160, 220, 111, 31))
        self.LCDpiggy.setObjectName("LCDpiggy")
        self.rub_6 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.rub_6.setGeometry(QtCore.QRect(290, 230, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rub_6.setFont(font)
        self.rub_6.setObjectName("rub_6")
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.mainAccount = QtWidgets.QLCDNumber(parent=self.groupBox_3)
        self.mainAccount.setGeometry(QtCore.QRect(30, 50, 231, 61))
        self.mainAccount.setObjectName("mainAccount")
        self.rub_3 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.rub_3.setGeometry(QtCore.QRect(280, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rub_3.setFont(font)
        self.rub_3.setObjectName("rub_3")
        self.fiillPiggy = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.fiillPiggy.setGeometry(QtCore.QRect(30, 130, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fiillPiggy.setFont(font)
        self.fiillPiggy.setObjectName("fiillPiggy")
        self.fillPiggySum = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.fillPiggySum.setGeometry(QtCore.QRect(220, 130, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fillPiggySum.setFont(font)
        self.fillPiggySum.setObjectName("fillPiggySum")
        self.fillPiggyConf = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.fillPiggyConf.setGeometry(QtCore.QRect(260, 170, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fillPiggyConf.setFont(font)
        self.fillPiggyConf.setObjectName("fillPiggyConf")
        self.rub_8 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.rub_8.setGeometry(QtCore.QRect(350, 140, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rub_8.setFont(font)
        self.rub_8.setObjectName("rub_8")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(150, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.autoFill = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.autoFill.setGeometry(QtCore.QRect(40, 220, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.autoFill.setFont(font)
        self.autoFill.setObjectName("autoFill")
        self.changeAutoFillBtn = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.changeAutoFillBtn.setGeometry(QtCore.QRect(60, 260, 231, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.changeAutoFillBtn.setFont(font)
        self.changeAutoFillBtn.setObjectName("changeAutoFillBtn")
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1210, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Money Calculator"))
        self.groupBox.setTitle(_translate("MainWindow", "Моя мечта"))
        self.dreamName.setText(_translate("MainWindow", "Мечта не задана"))
        self.label_4.setText(_translate("MainWindow", "В копилке:"))
        self.setDream.setText(_translate("MainWindow", "Установить/поменять\n"
"мечту"))
        self.rub_2.setText(_translate("MainWindow", "рублей"))
        self.setDreamConf.setText(_translate("MainWindow", "Установить мечту"))
        self.breakPiggyBtn.setText(_translate("MainWindow", "Разбить копилку и купить мечту"))
        self.label_2.setText(_translate("MainWindow", "Название:"))
        self.label_3.setText(_translate("MainWindow", "Цена:"))
        self.rub_7.setText(_translate("MainWindow", "рублей"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Доходы и расходы"))
        self.label.setText(_translate("MainWindow", "Введите сумму дохода/расхода:"))
        self.addInpSum.setText(_translate("MainWindow", "Добавить\n"
"доход"))
        self.addOutSum.setText(_translate("MainWindow", "Добавить\n"
"расход"))
        self.rub_1.setText(_translate("MainWindow", "рублей"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Анализ Финансов"))
        self.label_7.setText(_translate("MainWindow", "Выберите период:"))
        self.label_8.setText(_translate("MainWindow", "С"))
        self.label_9.setText(_translate("MainWindow", "по"))
        self.periodConf.setText(_translate("MainWindow", "Применить"))
        self.label_10.setText(_translate("MainWindow", "Доходов:"))
        self.label_11.setText(_translate("MainWindow", "Расходов:"))
        self.rub_4.setText(_translate("MainWindow", "рублей"))
        self.rub_5.setText(_translate("MainWindow", "рублей"))
        self.label_14.setText(_translate("MainWindow", "Отложено:"))
        self.rub_6.setText(_translate("MainWindow", "рублей"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Основной счёт"))
        self.rub_3.setText(_translate("MainWindow", "рублей"))
        self.fiillPiggy.setText(_translate("MainWindow", "Пополнить\n"
"копилку"))
        self.fillPiggyConf.setText(_translate("MainWindow", "Пополнить"))
        self.rub_8.setText(_translate("MainWindow", "рублей"))
        self.label_5.setText(_translate("MainWindow", "Сумма:"))
        self.autoFill.setText(_translate("MainWindow", "Автопополнение копилки (15% от суммы дохода)"))
        self.changeAutoFillBtn.setText(_translate("MainWindow", "Изменить сумму автопополнения"))


class MoneyCalc(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.morph = MorphAnalyzer()

        self.w = None
        # Получаем высоту и ширину экрана для последующей работы с поздравительным окном
        self.width = get_monitors()[0].width
        self.height = get_monitors()[0].height


        self.changeAutoFillBtn.clicked.connect(self.changeAutoFill)

        # Устанавливаем валидатор на поле ввода суммы дохода/расхода, пропускающий только цифры
        self.sumInp.setValidator(QRegularExpressionValidator(QRegularExpression(r'\d+')))
        # Привязываем к сигналу изменения текста в поле ввода суммы функцию textEdit, согласующую число в поле ввода с текстом на лейбле
        self.sumInp.textEdited.connect(self.textEdit)

        # Привязываем к нажатию кнопки изменения мечты ф-цию setDreamClicked, отвечающую за видимость определенных виджетов
        self.setDream.clicked.connect(self.setDreamClicked)

        # Привязываем к нажатию кнопки подтверждения изменения мечты ф-цию setDreamConfClicked, отвечающую за запись новых данных в БД
        self.setDreamConf.clicked.connect(self.setDreamConfClicked)

        # Валидатор на пропуск только цифр в поле ввода стоимости мечты
        self.dreamCost.setValidator(QRegularExpressionValidator(QRegularExpression(r'\d+')))
        # Привязываем к изменению числа в поле ввода стоимости мечты ф-цию textEdit, отвечающую за согласование числа с текстом на лейбле рядом с ним
        self.dreamCost.textEdited.connect(self.textEdit)

        # Привязываем нажатие кнопки "Разбить копилку" к ф-ции, разбивающей копилку и тратящей деньги
        self.breakPiggyBtn.clicked.connect(self.breakPiggy)

        # Привязываем к сигналу изменения параметра isChecked() функцию, записывающую в базу данных data.txt новое состояние чекбокса autoFill
        self.autoFill.stateChanged.connect(self.autoFillChecked)

        self.fillPiggySum.textEdited.connect(self.textEdit)

        # Скрываем кнопки пополнения копилки при создании приложения
        self.fillPiggyConf.setVisible(False)
        self.fillPiggySum.setVisible(False)
        self.label_5.setVisible(False)
        self.rub_8.setVisible(False)
        # Устанавливаем валиатор, пропускающий только цифры, на поле ввода суммы пополнения копилки
        self.fillPiggySum.setValidator(QRegularExpressionValidator(QRegularExpression(r'\d+')))
        # Привязываем к нажатию кнопки пополнения копилки ф-цию, отвечающую за пополнение копилки, запись данных в БД
        self.fillPiggyConf.clicked.connect(self.fillPiggy)
        # Привязываем к нажатию кнопки пополнения копилки ф-цию, отвечающую за видимость определенных виджетов
        self.fiillPiggy.clicked.connect(self.fillPiggyButton)

        # Привязываем к нажатию каждой из кнопок добавления дохода/расхода ф-йию, отвечающую за добавление денег на счет, в копилку/списания денег со счета, из копилки, занесения данных в БД
        self.addInpSum.clicked.connect(self.add_remove_money)
        self.addOutSum.clicked.connect(self.add_remove_money)

        # Определяем первую дату запуска приложения
        calendar = open('calendar.txt', 'r').readlines()
        if calendar:
            fd = calendar[0][:11].split('-')
            date = datetime.date(int(fd[0]), int(fd[1]), int(fd[2]))
        else:
            date = datetime.date.today()
            open('calendar.txt', 'w').write(str(f'{date}\n'))
        # Устанавливаеем минимальные и макимальные даты для виджетов выбора даты. ДАТЫ СЧИТАЕМ ВКЛЮЧИТЕЛЬНО
        self.sincePeriod.setMinimumDate(date)
        self.sincePeriod.setMaximumDate(datetime.date.today())
        self.forPeriod.setMinimumDate(date)
        self.forPeriod.setMaximumDate(datetime.date.today())

        # Привязываем к нажатию кнопки выбора даты ф-цию, анализирующую доходы/расходы за выбранный период
        self.periodConf.clicked.connect(self.analyzePeriod)

        # устанавливаем значения из базы данных на все виджеты, для которых хранятся значения
        self.setNames()

    def changeAutoFill(self):
        # Получаем значение из поля ввода числа и статус кнопки Ok (была ли нажата)
        summ, ok = QInputDialog.getInt(self, 'Введите целое число', 'Введите, какой процент от дохода хотите автоматически класть в копилку', 15, 1, 99)
        if ok:
            # Записываем в БД новое значение параметра autoFill, т.е. на какой процент будет пополняться копилка с каждым поступлением денежных средств
            data = open('data.txt', 'r').readlines()
            temp = []
            for i in data:
                if 'autoFill' not in i:
                    temp.append(i)
            data = open('data.txt', 'w')
            for i in temp:
                data.write(i)
            data.write(f'autoFill = {summ}\n')
            data.close()
            # Обновляем значения
            self.setNames()

    def autoFillChecked(self):
        # При изменении параметра isChecked() записываем в БД новое состояние чекбокса
        data = open('data.txt', 'r').readlines()
        temp = []
        for i in data:
            if 'afBool' not in i:
                temp.append(i)
        data = open('data.txt', 'w')
        for i in temp:
            data.write(i)
        data.write(f'afBool = {self.autoFill.isChecked()}\n')
        data.close()

    def breakPiggy(self):
        # Вызывается по нажатию на кнопку "Разбить копилку"
        data = open('data.txt', 'r').read()
        # Проверяем, что накопили нужную сумму
        if self.checkProgress(data, who='break'):
            ind = data.index('dreamCost = ')
            indl = (data[ind::]).find('\n') + ind
            dreamCostStr = int(data[ind + len('dreamCost = '):indl])
            # В календарь событий записываем списание с копилки суммы, равной цене мечты. Ту же сумму записываем в траты в календарь событий
            self.calendarWrite(dreamCostStr, '&-')
            self.calendarWrite(dreamCostStr, '-')
            # Записываем новые значения параметров inPiggy, dreamCost, dreamName в БД
            temp = []
            for i in data.split('\n'):
                if not ('inPiggy' in i or'dreamCost' in i or 'dreamName' in i) and i:
                    temp.append(f'{i}\n')
            data = open('data.txt', 'w')
            for i in temp:
                data.write(i)
            data.write(f'inPiggy = {self.piggy.intValue() - dreamCostStr}\n')
            data.write('dreamCost = 0\n')
            data.write('dreamName = Мечта не задана\n')
            data.close()
            # Обновляем значения
            self.setNames()
        # Если сумма не накоплена, высвечивается Инфо-бокс с советом
        else:
            msg = QMessageBox()
            msg.setIcon(msg.icon().Information)
            msg.setWindowTitle('Совет')
            msg.setInformativeText('Не спешите! Вы ещё не накопили')
            msg.show()
            msg.exec()

    def analyzePeriod(self):
        # Считываем значения из календаря событий
        calendar = open('calendar.txt', 'r').readlines()
        if calendar:
            # Получаем даты начала и окончания периода анализа
            date1 = self.sincePeriod.date()
            date2 = self.forPeriod.date()
            # Инициализируем переменные plus, minus, saved, отвечающие за доход, расход и отложенную сумму за период анализа
            plus = 0
            minus = 0
            saved = 0
            # Проходим по всем записям в каледаре событий
            for i in calendar:
                # Получаем дату из каждой записи
                ymd = list(map(int, i[:11].split('-')))
                date = datetime.date(ymd[0], ymd[1], ymd[2])
                # Если полученная дата находится в периоде анализа...
                if date1 <= date <= date2:
                    # ... "Отрезаем" часть строки, где записана дата
                    s = i[11::]
                    # Создаем список всех действий за полученную дату
                    actions = s.split()
                    # Проходим по всем действиям за полученную дату
                    for j in actions:
                        # Если действие не связано с копилкой...
                        if '&' not in j:
                            # ... Прибавляем к доходам или вычитаем из расходов сумму дохода/расхода в зависимости от ее знака
                            if int(j) > 0:
                                plus += int(j)
                            else:
                                minus -= int(j)
                        # Если же действие производилось с копилкой, то вычитаем/прибавляем сумму, внесенную/взятую в копилку/из копилки
                        else:
                            saved += int(j[1::])
            # Выводим полученные значения в соответствующие дисплеи
            self.LCDin.display(plus)
            self.LCDout.display(minus)
            self.LCDpiggy.display(saved)
            # Согласуем тексты на лейблах со значениями чисел на каждом из дисплеев
            self.makeAgree('LCDin')
            self.makeAgree('LCDout')
            self.makeAgree('LCDpiggy')
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Предупреждение!')
            msg.setIcon(msg.icon().Warning)
            msg.setInformativeText('Пока что нет данных о доходах/расходах')
            msg.show()
            msg.exec()

    def textEdit(self):
        # Согласуем значение текста лейбла и числа в поле ввода. Каждому полю ввода - свой лейбл
        if self.sender() is self.sumInp and self.sumInp.text():
            self.rub_1.setText(self.morph.parse('рубль')[0].make_agree_with_number(int(self.sumInp.text())).word)
        elif self.sender() is self.dreamCost and self.dreamCost.text():
            self.rub_7.setText(self.morph.parse('рубль')[0].make_agree_with_number(int(self.dreamCost.text())).word)
        elif self.sender() is self.fillPiggySum and self.fillPiggySum.text():
            self.rub_8.setText(self.morph.parse('рубль')[0].make_agree_with_number(int(self.fillPiggySum.text())).word)

    def makeAgree(self, who):
        # Согласуем значение текста лейбла и числа на дисплее. Каждому дисплею - свой лейбл
        if who == 'piggy':
            self.rub_2.setText(self.morph.parse('рубль')[0].make_agree_with_number(self.piggy.intValue()).word)
        elif who == 'mainAccount':
            self.rub_3.setText(self.morph.parse('рубль')[0].make_agree_with_number(self.mainAccount.intValue()).word)
        elif who == 'LCDin':
            self.rub_4.setText(self.morph.parse('рубль')[0].make_agree_with_number(self.LCDin.intValue()).word)
        elif who == 'LCDout':
            self.rub_5.setText(self.morph.parse('рубль')[0].make_agree_with_number(self.LCDout.intValue()).word)
        elif who == 'LCDpiggy':
            self.rub_6.setText(self.morph.parse('рубль')[0].make_agree_with_number(self.LCDpiggy.intValue()).word)

    def setDreamClicked(self):
        # Прячем или показываем виджеты по нажатию на кнопку
        self.dreamInp.setVisible(not self.dreamInp.isVisible())
        self.setDreamConf.setVisible(not self.setDreamConf.isVisible())
        self.dreamCost.setVisible(not  self.dreamCost.isVisible())
        self.label_3.setVisible(not self.label_3.isVisible())
        self.label_2.setVisible(not self.label_2.isVisible())
        self.rub_7.setVisible(not self.rub_7.isVisible())

    def setDreamConfClicked(self):
        # Используем конструкцию try-except, чтобы сразу выявить некорректный пользовательский ввод
        try:
            # p и p1 - заглушки, вызывающие ошибку при неправильном пользовательском вводе
            p = self.dreamInp.text()[0]
            p1 = int(self.dreamCost.text())
            # Записываем в БД параметры dreamCost и dreamName
            f = open('data.txt', 'r')
            temp = []
            for i in f.readlines():
                if not ('dreamCost' in i or "dreamName" in i):
                    temp.append(f'{i}')
            temp.append(f'dreamCost = {int(self.dreamCost.text())}\n')
            temp.append(f'dreamName = {self.dreamInp.text()}\n')
            f = open('data.txt', 'w')
            for i in temp:
                f.write(i)
            f.close()
            # Прячем лишние виджеты, которые не понадобятся нам в ближайшее время
            self.dreamInp.setVisible(False)
            self.dreamInp.setText('')
            self.dreamCost.setVisible(False)
            self.dreamCost.setText('')
            self.setDreamConf.setVisible(False)
            self.label_3.setVisible(False)
            self.label_2.setVisible(False)
            self.rub_7.setVisible(False)
            # Обновляем значения
            self.setNames()
            self.checkProgress(open('data.txt', 'r').read())
        # Если в заглушке р что-то сломалось, то это могло быть только из-за того, что указано пустое значение в поле ввода названия мечты
        except IndexError:
            # Показываем сообщение об ошибке
            msg = QMessageBox()
            msg.setIcon(msg.icon().Critical)
            msg.setInformativeText("Введите название мечты")
            msg.setWindowTitle("Error")
            msg.show()
            msg.exec()
        # Если в заглушке р1 что-то сломалось, то это могло быть только из-за того, что указано пустое значение в поле ввода цены мечты
        except ValueError:
            # Показываем сообщение об ошибке
            msg = QMessageBox()
            msg.setIcon(msg.icon().Critical)
            msg.setInformativeText("Указана некорректная цена")
            msg.setWindowTitle("Error")
            msg.show()
            msg.exec()

    def setNames(self):
        # Открываем БД
        data = open('data.txt', 'r').read()
        # Считываем название мечты
        ind = data.index('dreamName = ')
        indl = (data[ind::]).find('\n') + ind
        name = data[ind + len('dreamName = '):indl]
        # Записываем полученное название в соответсвующий лейбл
        self.dreamName.setText(name)
        # Если пользователь задал название и цену мечты (одно без другого не существует), то нет логики предлагать пользователю сразу поменять мечту. Поэтому скрываем ненужные виджеты
        if name != 'Мечта не задана':
            self.dreamInp.setVisible(False)
            self.dreamCost.setVisible(False)
            self.setDreamConf.setVisible(False)
            self.label_3.setVisible(False)
            self.label_2.setVisible(False)
            self.rub_7.setVisible(False)

        # Считываем сумму в копилке
        ind = data.index('inPiggy = ')
        indl = (data[ind::]).find('\n') + ind
        inPiggyStr = int(data[ind + len('inPiggy = '):indl])
        # Устанавливаем на соответсвующий дисплей сумму, которая лежит в копилке
        self.piggy.display(inPiggyStr)
        # Согласуем эту сумму с лейблом
        self.makeAgree('piggy')

        #  Считываем цену мечты
        ind = data.index('dreamCost = ')
        indl = (data[ind::]).find('\n') + ind
        dreamCostStr = int(data[ind + len('dreamCost = '):indl])
        #  Если цена указана, т.е. не равна нулю, то ставим в прогресс-бар процент накопления
        if dreamCostStr != 0:
            self.progressBar.setValue(math.ceil((self.piggy.intValue() / dreamCostStr) * 100))
        # Если цена не указана, то прогресс-бар не работает. Ставим 0
        else:
            self.progressBar.setValue(0)

        # Считываем сумму на основном счету
        ind = data.index('mainAcc = ')
        indl = (data[ind::]).find('\n') + ind
        mainAccStr = int(data[ind + len('mainAcc = '):indl])
        # Устанавливаем на соответсвующий дисплей сумму, которая лежит на основном счету
        self.mainAccount.display(mainAccStr)
        # Согласуем эту сумму с лейблом
        self.makeAgree('mainAccount')

        # Считываем, какой процент нужно откладывать в копилку с каждого дохода
        ind = data.index('autoFill = ')
        indl = (data[ind::]).find('\n') + ind
        autoFillStr = data[ind + len('autoFill = '):indl]
        # Ставим это значение в описание чекбокса
        self.autoFill.setText(f'Автопополнение копилки ({autoFillStr}% от суммы дохода)')

        # Считываем логическое значение, чекнут ли чекбокс
        ind = data.index('afBool = ')
        indl = (data[ind::]).find('\n') + ind
        afBoolStr = data[ind + len('afBool = '):indl]
        # В соответствии с полученным значении устанавливаем состояние чекбокса, отвечающего за автопополнение копилки
        self.autoFill.setChecked(afBoolStr == "True")

    def calendarWrite(self, value, action):
        # Получаем сегодняшнюю дату
        today = datetime.date.today()
        # Открываем календдарь событий
        calendar = open('calendar.txt', 'r')
        temp = []
        c = calendar.readlines()
        # Если за сегодня что-то происходило, то дополняем события
        if str(today) in ''.join(c):
            for i in range(len(c) - 1):
                temp.append(f'{c[i]}')
            calendar = open('calendar.txt', 'w')
            for i in temp:
                calendar.write(i)
            calendar.write(f'{c[-1][:-1]} {action}{value}\n')
            calendar.close()
        # Если сегодняшней даты нет в календаре событий, то записываем сегодняшнюю дату и действие
        else:
            open('calendar.txt', 'a').write(f'{str(today)} {action}{value}\n')

    def add_remove_money(self):
        # Если сумма введена
        if self.sumInp.text():
            # Открываем БД
            data = open('data.txt', 'r').read()
            # Получаем нужные значения из виджетов и из БД
            mainAccStr = self.mainAccount.intValue()
            inPiggyStr = self.piggy.intValue()
            ind = data.index('autoFill = ')
            indl = (data[ind::]).find('\n') + ind
            autoFillStr = int(data[ind + len('autoFill = '):indl])
            # Перезаписываем в БД всё, кроме параметров inPiggy, mainAcc, которые нам предстоит изменить
            temp = []
            for i in data.split('\n'):
                if i and not ('mainAcc' in i or 'inPiggy' in i):
                    temp.append(f'{i}\n')
            data = open('data.txt', 'w')
            for i in temp:
                data.write(i)
            # Получаем из поля ввода сумму пополнения или отчисления
            summ = int(self.sumInp.text())
            # Если нужно пополнить
            if self.sender() == self.addInpSum:
                # Если не стоит галочка на автопополнение копилки, то просто закидываем всю сумму на основной счёт
                if not self.autoFill.isChecked():
                    # Записываем в БД обновлённую сумму, лежащую на основном счету, и ту же сумму, лежащую в копилке, что и была до этого
                    data.write(f'mainAcc = {mainAccStr + summ}\n')
                    data.write(f'inPiggy = {inPiggyStr}\n')
                    data.close()
                    # В календарь событий записываем зачисление на основной счёт
                    self.calendarWrite(summ, '+')
                    # Обновляем значения
                    self.setNames()
                # Если галочка на автопополнение копилки всё же стоит, то пополняем на процент, установленный пользователем копилки и оставшуюся сумму кидаем на основной счёт
                else:
                    # Записываем в БД обновлённые значение параметров
                    data.write(f'mainAcc = {mainAccStr + summ - round(summ * autoFillStr / 100)}\n')
                    data.write(f'inPiggy = {inPiggyStr + round(summ * autoFillStr / 100)}\n')
                    data.close()
                    # В календарь заночсим данные о пополнении копилки и основного счёта
                    self.calendarWrite(summ - round(summ * autoFillStr / 100), '+')
                    self.calendarWrite(round(summ * autoFillStr / 100), "&+")
                    # Обновляем значения
                    self.setNames()
            # Если не пополнить, то потратить
            else:
                # Если сумма расхода превышает сумму сумм, находящихся на основном счету и в копилке
                if summ > mainAccStr + inPiggyStr:
                    # Выводим сообщение об ошибке
                    msg = QMessageBox()
                    msg.setIcon(msg.icon().Critical)
                    msg.setWindowTitle('Error')
                    msg.setInformativeText("На счету не хватает денежных средств!")
                    msg.show()
                    msg.exec()
                    # Ничего не меняем в базе данных, операция отклонена
                    data.write(f'mainAcc = {mainAccStr}\n')
                    data.write(f'inPiggy = {inPiggyStr}\n')
                    data.close()
                # Если на основном счету не хватает, но можно занять из копилки
                elif mainAccStr + inPiggyStr >= summ > mainAccStr :
                    # Спрашиваем у пользователя, можно ли взять из копилки
                    msg = QMessageBox()
                    msg.setWindowTitle("Warning")
                    msg.setIcon(msg.icon().Warning)
                    msg.setText("На счету недостаточно средств! Взять из копилки?")
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
                    msg.show()
                    # Получаем ответ
                    button = msg.exec()
                    # Если ок
                    if button == QMessageBox.StandardButton.Ok:
                        # Обнуляем основной счет
                        data.write(f'mainAcc = {0}\n')
                        # Вытаскиваем из копилки, сколько не хватает
                        data.write(f'inPiggy = {inPiggyStr - (summ - mainAccStr)}\n')
                        data.close()
                        # Записываем в календарь событий расход в виде все суммы на основном счету, взымание с копилки  нехватающей суммы
                        self.calendarWrite(mainAccStr, '-')
                        self.calendarWrite(summ - mainAccStr, '&-')
                        # Обновляем значения
                        self.setNames()
                    # Если не ок
                    else:
                        # Отклоняем операцию
                        data.write(f'mainAcc = {mainAccStr}\n')
                        data.write(f'inPiggy = {inPiggyStr}\n')
                        data.close()
                # Если на основном счету хватает денег
                else:
                    # Записываем в календарь событий трату с основного счёта
                    self.calendarWrite(summ, '-')
                    # В БД из параметра, содержащего сумму, лежащую на основном счету, вычитаем сумму расхода
                    data.write(f'mainAcc = {mainAccStr - summ}\n')
                    # Копилку не трогаем
                    data.write(f'inPiggy = {inPiggyStr}\n')
                    data.close()
                    # Обновляем значения
                    self.setNames()
            self.sumInp.setText('')
        # В противном случае показываем сообщение об ошибке
        else:
            msg = QMessageBox()
            msg.setIcon(msg.icon().Critical)
            msg.setWindowTitle('Error')
            msg.setInformativeText("Введите сумму!")
            msg.show()
            msg.exec()

    def congratulate(self):
        # Устанавливаем 100% на прогресс-баре
        self.progressBar.setValue(100)
        # Инициализируем объект новой формы с поздравлением, передаем туда название мечты
        self.w = Congratulations(str(self.dreamName.text()))
        # Отображаем окно посередине экрана
        self.w.move(self.width // 2 - 350, self.height // 2 - 300)
        self.w.show()

    def checkProgress(self, data, who=''):
        # Считываем значение с дисплея копилки
        inPiggyStr = self.piggy.intValue()
        # Получаем данные из БД, переданной в качестве аргумента
        ind = data.index('dreamCost = ')
        indl = (data[ind::]).find('\n') + ind
        dreamCostStr = int(data[ind + len('dreamCost = '):indl])
        # Если мы накопили и ф-йия вызвана для вывода окна с поздравлением
        if inPiggyStr >= dreamCostStr and not who:
            # Запускаем функцию поздравления
            self.congratulate()
        # Если мы накопили и не нужно еще раз показывать окно с поздравлением
        elif inPiggyStr >= dreamCostStr and who and inPiggyStr != 0:
            return True

    def fillPiggyButton(self):
        # Скрывает или показывает кнопку пополнения и поле ввода суммы пополнения копилки
        self.fillPiggyConf.setVisible(not self.fillPiggyConf.isVisible())
        self.fillPiggySum.setVisible(not self.fillPiggySum.isVisible())
        self.label_5.setVisible(not self.label_5.isVisible())
        self.rub_8.setVisible(not self.rub_8.isVisible())

    def fillPiggy(self):
        # Если хотим пополнить на бо'льшую сумму, чем есть на основном счету или не указана сумма
        if (not self.fillPiggySum.text()) or int(self.fillPiggySum.text()) > self.mainAccount.intValue() or self.fillPiggySum.text() == '0':
            # Выводим сообщение об ошибке
            msg = QMessageBox()
            msg.setIcon(msg.icon().Critical)
            msg.setInformativeText("Некорректное знаечние для пополнения")
            msg.setWindowTitle("Error")
            msg.show()
            msg.exec()
        # Если все хорошо
        else:
            print(2)
            # Считываем данные из БД
            data = open('data.txt', 'r').read()
            # Считываем значение dreamCostStr
            ind = data.index('dreamCost = ') + len('dreamCost = ')
            dreamCostStr = int(data[ind:ind + data[ind::].index('\n')])
            # Если стоимость мечты больше чем сумма в копилке, т.е. если не накопили, или если мечта не задана
            if dreamCostStr > self.piggy.intValue() or dreamCostStr == 0:
                # Если dreamCostStr равно нулю, т.е. мечта не задана
                if dreamCostStr == 0:
                    # Выводим предупреждение, что прогресс-бар не работает
                    msg = QMessageBox()
                    msg.setIcon(msg.icon().Information)
                    msg.setInformativeText("Стоимость мечты не задана, поэтому прогресс-бар пока не работает :(")
                    msg.setWindowTitle("Важно!")
                    msg.show()
                    msg.exec()
                # Считываем данные из БД
                data = open('data.txt', 'r').read()
                # Считываем значения с виджетов
                mainAccStr = self.mainAccount.intValue()
                inPiggyStr = self.piggy.intValue()
                # Записываем в БД новые значения для параметров mainAcc и inPiggy
                temp = []
                for i in data.split('\n'):
                    if i and not ('mainAcc' in i or 'inPiggy' in i):
                        temp.append(f'{i}\n')
                data = open('data.txt', 'w')
                for i in temp:
                    data.write(i)
                data.write(f'mainAcc = {mainAccStr - int(self.fillPiggySum.text())}\n')
                data.write(f'inPiggy = {inPiggyStr + int(self.fillPiggySum.text())}\n')
                data.close()
                # Обновляем значения
                self.setNames()
                # Записываем в календарь событий пополнение копилки. ПОПОЛНЕНИЕ КОПИЛКИ НЕ СЧИТАЕТСЯ ЗА РАСХОД
                self.calendarWrite(int(self.fillPiggySum.text()), '&+')
                # Скрываем только что использованные виджеты, т.к. нелогично пополнять сразу несколько раз
                self.fillPiggyConf.setVisible(False)
                self.fillPiggySum.setVisible(False)
                self.rub_8.setVisible(False)
                self.label_5.setVisible(False)
                self.fillPiggySum.setText('')
                # Проверяем, вдруг, только что накопили
                if dreamCostStr  !=  0:
                    self.checkProgress(open('data.txt', 'r').read())
            # Иначе, если мы накопили и пытаемся пополнить копилку
            elif self.dreamName.text() != 'Мечта не задана' and dreamCostStr <= self.piggy.intValue() and dreamCostStr != 0:
                # Выводим совет
                msg = QMessageBox()
                msg.setIcon(msg.icon().Information)
                msg.setInformativeText(f"Вы уже накопили на {self.dreamName.text()}. Пора разбить копилку!")
                msg.setWindowTitle("Совет")
                msg.show()
                msg.exec()

    def closeEvent(self, event):
        # При закрытии главного окна, дочернее окно с поздравлением, если оно есть, тоже будет закрыто
        if self.w:
            self.w.close()


class Congratulations(QWidget):
    def __init__(self, dreamName):
        super().__init__()
        self.dreamName = dreamName
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 600)
        self.setWindowTitle('Поздравояем!')
        self.label = QLabel(self)
        self.pixmap = QPixmap('cong.jpg')
        self.label.resize(700, 470)
        self.label.setPixmap(self.pixmap)
        self.label1 = QLabel(self)
        self.label1.move(10, 500)
        self.label1.resize(700, 50)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setStyleSheet("font: 12pt Time New Roman")
        self.label1.setText(f'Поздравляем! Вы накопили на {self.dreamName if self.dreamName != "Мечта не задана" else "вашу мечту"}! Можете разбить копилку')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MoneyCalc()
    mc.showMaximized()
    sys.exit(app.exec())