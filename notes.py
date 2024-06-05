from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit
from PyQt5.QtWidgets import QLineEdit, QListWidget, QInputDialog, QMessageBox
from PyQt5.QtGui import QIcon
import json


'''_dict_ = {
    'Добро пожаловать!':
    {'текст' : 'В этом приложении можно создавать заметки с тегами',
    'теги' : ['умные заметки', 'инструкция']}
}

with open('notes.json', 'w') as file:
    json.dump(_dict_, file)
'''


#работа с заметками
def del_note():  #удалить заметку
    if list_1.selectedItems():
        name = list_1.selectedItems()[0].text()
        del _dict_[name]
        list_1.clear()
        list_2.clear()
        list_0.clear()
        list_1.addItems(_dict_)
    else:
        win_err = QMessageBox()  
        win_err.setText('Вы не выбрали заметку!') 
        win_err.setWindowTitle('Ошибка')  
        win_err.setIcon(QMessageBox.Critical)
        win_err.setWindowIcon(QIcon('error.png'))
        win_err.exec_()
        
def save_note():  #сохранить заметку
    if list_1.selectedItems():
        name = list_1.selectedItems()[0].text()
        text = list_0.toPlainText()
        _dict_[name]['текст'] = text
        win_inf = QMessageBox()  
        win_inf.setText('Заметка сохранена!') 
        win_inf.setWindowTitle('Сохранение заметки')  
        win_inf.setIcon(QMessageBox.Information)
        win_inf.setWindowIcon(QIcon('ok.png'))
        win_inf.exec_()
    else:
        win_err = QMessageBox()  
        win_err.setText('Вы не выбрали заметку!') 
        win_err.setWindowTitle('Ошибка')  
        win_err.setIcon(QMessageBox.Critical)
        win_err.setWindowIcon(QIcon('error.png'))
        win_err.exec_()
          
def add_note():  #создать заметку
    name_note_win = QInputDialog()
    main_win.setStyleSheet("background: rgb(255,255,255)")
    main_win.hide()
    note_name, result = name_note_win.getText(main_win, 'Создание заметки', 'Название заметки')
    if result and note_name != '':
        _dict_[note_name] = {'текст':'', 'теги':[]}
        list_1.addItem(note_name)
    elif note_name == '' and result != False:
        win_err = QMessageBox()  
        win_err.setText('Вы не ввели название заметки!') 
        win_err.setWindowTitle('Ошибка')  
        win_err.setIcon(QMessageBox.Critical)
        win_err.setWindowIcon(QIcon('error.png'))
        win_err.exec_()
    main_win.setStyleSheet('background: rgb(128, 24, 232)')
    main_win.show()

def show_note():  #показать текст
    name = list_1.selectedItems()[0].text()
    list_0.setText(_dict_[name]['текст'])
    list_2.clear()
    list_2.addItems(_dict_[name]['теги'])


#работа с тегами
def add_tag():  #добавить тег
    if list_1.selectedItems():
        key = list_1.selectedItems()[0].text()
        tag = line.text()
        if tag != '' and not tag in _dict_[key]['теги']:
            _dict_[key]['теги'].append(tag)
            list_2.addItem(tag)
            line.clear()
        elif tag in _dict_[key]['теги']:
            win_err = QMessageBox()  
            win_err.setText('Такой тег уже добавлен!') 
            win_err.setWindowTitle('Ошибка')  
            win_err.setIcon(QMessageBox.Critical)
            win_err.setWindowIcon(QIcon('error.png'))
            win_err.exec_()  
        else:
            win_err = QMessageBox()  
            win_err.setText('Вы не ввели тег!') 
            win_err.setWindowTitle('Ошибка!')  
            win_err.setIcon(QMessageBox.Critical)
            win_err.setWindowIcon(QIcon('error.png'))
            win_err.exec_()    
    else:
        win_err = QMessageBox()  
        win_err.setText('Вы не выбрали заметку!') 
        win_err.setWindowTitle('Ошибка')  
        win_err.setIcon(QMessageBox.Critical)
        win_err.setWindowIcon(QIcon('error.png'))
        win_err.exec_()
        
def del_tag():  #удалить тег
    if list_1.selectedItems():
        if list_2.selectedItems():
            name_note = list_1.selectedItems()[0].text()
            name_tag = list_2.selectedItems()[0].text()
            _dict_[name_note]['теги'].remove(name_tag)
            list_2.clear()
            list_2.addItems(_dict_[name_note]['теги'])
        else:
            win_err = QMessageBox()  
            win_err.setText('Вы не выбрали тег!') 
            win_err.setWindowTitle('Ошибка')  
            win_err.setIcon(QMessageBox.Critical)
            win_err.setWindowIcon(QIcon('error.png'))
            win_err.exec_()
    else:
        win_err = QMessageBox()  
        win_err.setText('Вы не выбрали заметку!') 
        win_err.setWindowTitle('Ошибка')  
        win_err.setIcon(QMessageBox.Critical)
        win_err.setWindowIcon(QIcon('error.png'))
        win_err.exec_()
           
def search_tag():  #искать по тегу
    tag = line.text()
    if butt_6.text() == 'Искать заметки по тегу' and tag:
        notes_filtred = {}
        for note in _dict_:
            if tag in _dict_[note]['теги']:
                notes_filtred[note] = _dict_[note]
        if notes_filtred == {}:
            win_err = QMessageBox()  
            win_err.setText('По такому тегу заметок нет') 
            win_err.setWindowTitle('Поиск заметок')  
            win_err.setIcon(QMessageBox.Information)
            win_err.setWindowIcon(QIcon('info.png'))
            win_err.exec_()   
        else:         
            butt_6.setText('Сбросить поиск')
            list_1.clear()
            list_2.clear()
            list_1.addItems(notes_filtred)
    elif butt_6.text() == 'Сбросить поиск':
        line.clear()
        list_1.clear()
        list_2.clear()
        list_1.addItems(_dict_)
        butt_6.setText('Искать заметки по тегу')
    else:
        win_err = QMessageBox()  
        win_err.setText('Вы не ввели тег!') 
        win_err.setWindowTitle('Ошибка')  
        win_err.setIcon(QMessageBox.Critical)
        win_err.setWindowIcon(QIcon('error.png'))
        win_err.exec_()
        

#подготовка приложения
app = QApplication([])
main_win = QWidget()
main_win.resize(900,700)
main_win.setWindowTitle('Умные заметки')
main_win.setWindowIcon(QIcon('im.png'))
main_win.setStyleSheet('background: rgb(128, 24, 232)')

#виджеты
#левая половина
list_0 = QTextEdit()
list_0.setStyleSheet('background: rgb(255, 255, 255)')
#правая половина
lab_1 = QLabel('Список заметок')
list_1 = QListWidget()
list_1.setStyleSheet('background: rgb(255,255,255)')
butt_1 = QPushButton('Создать заметку')
butt_1.setStyleSheet('background: rgb(245, 237, 56)')
butt_2 = QPushButton('Удалить заметку')
butt_2.setStyleSheet('background: rgb(245, 237, 56)')
butt_3 = QPushButton('Сохранить заметку')
butt_3.setStyleSheet('background: rgb(245, 237, 56)')
lab_2 = QLabel('Список тегов')
list_2 = QListWidget()
list_2.setStyleSheet('background: rgb(255, 255, 255)')
line = QLineEdit()
line.setPlaceholderText('Введите тег...')
line.setStyleSheet('background: rgb(255, 255, 255)')
butt_4 = QPushButton('Добавить к заметке')
butt_4.setStyleSheet('background: rgb(245, 237, 56)')
butt_5 = QPushButton('Открепить от заметки')
butt_5.setStyleSheet('background: rgb(245, 237, 56)')
butt_6 = QPushButton('Искать заметки по тегу')
butt_6.setStyleSheet('background: rgb(245, 237, 56)')

#layouts
left_layout = QVBoxLayout()
right_layout = QVBoxLayout()
note_layout = QHBoxLayout()
teg_layout = QHBoxLayout()
main_layout = QHBoxLayout() 

#прикрепление к layout
left_layout.addWidget(list_0)
right_layout.addWidget(lab_1)
right_layout.addWidget(list_1)
note_layout.addWidget(butt_1)
note_layout.addWidget(butt_2)
right_layout.addLayout(note_layout)
right_layout.addWidget(butt_3)
right_layout.addWidget(lab_2)
right_layout.addWidget(list_2)
right_layout.addWidget(line)
teg_layout.addWidget(butt_4)
teg_layout.addWidget(butt_5)
right_layout.addLayout(teg_layout)
right_layout.addWidget(butt_6)
main_layout.addLayout(left_layout)
main_layout.addLayout(right_layout)


#подключение обработки событий
list_1.itemClicked.connect(show_note)
butt_1.clicked.connect(add_note)
butt_2.clicked.connect(del_note)
butt_3.clicked.connect(save_note)
butt_4.clicked.connect(add_tag)
butt_5.clicked.connect(del_tag)
butt_6.clicked.connect(search_tag)


#прикрепление главного layout к окну
main_win.setLayout(main_layout)


with open('notes.json', 'r') as file:
    _dict_ = json.load(file)
list_1.addItems(_dict_)  
  
main_win.show()
app.exec_()

with open('notes.json', 'w') as file:
    json.dump(_dict_, file)
