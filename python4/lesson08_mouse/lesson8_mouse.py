# Сегодня мы научимся обрабатывать событие клика клика клавиши мышки и создадим простую игру - стрелялку.
# Правда стрелять мы будем пока только в одном направлении, но все равно постараемся сделать игру интересной.
# Для работы в Python с мышью нам необходимо установить библиотеку mouse.
# Запустим командную строку и выполним команду:

# pip install mouse

# Теперь, как обычно, создаем базовый код, и в блок импорта добавим новую библиотеку mouse.

from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import sleep
import mouse

mc = Minecraft.create(address="localhost", port=4711)

# Очистим поле

pos = mc.player.getTilePos()
size = 10
mc.setBlocks(pos.x - size, pos.y - size, pos.z - size, pos.x + size, pos.y + size, pos.z + size, block.AIR.id)


# Нам нужно чтобы при нажатии от игрока вылетал блок. Пускай это будет каменный блок.
# Напишем эту функцию:



def shoot():
    # mc.postToChat("shooting start")
    posB = mc.player.getTilePos()
    for i in range(50):
        mc.setBlock(posB.x - 1, posB.y, posB.z, block.AIR.id)
        mc.setBlock(posB.x, posB.y, posB.z, block.STONE.id)
        sleep(0.1)
        posB.x += 1
    # mc.postToChat("shooting end")


# Как видно, мы создаем каменный блок каждый раз на 1 координату по х дальше, а на
# предыдущем месте замещаем его блоком воздух (AIR). Таким образом у нас получается движение блока.

# while True:
#     a = mc.events.pollBlockHits()
#     if len(a) > 0:
#         mouse.on_click(shoot)

# Чтобы при нажатии левой кнопки мыши выполнялся наш код, необходимо
# воспользоваться функцией из библиотеки mouse:

while True:
    mouse.on_click(shoot)
