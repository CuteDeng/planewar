# -*- coding:utf8 -*-
from plane_sprites import *

pygame.init()

scree = pygame.display.set_mode([480, 700])

bg = pygame.image.load("images/background.png")
scree.blit(bg, (0, 0))

hero = pygame.image.load("images/me1.png")
scree.blit(hero, (150, 500))

pygame.display.update()

clock = pygame.time.Clock()
hero_rect = pygame.Rect(150, 500, 102, 126)

enemy = GameSprite("images/enemy1.png")
enemy1 = GameSprite("images/enemy2.png", 2)
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700
    scree.blit(bg, (0, 0))
    scree.blit(hero, hero_rect)

    enemy_group.update()
    enemy_group.draw(scree)
    pygame.display.update()

pygame.quit()
