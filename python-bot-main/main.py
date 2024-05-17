import telebot
import sqlite3

bot = telebot.TeleBot('6786834594:AAFcsb-dKClQL_X0B3R5sbAY0ZedWQRH1lA')

conn = sqlite3.connect('db1.db', check_same_thread=False)
cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Введите вашу фамилию:")

@bot.message_handler(func=lambda message: True)
def check_student(message):
    surname = message.text.strip()

    cursor.execute('SELECT s.f, s.i, s.o, g.name FROM Student s JOIN "Group" g ON s.groupid = g.id WHERE s.f = ?',
                   (surname,))
    students = cursor.fetchone()

    if students:
        response = f"Студент {students[0]} {students[1]} {students[2]} учится в {students[3] } ЗМК."
    else:
        response = "Студент с такой фамилией не найден."

    bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)

