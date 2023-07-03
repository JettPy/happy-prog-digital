import sqlite3
import telebot
from telebot import types
import os
import dotenv

dotenv.load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

# Подключение к базе данных
conn = sqlite3.connect('notes.db', check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы для хранения записей
cursor.execute('''CREATE TABLE IF NOT EXISTS notes
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   text TEXT)''')
conn.commit()

# Создание бота
bot = telebot.TeleBot(API_TOKEN)

# Функция для добавления записи в базу данных
def add_note(user_id, text):
    cursor.execute('INSERT INTO notes (user_id, text) VALUES (?, ?)', (user_id, text))
    conn.commit()

# Функция для получения всех записей пользователя из базы данных
def get_notes(user_id):
    cursor.execute('SELECT * FROM notes WHERE user_id = ?', (user_id,))
    return cursor.fetchall()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Создание клавиатуры
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Добавить запись'))
    keyboard.add(types.KeyboardButton('Посмотреть записи'))

    # Отправка сообщения с приветствием и клавиатурой
    bot.send_message(message.chat.id, 'Привет! Это твоя записная книжка. Что хочешь сделать?', reply_markup=keyboard)

# Обработчик команды "Добавить запись"
@bot.message_handler(func=lambda message: message.text == 'Добавить запись')
def add_note_handler(message):
    # Отправка сообщения с запросом текста записи
    bot.send_message(message.chat.id, 'Напиши свою запись:')
    bot.register_next_step_handler(message, add_note_step)

# Обработчик следующего шага после команды "Добавить запись"
def add_note_step(message):
    # Добавление записи в базу данных
    add_note(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Запись добавлена!')

# Обработчик команды "Посмотреть записи"
@bot.message_handler(func=lambda message: message.text == 'Посмотреть записи')
def get_notes_handler(message):
    # Получение всех записей пользователя из базы данных
    notes = get_notes(message.chat.id)

    # Отправка сообщения со списком записей
    if notes:
        notes_text = '\n\n'.join([f'{note[0]}. {note[2]}' for note in notes])
        bot.send_message(message.chat.id, f'Вот твои записи:\n\n{notes_text}')
    else:
        bot.send_message(message.chat.id, 'У тебя пока нет записей.')

# Запуск бота
bot.polling()
