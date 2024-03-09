import sys
import os
import pygame
import random

from player import Player
from enemy import Enemy
from pygame.locals import QUIT

pygame.font.init()

#window
WIDTH, HEIGHT = 600, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Ivaders")

#background
BG = pygame.transform.scale(
    pygame.image.load(os.path.join("images/background.png")), (WIDTH, HEIGHT))


#main settings
def main():
  run = True
  FPS = 60
  level = 0
  lives = 5
  clock = pygame.time.Clock()
  wave_length = 5
  main_font = pygame.font.SysFont("arial", 50)
  lost_font = pygame.font.SysFont("arial", 60)
  lost = False
  lost_count = 0

  #player input
  player = Player(200, 600)
  playersprite = pygame.sprite.GroupSingle()
  playersprite.add(player)

  #enemy input
  enemies = pygame.sprite.Group()

  #window settings
  def redraw_window():
    WIN.blit(BG, (0, 0))
    #text
    lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
    level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

    WIN.blit(lives_label, (10, 10))
    WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

    playersprite.draw(WIN)
    playersprite.sprite.lasers_group.draw(WIN)
    enemies.draw(WIN)
    pygame.display.update()
  
  #collision settings
  def collide(obj1, obj2):
    offset_x = obj2.rect.x - obj1.rect.x
    offset_y = obj2.rect.y - obj1.rect.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None

  def collision(self, obj):
    return collide(self, obj)

  #game loop
  run = True

  while run:
    clock.tick(FPS)
    redraw_window()
    
    #health management
    if lives <= 0:
      lost = True
      lost_count += 1

    if lost:
      if lost_count > FPS * 3:
          run = False
      else:
          continue
    
    #enemies appearing randomly

    if len(enemies) == 0:
      level += 1
      wave_length += 5
      for i in range(wave_length):
        enemy = Enemy(random.randrange(50, WIDTH - 100),
                      random.randrange(-1500, -100))
        enemies.add(enemy)
      print(len(enemies))
      
    #collisions
    for enemy in enemies:
      enemy.update()
      if collide(enemy, player):
        lives -= 1
        enemies.remove(enemy)
      if enemy.rect.top + enemy.get_height() > HEIGHT:
        lives -= 1
        enemies.remove(enemy)

    for laser in playersprite.sprite.lasers_group:
      for enemy in enemies:
        if collide(enemy, laser):
          enemies.remove(enemy)

    keys = player.get_input()
    player.move(keys, WIDTH, HEIGHT)

    playersprite.update()

    for event in pygame.event.get():
      if event.type == QUIT:
        run = False

#main menu
def main_menu():
  title_font = pygame.font.SysFont("arial", 30)
  run = True
  while run:
      WIN.blit(BG, (0,0))
      title_label = title_font.render("Welcome to Python Invaders", 1, (255,255,255))
      title2_label = title_font.render("Press your mouse to begin..", 1, (255,255,255))
      WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
      WIN.blit(title2_label, (WIDTH/2 - title_label.get_width()/2, 400))
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            main()
  pygame.quit()
  sys.exit()



main_menu()
