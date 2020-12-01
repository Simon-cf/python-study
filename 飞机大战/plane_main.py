from plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        # 设置敌机定时器
        pygame.time.set_timer(ENEMY_EVENT, 1000)
        pygame.time.set_timer(BULLET_EVENT, 650)
        self.count = 0

    def __create_sprites(self):
        self.back1 = Background()
        self.back2 = Background()
        self.back2.rect.bottom = SCREEN_RECT.top
        self.back_group = pygame.sprite.Group(self.back1, self.back2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.bullet_group = pygame.sprite.Group()

    def start_game(self):
        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == ENEMY_EVENT:
                if self.count % 2 == 0:
                    self.enemy = Enemy(ENEMY_IMAGE2)
                    self.count += 1
                else:
                    self.enemy = Enemy(ENEMY_IMAGE1)
                    self.count += 1
                self.enemy_group.add(self.enemy)
            elif event.type == BULLET_EVENT:
                for i in range(3):
                    for k in range(2):
                        self.bullet = Bullet()
                        self.bullet.rect.centerx = self.hero.rect.centerx + 10 - (20 * k)
                        self.bullet.rect.bottom = self.hero.rect.top + 20 * i
                        self.bullet_group.add(self.bullet)

    def __check_collide(self):
        pygame.sprite.groupcollide(self.bullet_group, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if enemies:
            self.hero.kill()
            self.__game_over()

    def __update_sprites(self):
        for group in [self.back_group, self.enemy_group, self.hero_group, self.bullet_group]:
            group.update()
            group.draw(self.screen)

    def __game_over(self):
        print("英雄死亡，游戏结束")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()
