import pygame

class Target:
    def __init__(self, sprite, position, size, display):
        self.sprite = pygame.image.load(sprite).convert_alpha()
        self.size = size
        self.position = position
        self.display = display
        self.sprite = pygame.transform.scale(self.sprite, size)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
    def draw(self):
        self.display.blit(self.sprite, self.rect)
    def on_click(self, point):
        return self.rect.collidepoint(point)