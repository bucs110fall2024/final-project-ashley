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
    """
    args: (int) x and y coordinate values; (int) width and height; (tuple) RGB color of button; (str) pathway to button image
    return: None
    """
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    """
    Draws the button
    args: (pygame.Surface) the surface that the button is drawn on
    return: None
    """
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    """
    Determines if the button is clicked based on mouse position
    args: (tuple) x and y coordinates of mouse click
    return: (bool) True if mouse click is in boundaries, false if not
    """