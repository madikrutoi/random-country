from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QtWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QLineEdit, QtCore, QListWidget, QtWidgets
import json

app = QApplication([])
window = QtWidget()


main_layout = QHBoxLayout()
line = QVBoxLayout()
line_buttons = QHBoxLayout()

button_add =  QPushButton('Добавить')
button_del = QPushButton('Удалить')
button_save = QPushButton('Сохранить')

line_buttons.addWidget(button_add)
line_buttons.addWidget(button_del)
line_buttons.addWidget(button_save)

countries_info = QTextEdit(button_add)
line.addWidget(countries_info)
line.addLayout(line_buttons)

countries_list = QListWidget()
main_layout.addWidget(countries_list)
main_layout.addLayout

countries_edit = QLineEdit()
countries_edit.setPlaceholderText('Введите страну...')
line.addWidget(countries_edit)

with open('countries.json', 'r') as file:
    countries = json.load(file)
    for country in countries:
        countries_list.addIthem(country)

def info_country():
    with open('coutries,json', 'r') as file:
        countries = json.load(file)
    country = countries_list.selectedItems()[0].text()
    countries_info.setText(countries[country])

def add_country():
    country = countries_edit.text()
    with open('countries.json', 'r') as file:
        countries = json.load(file)
    countries[country] = ''
    with open('countries.json', 'w') as file:
        countries = json.dump(count,file)
    countries_info.clear()
    countries_list.addItem(country)

def edit_country():
    country = ''
    if countries_list.selectedItems()[0].text():
         country = countries_list.selectedItems()[0].text()
    with open('countries.json', 'r') as file:
        countries = json.load(file)
    countries[country] = countries_info.to_PlainText()
    with open('countries.json', 'w') as file:
        countries = json.dump(countries, file)
    countries_info.clear()


    def del_country():
        country = ''
        if coutries_list.selectedItems()[0].text():
            country = countries_list.selectedItems()[0].text()
        with open('countries.json', 'r') as file:
            countries = json.load(file)
        del countries[countries]
        with open('countries.json', 'w') as file:
            countries = json.dump(countries,file)
        with open('countries.json', 'r') as file:
            countries = json.load(file)
        countries_list.clear()
        countries_info.clear()
        for country in countries:
            countries_list.addIthem(country)



countries_list.itemClicked.connect(info_country)
button_add.clicked.connect(add_country)
button_del.clicked.connect(del_country)
button_save.clicked.connect(edit_country)

window.setLayout(main_layout)
window.show()
app.exec()
