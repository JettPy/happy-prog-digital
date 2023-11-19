from mcpi.minecraft import Minecraft
from time import sleep

# В этом уроке создадим игру "пол это лава"

# подключаемся к серверу minecraft
# address="localhost" адресс сервера в сети, в нашем случае он локальный
# port=4711 порт по которму python подключается к серверу
mc = Minecraft.create(address="localhost", port=4711)
# mc.player - переменная, которая содержит информацию об игроке
# получаем стартовое положение игрока методом getPos у mc.player (объект Vec3, содержит координаты x, y, z)
start = mc.player.getPos()
# Задаем начальное количество жизней, например 10
hp = 10
# С помощью mc.postToChat можно отправлять сообщения в чат
mc.postToChat(f'You have {hp} hp')
# пока у игрока есть жизни
while hp > 0:
    # Получаем координаты игрока
    pos = mc.player.getPos()
    # Если игрок находится в прямоугольнике, шириной 20 на 20 блоков перед начальным положением игрока
    if start.x + 1 <= pos.x <= start.x + 21 and start.z - 10  <= pos.z <= start.z + 10:
        # То отнимаем жизнь
        hp -= 1
        # Выводим сообщение "Lava" в чат м сообщаем сколько жизней осталось у игрока
        mc.postToChat('Lava')
        mc.postToChat(f'You have {hp} hp')
        # Перемещаем игрока в начальное положение командой mc.player.setPos
        mc.player.setPos(start)
    # Создаем задержку в 1 секунду
    sleep(1)
# Сообщаем что игрок проиграл
mc.postToChat(f'You Lose')
