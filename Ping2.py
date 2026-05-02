from pygame import *
from random import randint
# подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.SysFont("Arial", 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))


font2 = font.SysFont("Arial", 36)


#фоновая музыка
mixer.init()



# нам нужны такие картинки:
score = 0 # сбито кораблей
goal = 10 # столько кораблей нужно сбить для победы
lost = 0 # пропущено кораблей
max_lost = 3 # проиграли, если пропустили столько
 
# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
  # метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def updater(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


# класс спрайта-врага  
ball = GameSprite('ball.png', 200,200,69,69,0)
racket1 = Player('racketka.png',20,100,10,150,10)
racket2 = Player('racketka.png',600,100,10,150,10)
# класс спрайта-пули  
 
# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
speed_x=8
speed_y=8
    

 

 

 
# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        # событие нажатия на пробел - спрайт стреляет
    
    if not finish:
        ball.rect.x +=speed_x
        ball.rect.y +=speed_y
    if ball.rect.y >(win_height  - 50) or ball.rect.y<0:
        speed_y *= -1
    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
        speed_x *=-1
    if ball.rect.x<0:
        finish = True
        window.blit(lose1(200,200))
 
  # сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
        # обновляем фон
        window.fill((120,120,205))
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.updatel()
        racket2.updater()

       
        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
