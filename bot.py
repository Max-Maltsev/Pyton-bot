import telebot
import datetime
from random import randint
from PythonProject.Max_login import login
import os.path
from telebot import types
path = os.path.join("data_base", "Bot.txt")
path1 = os.path.join("data_base", "Bot.txt")
config = {
    "name": "Maxxxxxxxxxxxxxbot",
    "token": "5551701270:AAG0EHv0GiQlYbGXcND8HPnK_s6LfERpDvc"
}
max = telebot.TeleBot(config["token"])

@max.message_handler(commands=["start"])

def menu(massage):
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_time = types.KeyboardButton('time🕘')# Кнопка часу
    button_calculator = types.KeyboardButton('calculator🧮')# Кнопка калькулятора
    button_text = types.KeyboardButton('text📄')# Кнопка тексту
    button_sumbolsnumers = types.KeyboardButton('sumbolsnumers1️⃣')# Кнопка рахує символи
    button_happy_ticket = types.KeyboardButton('happy_ticket🎫')# Кнопка видає щаслий / нещасливий білет
    button_countword = types.KeyboardButton('countword📃')# ???
    button_file = types.KeyboardButton('file📁')# Кнопка видає у файлі данні про текст
    button_sun = types.KeyboardButton('sun🌞')# Кнопка визначає залежно від часу нахил сонця
    button_text_maker = types.KeyboardButton('text_maker')
    keybord.add(button_time, button_calculator, button_sumbolsnumers, button_text, button_happy_ticket, button_countword, button_file, button_sun, button_text_maker)
    keybord111 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    text = types.KeyboardButton('text')
    keybord.add(button_time)
    max.send_message(massage.chat.id, "Меню:", reply_markup=keybord111)

@max.message_handler(content_types=['text'])
def start(message):
    if message.text == "text":
        pass
    if message.text == "start":
        max.send_message(message.chat.id, "Мій бот може: привітатись з тобою також може відповісти на (Як справи)")
    if message.text == "time🕘":
        max.send_message(message.chat.id, str(datetime.datetime.now()))# Видає час
    if message.text == "calculator🧮":
        action = max.send_message(message.chat.id, "Enter your action: ") # Обчислює числа
        max.register_next_step_handler(action, calculator)
    if message.text == "sumbolsnumers1️⃣":
        numberstext = max.send_message(message.chat.id, "Enter your text: ")# Видає суму усіх символів
        max.register_next_step_handler(numberstext, numberscount)
    if message.text == "sun🌞":
        numbersun = max.send_message(message.chat.id, "Enter your time: ")# визначає залежно від часу нахил сонця
        max.register_next_step_handler(numbersun, sun)
    # if message.text == "/count":
    #     count = max.send_message(message.chat.id, "Enter your text: ")
    #     max.register_next_step_handler(count, counts)
    if message.text == "text📄":
        text = max.send_message(message.chat.id, "Enter your text: ")# рахує символи
        max.register_next_step_handler(text, count_symbols)
    if message.text == "happy_ticket🎫":
        texthappy = max.send_message(message.chat.id, "Enter your text: ")# видає щаслий / нещасливий білет
        max.register_next_step_handler(texthappy, happy)
    if message.text == "countword📃":
        word = max.send_message(message.chat.id, "Enter your word: ")# ???
        max.register_next_step_handler(word, worddef)
    if message.text == "file📁":
        word = max.send_message(message.chat.id, "Enter your word: ")# видає у файлі данні про текст
        max.register_next_step_handler(word, filedef)
    if message.text == "/play":
        a = randint(1, 100)
        playtext = max.send_message(message.chat.id, "Напишіть цифру:")
    if message.text == "entry":
        word = max.send_message(message.chat.id, "Enter your password/login: ")
        max.register_next_step_handler(word, login)

# def game(massage):
#     a = randint(1,100)
#     for i in range(10):
#         b = int(massage.text)
#         if b == a:
#             max.send_message(massage.chat.id, f"Ви перемогли!  Витрачено {i+1} спроби Так це {a}")
#             if b < a:
#                 max.send_message(massage.chat.id, "Ваша цифра меньша")
#             if b > a:
#                 max.send_message(massage.chat.id, "Ваша цифра більша")
    # max.send_message(massage.chat.id, "lose")
# def counts(massage):
#     massagecount = massage.text.split()
#     massagecount2 = []
#     for i in massagecount:
#          massagecount2.append(int(i))
#         if
# def login(message, word):
#     users = Users.objects.all()
#     word1 = word.split("/")
#     loging = 0
#     for i in users:
#         if i.name == word1[1]:
#             if i.password == word1[0]:
#                 max.send_message(message.chat.id, f'You in account!!!')
#                 loging = "yes"
#             else:
#                 max.send_message(message.chat.id, f'Password Eror!!!')
def numberscount(massage):
    massagefor = []
    for i in massage.text:
        massagefor.append(int(i))
    max.send_message(massage.chat.id,  f'сума цифр {massage.text} = {str(sum(massagefor))}')
def happy(massage):
    sum1 = 0
    sum2 = 0
    mid = int(len(massage.text)/2)
    happy = massage.text[:mid]
    happy2 = massage.text[mid:]
    for i in happy:
        sum1 = sum1 + int(i)
    for a in happy2:
        sum2 = sum2 + int(a)
    if sum1 == sum2:
        max.send_message(massage.chat.id, "this a happy ticket")
    else:
        max.send_message(massage.chat.id, "this a not happy ticket")
def filedef(massage):
    file = open(path, "w")
    file1 = open(path, "r")
    word = massage.text.split()
    # for i in word:
    #     if len(i) > 7:
    #         file.write(f'{i}\n')
    file.write(f'{len(word)} количество слов \n')
    file.write(f'{len(massage.text)} количиство символов \n')
    list_abc = ["q","r","w","t","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    count = 0
    for i in massage.text:
        if i in list_abc:
            count = count+1
    file.write(f'{count} количество согласних букв \n')
    list_abc = ["a","u","o","e","y","i",]
    count = 0
    for i in massage.text:
        if i in list_abc:
            count = count+1
    file.write(f'{count} количество гласних букв \n')
    count2 = 0
    for i in massage.text:
        if i.isdigit():
            count2 = count2+1
    file.write(f'{count2} количество цифр \n')
    list_abc2 = ["!", "?", ".", ","]
    count4 = 0
    for d in massage.text:
        if d in list_abc2:
            count4 = count4+1
    file.write(f'{count4} количество символов припинания \n')
    file.close()
    max.send_document(massage.chat.id, open(path, "r"))
def worddef(massage):
    symbolsword = massage.text.split("/")
    max.send_message(massage.chat.id, str(symbolsword[0].count(symbolsword[1])))
def count_symbols(massage):
    symbols = len(massage.text)
    max.send_message(massage.chat.id, str(symbols))
def sun(message):
    sun1 = message.text.split(":")
    hours = int(sun1[0])
    minut = int(sun1[1])
    if 18<=hours<=24 or 0>=hours>6:
        max.send_message(message.chat.id, "В цей час сонця не видно")
    else:
        angle = (hours-6)*15 + minut*0.25
        max.send_message(message.chat.id, f'нахил сонця {angle} градусів')
def calculator(message): # message.text = 2+2
    a = message.text
    b = ["+", "-", "*", "/"]
    for i in b:
        if i in a:
            c = a.split(i)
            if i == "+":
                max.send_message(message.chat.id, f'{c[0]}+{c[1]}={int(c[0])+int(c[1])}')
            elif i == "-":
                max.send_message(message.chat.id, f'{c[0]}-{c[1]}={int(c[0])-int(c[1])}')
            elif i == "*":
                max.send_message(message.chat.id, f'{c[0]}*{c[1]}={int(c[0])*int(c[1])}')
            elif i == "/":
                if c[1] == "0":
                    max.send_message(message.chat.id, "На нуль немажна ділити")
                else:
                    max.send_message(message.chat.id, f'{c[0]}/{c[1]}={int(c[0])/int(c[1])}')


# if message.text == "/name":
    #     max.send_message(message.chat.id, "Напишіть своє ім'я")
    #     @max.message_handler(content_types=["text"])
    #     def name(message):
    #         if message.text.lower == ""
@max.message_handler(content_types=["text"])
def get_text(message):
    if message.text.lower() == "привіт" or message.text.lower() == "hello" or message.text.lower() == "hi" or message.text.lower() == "🖖":
        max.send_message(message.chat.id, "Привіт Сергій! Вітаю тебе з приєднадня з сімєю")
    if message.text.lower() == "як справи" or message.text.lower() == "how do you do":
        max.send_message(message.chat.id, "OK")
    if message.text.lower() == "як тебе звати" or message.text.lower() == "what is your name":
        max.send_message(message.chat.id, "My name Max")
        max.send_message(message.chat.id, "nice to meet you")
# Пользователь пишет время в формате 14:30, мы выводим угол солнца при условии 06:00 - 0 градусов , 18:00 - 180 градусов



max.polling(none_stop=True,interval=0)