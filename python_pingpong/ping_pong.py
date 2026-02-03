from pygame import *
from random import randint
init()
'''Required classes'''

#parent class for sprites
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__(player_image, player_x, player_y, player_speed, wight, height)
        self.speed_x = 3
        self.speed_y = 3
    def update_dir(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= win_height - self.rect.height:
            self.speed_y *= -1

back = (200, 255, 255) #background color (background)
win_width = 600
win_height = 500
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60



racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = Ball('tenis_ball.png', 200, 200, 4, 50, 50)
balls = sprite.Group()
balls.add(ball)
rackets = sprite.Group()
rackets.add(racket1)
rackets.add(racket2)

speed_x = 3
speed_y = 3
while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        racket1.update_l()
        racket2.update_r()
        ball.update_dir()

    if sprite.groupcollide(balls, rackets, False, False):
        ball.speed_x *= -1
    
    if ball.rect.x > win_width:
        finish = True
        font1 = font.Font(None, 50)
        text_1 = font1.render("Player 1 Wins!",  True, (255,0,0))
        window.blit(text_1, (200,200))
    elif ball.rect.x < 0:
        finish = True
        font2 = font.Font(None, 50)
        text_2 = font2.render("Player 2 Wins!", True, (255,0,0))
        window.blit(text_2,(200,200))

    rackets.draw(window)
    balls.draw(window)

    display.update()
    clock.tick(FPS)