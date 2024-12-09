import pygame

class Target:
    def __init__(self, sprite, position, size, display):
        self.sprite = pygame.image.load(sprite).convert_alpha()
        self.size = size
        self.position = position
        self.display = display
        self.sprite = pygame.transform.scale(self.sprite, size)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
    """
    Initializes the target.
    args: (str) pathway to image file; (tuple) x and y where the sprite is placed; (tuple) width and height dimensions; (pygame.Surface) where sprite is drawn
    return: None
    """
    def draw(self):
        self.display.blit(self.sprite, self.rect)
    """
    Draw the sprite
    args: None
    returns: None
    """
    def on_click(self, point):
        return self.rect.collidepoint(point)
    """
    Checks if a point is in the sprite's rectangle
    args: (tuple) x and y coordinates of click
    returns: (bool) True if point is in sprite, false if not
    """