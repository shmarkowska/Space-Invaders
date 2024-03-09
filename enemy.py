import pygame


class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load("images/enemy1.png")
    self.rect = self.image.get_rect()
    self.speed=3
    self.rect.left=x
    self.rect.top=y
    self.mask = pygame.mask.from_surface(self.image)
   
  def update(self):
    self.rect.y += self.speed

  def get_height(self):
    return self.image.get_height()
   