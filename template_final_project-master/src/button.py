import pygame

FONT_SIZE = 60
MESSAGE_POSITION = 20
class Button(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, width=175, height=75, color=(0,0,255), image_path=None):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)