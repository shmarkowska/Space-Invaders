import pygame 
HEIGHT=750

class Laser(pygame.sprite.Sprite):
  def __init__(self,position,speed, HEIGHT):
    super().__init__()
    self.image = pygame.Surface((4,15))
    self.image.fill((0,153,153))
    self.rect = self.image.get_rect(center=position)
    self.height_y_constraint = HEIGHT
    self.speed = speed
    self.HEIGHT=HEIGHT
    self.mask = pygame.mask.from_surface(self.image)
  
  #disappearing when outside of borders
  def update(self):
    self.rect.y -= self.speed
    if self.rect.y > self.HEIGHT + 15 or self.rect.y < 0:
      self.kill()

  
