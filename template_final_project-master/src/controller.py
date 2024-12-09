import pygame, random

from src.button import Button 
from src.score import Score
from src.target import Target
from src.timer import Timer

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_COLOR = (255,255,255)
TEXT_COLOR = (0,0,0)
BUTTON_SPACING = 20
FONT_SIZE = 50
TOTAL_TIME = 30

class Controller():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("AIM TRAINER")
        self.state = "START"
        self.font = pygame.font.SysFont("comicsans", FONT_SIZE)
        self.game_background = pygame.image.load("assets/background.png")
        self.game_background = pygame.transform.scale(self.game_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.start_button = Button(
            image_path="assets/start_but.png",
            x=SCREEN_WIDTH//2 - 100,
            y=SCREEN_HEIGHT//2 - 50,
            width = 200,
            height = 100  
        )
        self.restart_button = Button(
            image_path="assets/retry_but.png",
            x=SCREEN_WIDTH//2 - 100,
            y=SCREEN_HEIGHT//2 - 50,
            width = 200,
            height = 100
        )
        self.quit_button = Button(
            image_path="assets/quit_but.png",
            x=SCREEN_WIDTH//2 - 100,
            y=SCREEN_HEIGHT//2 - 50,
            width = 200,
            height = 100
        )
        
        self.score = Score()
        self.timer = Timer(TOTAL_TIME)
        self.target = None
        self.spawn_target()
        
        self.clock = pygame.time.Clock()
    """
    Manages game states.
    args: None
    return: None
    """
        
    def spawn_target(self):
        size = random.randint(30, 100)
        target_size = (size, size)
        padding = 10
        x = random.randint(0, SCREEN_WIDTH - target_size[0] - padding)
        y = random.randint(0, SCREEN_HEIGHT - target_size[1] - padding)
        self.target = Target("assets/Target.png", (x, y), target_size, self.screen)
    """
    Spawns the targets at random areas on the screen with different sizes.
    args: None
    return: None
    """
        
    def mainloop(self):
        while True:
            if self.state == "START":
                self.startloop()
            elif self.state == "END":
                self.endloop()
            elif self.state == "GAME":
                self.gameloop()
    """
    Displays the screen
    args: None
    return: None
    """
    def startloop(self):
        while self.state == "START":
            self.clock.tick(TOTAL_TIME)
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_clicked(event.pos):
                        self.state = "GAME"
                        self.score.reset()
                        self.spawn_target()
                        return
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill(SCREEN_COLOR)
            start_text = self.font.render("AIM TRAINER", True, TEXT_COLOR)
            text_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
            self.screen.blit(start_text, text_rect)
            
            self.start_button.rect.centerx = SCREEN_WIDTH // 2
            self.start_button.rect.y = text_rect.bottom + BUTTON_SPACING
            self.start_button.draw(self.screen)
            
            pygame.display.flip()
    """
    Opens and shows the start screen 
    args: None
    return: None
    """
    def gameloop(self):
        self.timer.restart()
        while self.state == "GAME":
            self.clock.tick(TOTAL_TIME)
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.target and self.target.on_click(mouse_pos):
                            if self.timer.start_time is None:
                                self.timer.restart()
                            self.score.score_hit(hit=True)
                            self.spawn_target()
                        else:
                            self.score.score_hit(hit=False)
            remaining_time = self.timer.countdown()
            if remaining_time <= 0:
                self.state = "END"
                return
            
            self.screen.blit(self.game_background, (0,0))
            
            if self.target:
                self.target.draw()
            
            score_text = self.font.render(
                f"Hits: {self.score.hit} Misses: {self.score.misses}", 
                True, 
                (0,0,0)
            )
            self.screen.blit(score_text, (20,20))
            
            timer_text = self.font.render(
                f"Time: {remaining_time}",
                True,
                (0,0,0)
            )
            self.screen.blit(timer_text, (20, 70))
            
            pygame.display.flip()
    """
    Displays game screen
    args: None
    return: None
    """  
    def endloop(self):               
        while self.state == "END":
            self.screen.fill(SCREEN_COLOR)
            end_text = self.font.render("Game Over! Click anywhere to restart.", True, TEXT_COLOR)
            text_rect = end_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(end_text, text_rect)
            
            
            accuracy = self.score.accuracy()
            accuracy_text = self.font.render(f"Accuracy: {accuracy: .2f}%", True, TEXT_COLOR)
            accuracy_rect = accuracy_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            self.screen.blit(accuracy_text, accuracy_rect)
            
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.score.reset()
                        self.timer.restart()
                        self.spawn_target()
                        self.state = "START"
                        return
            pygame.display.flip()
    """
    Displays end screen
    args: None
    return: None
    """
        

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
        
        