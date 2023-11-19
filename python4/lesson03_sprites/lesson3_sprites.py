# Импортируем библиотеку pygame и os для взаимодействия с операционной системой
import pygame
import os


WIDTH = 800
HEIGHT = 600
FPS = 60

LIGHT_GREEN = (196, 240, 129)
RED = (199, 71, 16)

# Инициализируем pygame
pygame.init()
# Создаем объект экрана и задаем ему размер
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Далее будем подключать картинку для нашего спрайта:
# Первым делом определяем динамически путь в системе до нашего файла
game_folder = os.path.dirname(__file__)
# И получаем путь до картики нашего игрока, объединяя путь до проекта и название картинки
player_img = pygame.image.load(os.path.join(game_folder, "car.svg")).convert()

clock = pygame.time.Clock()


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Заменяем наш красный квадрат на изображение полученное ранее
        # А так же, с помощью transform.scale изменим масштаб изображения:
        self.image = pygame.transform.scale(player_img, (64, 32))
        self.rect = self.image.get_rect()
        self.v = [0, 0]
        # Сделаем так, чтобы наш игрок появляйся по центру поля,
        # передав параметры ширины и высоты в поле center:
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        # Ограничим перемещение нашего игрока в рамках видимого поля:
        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT
        self.rect.move_ip(*self.v)


# Спрайты лучше групировать, поэтому используем специальный класс Group для создания группы:
all_sprites = pygame.sprite.Group()
player = Player()
# Поместим в группу нашего игрока
all_sprites.add(player)
isRunning = True
while isRunning:
    t = clock.tick(FPS)
    screen.fill(LIGHT_GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.v[1] = -.5 * t
            elif event.key == pygame.K_s:
                player.v[1] = .5 * t
            elif event.key == pygame.K_a:
                player.v[0] = -.5 * t
            elif event.key == pygame.K_d:
                player.v[0] = .5 * t
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.v[1] = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                player.v[0] = 0
    # Теперь вместо одного игрока будем обновлять группу спрайтов, в которую он входит
    all_sprites.update()
    screen.blit(player.image, player.rect)
    pygame.display.update()
pygame.quit()
