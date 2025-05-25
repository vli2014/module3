from flask import Flask
import random

facts_list = ["Одиннадцать процентов людей на земле левши.", "Люди теряют около шестиста тысяч частиц кожи каждый час.", "Виноград взрывается в микроволновой печи."]
app = Flask(__name__)
symbols = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890~!@$"

@app.route("/")
def home():
    return f'<h1>Главная страница</h1>\n<a href="/random_fact">Посмотреть случайный факт!</a>'
@app.route("/random_fact")
def random_fact():
    return f'<h3>Ваш рандомный факт:</h3>\n<p>{random.choice(facts_list)}</p>'
@app.route("/passgen")
def password_generator():
    password = ""
    for i in range(0, 10):
        password+=symbols[random.randint(0, 55)]
    return f'<h1>Генератор паролей</h1>\n<p>Ваш пароль: {password}</p>'


app.run(debug=True)