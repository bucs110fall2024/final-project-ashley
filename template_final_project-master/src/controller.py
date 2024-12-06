import pygame, random

from src.button import Button 
from src.score import Score
from src.target import Target
from src.timer import Timer

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
class Controller():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("AIM TRAINER")
        self.state = "START"
        self.font = pygame.font.SysFont("comicsans", 50)
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
        self.timer = Timer(total_time=30)
        self.target = None
        self.spawn_target()
        
        self.clock = pygame.time.Clock()
        
    def spawn_target(self):
        size = random.randint(30, 100)
        target_size = (size, size)
        padding = 10
        x = random.randint(0, SCREEN_WIDTH - target_size[0] - padding)
        y = random.randint(0, SCREEN_HEIGHT - target_size[1] - padding)
        self.target = Target("assets/Target.png", (x, y), target_size, self.screen)
        
    def mainloop(self):
        while True:
            if self.state == "START":
                self.startloop()
            elif self.state == "END":
                self.endloop()
            elif self.state == "GAME":
                self.gameloop()
    
    def startloop(self):
        while self.state == "START":
            self.clock.tick(30)
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
            self.screen.fill((255, 255, 255))
            self.start_button.draw(self.screen)
            pygame.display.flip()
    
    def gameloop(self):
        while self.state == "GAME":
            self.clock.tick(30)
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
            if remaining_time == 0:
                self.state = "END"
                return
            
            self.screen.fill((255, 255, 255))
            
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
            
    def endloop(self):
        while self.state == "END":
            self.clock.tick(30)
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button.is_clicked(event.pos):
                        self.score.reset()
                        self.timer.restart()
                        self.spawn_target()
                        self.state = "START"
                        return
                    elif self.quit_button.is_clicked(event.pos):
                        pygame.quit()
                        exit()
                        
        self.screen.fill((255,255,255))
        end_text = self.font.render("Game Over! Click the button to restart.", True, (0,0,0))
        text_rect = end_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(end_text, text_rect)
        
        
        accuracy = self.score.accuracy()
        accuracy_text = self.font.render(f"Accuracy: {accuracy: .2f}%", True, (0,0,0))
        accuracy_rect = accuracy_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(accuracy_text, accuracy_rect)
        
        self.restart_button.rect.centerx = SCREEN_WIDTH // 2
        self.restart_button.rect.y = SCREEN_HEIGHT // 2 + 50
        self.restart_button.draw(self.screen)
        
        self.quit_button.rect.centerx = SCREEN_WIDTH // 2
        self.quit_button.rect.y = SCREEN_HEIGHT // 2 + 70
        self.quit_button.draw(self.screen)
        
        pygame.display.flip()
        
        

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
        
        