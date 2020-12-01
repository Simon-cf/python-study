import pygame
import random

# 常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
BACK_IMAGE = "./images/background.png"
ENEMY_IMAGE1 = "./images/enemy1.png"
ENEMY_IMAGE2 = "./images/enemy2.png"
HERO_IMAGE = "./images/me1.png"
BULLET_IMAGE = "./images/bullet2.png"
# 事件常量
ENEMY_EVENT = pygame.USEREVENT
BULLET_EVENT = pygame.USEREVENT + 1



class GameSprites(pygame.sprite.Sprite):
    """游戏精灵基类"""

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprites):
    """游戏背景精灵"""

    def __init__(self):
        super().__init__(BACK_IMAGE)

    def update(self):
        super().update()
        if self.rect.top >= SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.top


class Enemy(GameSprites):
    """敌机精灵"""

    def __init__(self, image_name):
        super(Enemy, self).__init__(image_name)
        self.rect.x = random.randint(0, SCREEN_RECT.right - self.rect.width)
        self.rect.bottom = SCREEN_RECT.top

    def update(self):
        super(Enemy, self).update()
        if self.rect.top >= SCREEN_RECT.bottom:
            self.kill()


class Hero(GameSprites):
    """英雄精灵"""

    def __init__(self):
        super().__init__(HERO_IMAGE, 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 80


    def update(self):
        super().update()
        speed = 3
        keys_pressed =  pygame.key.get_pressed()
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            self.rect.y += speed
        elif keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            self.rect.y -= speed
        elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.rect.x -= speed
        elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.rect.x += speed


        if self.rect.left <= SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left
        elif self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.bottom <= SCREEN_RECT.top:
            self.rect.top = SCREEN_RECT.bottom
        elif self.rect.bottom >= SCREEN_RECT.bottom + 40:
            self.rect.bottom = SCREEN_RECT.bottom + 40

class Bullet(GameSprites):
    """子弹精灵"""
    def __init__(self):
        super().__init__(BULLET_IMAGE, -2)

    def update(self):
        super().update()
        if self.rect.bottom <= SCREEN_RECT.top:
            self.kill()
