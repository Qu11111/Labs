import telebot
from telebot import types
from datetime import date
import json
import io
import random

API_TOKEN = '7004556756:AAFnUquI9LIb7uANPryJxM7JAsVcNlA5TTs'

bot = telebot.TeleBot(API_TOKEN)


def is_day_name(day_name):
    days = ["понедельник", "вторник", "среда", "четверг", "пятница"]

    return day_name.lower() in days

def is_even_week():
    today = date.today()
    week_number = today.isocalendar()[1]
    return week_number % 2 == 0

def get_schedule(day_name, is_even):
    schedule = []

    with io.open("calendar.json", encoding='utf-8') as f:
        file_content = f.read()
        calendar = json.loads(file_content)

        schedule = calendar["even" if is_even else "odd"][day_name.lower()]

    return schedule

def get_format_schedule(day_name, is_even):
    schedule = get_schedule(day_name, is_even)

    formattedString = " *{day_name}*\n\n".format(day_name=day_name.capitalize())

    for item in schedule:
        formattedString += " {item}\n".format(item=item)

    return formattedString


def get_curweek_schedule():
    days = ["понедельник", "вторник", "среда", "четверг", "пятница"]
    even = is_even_week()

    s = "Расписание на эту неделю\n\n"

    for day in days:
        s += get_format_schedule(day, even) + "\n"
    
    return s

def get_nextweek_schedule():
    days = ["понедельник", "вторник", "среда", "четверг", "пятница"]
    even = not is_even_week()

    s = "Расписание на следующую неделю\n\n"

    for day in days:
        s += get_format_schedule(day, even) + "\n"
    
    return s

week_keyboard = (
    types.ReplyKeyboardMarkup(resize_keyboard=True)
    .add(types.KeyboardButton("Понедельник"))
    .add(types.KeyboardButton("Вторник"))
    .add(types.KeyboardButton("Среда"))
    .add(types.KeyboardButton("Четверг"))
    .add(types.KeyboardButton("Пятница"))
    .add(types.KeyboardButton("Расписание"))
)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "При возникновении вопросов используйте /help", reply_markup=week_keyboard)


@bot.message_handler(commands=['help'])
def handle_help(message):
    help_message = """
 Привет! Я бот для удобного просмотра расписания в институте.

Создан студентом группы 4311-22 Папеевым Сергеем.
Доступные команды:

/start - начать взаимодействие с ботом
/help - доступные команды
/kstu - получить ссылку на официальный сайт КНИТУ
/vk - получить ссылку на официальную группа вконтакте КНИТУ
/location - получить адреса всех учебных корпусов
    """

    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=['location'])
def handle_location(message):
    locations = """
    Местонахождение учебных корпусов:

    Корпус «А» - г. Казань, ул. К. Маркса, 68
    Корпус «Б», «В», «О» - г. Казань, ул. К. Маркса, 72
    Корпус «Д», «Е», «Л», «М» - г. Казань, ул. Сибирский тракт, 12
    Корпус «К» - г. Казань, ул. Толстого, 8/31
    Корпус «Г» - г. Казань, ул. Попова, 10
    Корпус «И» - г. Казань, ул. Сибирский тракт, 41
    Корпус «Т» - г. Казань, ул. Толстого, 6 корпус 1
    """

    bot.send_message(message.chat.id, locations)


@bot.message_handler(commands=['vk'])
def handle_vk_group(message):
    bot.send_message(message.chat.id, "Группа Казанского национального технического университета (КазНИТУ) во ВКонтакте: https://vk.com/knitu")


@bot.message_handler(commands=['kstu'])
def kstu_handler(message):
    bot.send_message(message.chat.id, 'https://www.kstu.ru/')



@bot.message_handler(func=lambda message: message.text.lower() == "как дела?")
def handle_wheretogo(message):
    bot.send_message(message.chat.id, "отлично")


@bot.message_handler(func=lambda message: message.text.lower() == "твое имя?")
def handle_scholarship(message):
    bot.send_message(message.chat.id, "я просто бот")


@bot.message_handler(func=lambda message: message.text.lower() == "назови фамилию любого преподавателя")
def handle_scholarship(message):
    l = [
        "Титовцев",
        "Панченко",
        "Курбангалеев",
        "Габделганиева",
        "Габдрахманова"
    ]

    bot.send_message(message.chat.id, "Фамилия преподавателя: " + random.choice(l))


@bot.message_handler(func=lambda message: True)
def handle_day(message):
    text = message.text.lower()

    if is_day_name(text):
        schedule = get_format_schedule(text, is_even_week())
        bot.send_message(message.chat.id, schedule)

    elif text == "расписание":
        schedule = get_curweek_schedule()
        bot.send_message(message.chat.id, schedule)


    else:
        bot.send_message(message.chat.id, "Такой команды не существует")




bot.infinity_polling()