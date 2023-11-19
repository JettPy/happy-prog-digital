from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create(address="localhost", port=4711)

# Для обработки событий у объекта minecraft есть поле events.

# В нем есть несколько списков событий:

# mc.events.pollBlockHits() - получение списка событий удара по блоку
# Важно, что ударами считаются нажатия правой кнопки мыши с мечём в руках.
# А также после вызова списка pollBlockHits() - список событий сбрасывается.
# Метод возвращает список из BlockEvent, который содержит тип события, координаты блока и id игрока

# mc.events.pollChatPosts() - получение данных о сообщениях.
# Метод возвращает список из ChatEvent, который содержит тип события, текст сообщения и id игрока

# mc.events.ProjectileEvent() - получение списка ударов такими объектами как стрелы и т.п.
# Метод возвращает список из ProjectileEvent, который содержит тип события, координаты блока и данные о снаряде

# Задача: превратить как можно больше объектов в арбузы за 30 секунд
mc.postToChat("game started")
time.sleep(30)
hits = mc.events.pollBlockHits()
block = 103
for hit in hits:
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
    mc.setBlock(x, y, z, block)
mc.postToChat(f"game ended. Hit {len(hits)} blocks")
