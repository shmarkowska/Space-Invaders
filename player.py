import pygame
from laser import Laser

HEIGHT=750

class Player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image=pygame.image.load("images/player1.png")
    self.rect = self.image.get_rect()
    self.x = x
    self.y = y
    self.rect.center = (x, y)
    self.speed = 5
    self.ready = True
    self.mask = pygame.mask.from_surface(self.image)
    self.laser_time = 0
    self.laser_cooldown = 600
    self.lasers_group = pygame.sprite.Group()


  #movement with WSAD and shooting with space
  
  def get_input(self):
    keys = pygame.key.get_pressed()
    return keys

  def move(self, keys, window_width, window_height):
    if keys[pygame.K_w] and self.rect.y > 0:
      self.rect.y -= self.speed
    if keys[pygame.K_s] and self.rect.y < window_height - self.rect.height:
      self.rect.y += self.speed
    if keys[pygame.K_a] and self.rect.x > 0:
      self.rect.x -= self.speed
    if keys[pygame.K_d] and self.rect.x < window_width - self.rect.width:
      self.rect.x += self.speed
    if keys[pygame.K_SPACE] and self.ready:
      self.shoot_laser()
      self.ready = False
      self.laser_time = pygame.time.get_ticks()

#laser position
  
  def shoot_laser(self):
    laser = Laser((self.rect.centerx, self.rect.top), 5, 750)
    self.lasers_group.add(laser)

  #bufor
  
  def recharge(self):
    if not self.ready:
      current_time = pygame.time.get_ticks()
      if current_time - self.laser_time >= self.laser_cooldown:
        self.ready = True
  
  def update(self):
    self.get_input()
    self.recharge()
    self.lasers_group.update()

  def get_height(self):
    return self.image.get_height()
    
  # def draw(self, window):
  #   super().draw(window)
  #   self.healthbar(window)

  # def healthbar(self, window):
  #   pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.image.get_height() + 10, self.image.get_width(), 10))
  #   pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.image.get_height() + 10, self.image.get_width() * (self.health/self.max_health), 10))