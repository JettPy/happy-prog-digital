# В этом уроке рассмотрим библиотеку для работы с изображениями Pillow
# Раньше эта библиотека входила в стандартный набор Python, но со временем стала отдельным пакетом
# Что бы обратиться к этой библиотеке мы импортируем PIL (Python Image Library)
# Основным классом для нас является Image - именно он позволяет открывать, сохранять и обрабатывать изображения.
from PIL import Image

# Разберем пример на картинке красной панды:
# Что бы открыть изображение используем команду Image.open(<название файла>):
panda = Image.open('picture.jpg')

# Мы можем узнать какую нибудь базовую информацию о нашей картинке:
print(panda.size)  # Вывод: (1920, 1280) - размеры картинки
print(panda.filename)  # Вывод: picture.jpg - название файла
print(panda.format)  # Вывод: JPEG - формат файла
print(panda.format_description)  # Вывод: JPEG (ISO 10918) - описание формата

# Для вывода картинки на экран можно использовать метод show():
# panda.show()

# Мы можем создавать новые картинки, и рисовать в них что-нибудь:
# Для этого нам пригодиться класс ImageDraw.

from PIL import ImageDraw

# Создаем изображение размером 1000 на 1600:
image_blank = Image.new('RGBA', (1000, 1600))

# Создаем объект для рисования в новой картинке
draw = ImageDraw.Draw(image_blank)

# rectangle - метод для создания прямоугольника
draw.rectangle((200, 400, 700, 600), fill=(255, 0, 0), outline='yellow', width=5)
# ellipse - метод для создания эллипса
draw.ellipse((200, 400, 700, 600), fill=(255, 0, 255), outline='purple', width=5)
# polygon - метод для создания полигона
draw.polygon(((0, 0), (100, 0), (100, 100), (50, 200)), fill='blue', outline='pink')
# line - метод для создания линии
draw.line(((800, 600), (700, 500), (1000, 400)), fill='black', width=10, joint='curve')

# Для рисования окружностей есть еще методы:

# arc - метод для создания дуги
draw.arc((800, 100, 1000, 300), start=10, end=40, width=10, fill='red')
# chord - метод для создания хорды
draw.chord((1000, 300, 1200, 500), start=10, end=180, width=10, fill='red')
# pieslice - метод для рисования фигуры как если бы от пирога отрезали кусочек
draw.pieslice(((800, 100), (1000, 300)), start=10, end=180, width=10, fill='red')

# Естественно при работе с изображением можно настраивать фильтры и цветокоррекцию
# для этого импортируем модуль
from PIL import ImageFilter

# Ниже представлены различные фильтры:
image_blur = panda.filter(ImageFilter.BLUR)
# image_blur.show()
image_contour = panda.filter(ImageFilter.CONTOUR)
# image_contour.show()
image_detail = panda.filter(ImageFilter.DETAIL)
# image_detail.show()
image_edge = panda.filter(ImageFilter.EDGE_ENHANCE)
# image_edge.show()
image_edge_more = panda.filter(ImageFilter.EDGE_ENHANCE_MORE)
# image_edge_more.show()
image_find_edges = panda.filter(ImageFilter.FIND_EDGES)
# image_find_edges.show()
image_emboss = panda.filter(ImageFilter.EMBOSS)
# image_emboss.show()
image_sharp = panda.filter(ImageFilter.SHARPEN)
# image_sharp.show()
image_smooth = panda.filter(ImageFilter.SMOOTH)
# image_smooth.show()
image_smooth_more = panda.filter(ImageFilter.SMOOTH_MORE)
# image_smooth_more.show()

# Далее представлен фрагмент кода для обработки изображения бота:

import telebot
import os
import dotenv

dotenv.load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


# В content_types передадим тип фотографии (photo)
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Далее объект message будет хранить информацию об изображении (поле photo).
    # В photo храниться список из 4 объектов вида <telebot.types.PhotoSize object at 0x0000023FF0C1BF10>.
    # Каждый объект хранит картинку разных масштабов. Оригинальная последняя, берем ее id из поля file_id:
    photo_id = message.photo[-1].file_id
    # Далее используя метод get_file(<id файла>) получаем объект типа telebot.types.File
    photo_file = bot.get_file(photo_id)
    # И берем путь к файлу внутри системы (поле file_path):
    photo_path = photo_file.file_path
    # Скачиваем фото методом download_file(<путь к файлу>). Этот метод похож на обычный стандартный open:
    downloaded_photo = bot.download_file(photo_path)

    # Отправляем фото обратно в ответ методом send_photo. Метод похож на send_message:
    # Он также первым методом принимает адрес, куда отправить, а вторым то что отправить, в нашем случае набор байт,
    # из которых состоит изображение
    bot.send_photo(message.chat.id, downloaded_photo)
