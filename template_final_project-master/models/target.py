class Target:
    def __init__(self, sprite, position, size, display):
        self.position = position
        self.sprite = pygame.image.load(sprite)
        self.size = size
        self.display = display
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
    def draw(self):
        self.display.blit(self.sprite, self.rect)
    def move(self, new_position):
        self.position = new_position
        self.rect.topleft = new_position
    def check_collision(self, point):
        return self.rect.collidepoint(point)
    def on_click(self, point):
        if self.check_collision(point):
            self.rect = self.rect.move(-100,-100)
            return True
        else:
            return False