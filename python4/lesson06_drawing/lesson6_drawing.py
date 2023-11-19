# В этом уроке познакомимся с рисованием в Minecraft

# Прошлое дз:


# from mcpi.minecraft import Minecraft
# import mcpi.block as block
# import time

# mc = Minecraft.create(address="localhost", port=4711)
# pos = mc.player.getPos()
# x = pos.x + 1
# y = pos.y
# z = pos.z + 1
# while True:
#     mc.setBlock(x, y, z, block.AIR.id)
#     y += 1
#     mc.setBlock(x, y, z, block.TNT.id)
#     time.sleep(1)

# Для работы с графикой нам нужно скачать библиотеку minecraftstuff:

# pip install minecraftstuff

# Из нее нам пригодится MinecraftDrawing:

from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
import time

mc = Minecraft.create(address="localhost", port=4711)

# Для создание объекта рисования блоками надо вызвать класс MinecraftDrawing и передать в него объект Minecraft:
mcdraw = MinecraftDrawing(mc)
pos = mc.player.getPos()

# drawLine(x1, y1, z1, x2, y2, z2, id_блока) - создает линию от точки 1 до точки 2 с указанным типом блока.
# Обратите внимание, что id  должны быть целыми числами.
# mcdraw.drawLine(int(pos.x), int(pos.y), int(pos.z), int(pos.x + 5), int(pos.y + 5), int(pos.z + 5), 23)

# drawCircle(x, y, z, radius id_блока) - рисует окружность с указанным радиусом и центром в указанной точке с указанным типом блока.
# mcdraw.drawCircle(int(pos.x), int(pos.y), int(pos.z), 10, 23)

# Пример программы с урока: Будут появляться круги если поставить блок в точку где стоит  игрок.
while True:
    time.sleep(1)
    block = mc.getBlock(int(pos.x), int(pos.y), int(pos.z))
    if block!= 0:
        radius = 10
        for i in range(10):
            mcdraw.drawCircle(int(pos.x), int(pos.y), int(pos.z), radius+i, 23)
            time.sleep(0.5)
            mcdraw.drawCircle(int(pos.x), int(pos.y), int(pos.z), radius+i, 0)
