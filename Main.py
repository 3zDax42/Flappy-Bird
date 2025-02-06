import pygame
import random
pygame.init()
#--------Classes--------#
def check_collision(bx, by, px, py):
    if (bx + 30 > px and bx < px + 50) and by < py:
        return True
    if (bx + 30 > px and bx < px + 50) and by + 30 > py + 150:
        return True
    return False
class bird:
    def __init__(self):
        self.y = 400
        self.velocity = 0
    def flap(self):
        self.velocity = -3
    def physics(self):
        self.velocity += 0.1
        self.y += self.velocity
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (50, self.y, 30, 30))
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50,400)
        self.gap = 150
        self.top_pipe = pygame.transform.flip(pipe_image, False, True)
        self.bottom_pipe = pipe_image
    def move(self):
        self.x -= 2
    def draw(self):
        top_height = self.height
        bottom_height = 800 - (self.height + self.gap)
        screen.blit(self.top_pipe, (self.x, top_height - self.top_pipe.get_height()))
        screen.blit(self.bottom_pipe, (self.x, self.height + self.gap))
#=============================================================#
bird = bird()
pipes = []
spawn_pipe = 0
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy bird")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 72)
pipe_image = pygame.image.load('Pipe.png').convert_alpha()
background = pygame.image.load('background_image.png')
score = 0
framewidth = 64
frameheight = 64
row_num = 0
frame_num = 0
bg_x1 = 0
bg_x2 = 64
ticker=0

# 0 columns 50 rows
running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird.flap()
    ticker+=1
    if ticker%100==0:
        ticker = 0
        score+=1
    spawn_pipe += 1
    if spawn_pipe >= 150:
        pipes.append(Pipe(800))
        spawn_pipe = 0
    if ticker%10 == 0:
        frame_num+=1
    if frame_num > 49:
        frame_num = 0
    #---------------Gamephisics---------------#
    for pipe in pipes:
        pipe.move()
        if check_collision(50, bird.y, pipe.x, pipe.height):
            running = False
    i = len(pipes) - 1
    while i >= 0:
        if pipes[i].x <= -50:
            pipes.pop(i)
        i -= 1
    bird.physics()
    #--------------Render section---------------#
    bg_x1 -= 2
    bg_x2 -= 2
    if bg_x1 <= -64:
        bg_x1 = 64
    if bg_x2 <= -64:
        bg_x2 = 64
    screen.blit(background, (0,0), (framewidth*frame_num, row_num*frameheight, framewidth, frameheight))
    ##############################################
    score_text = font.render("Score:", True, (255, 255, 255))
    screen.blit(score_text, (650, 20))
    score_text2 = font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text2, (750, 20))
    for pipe in pipes:
        pipe.draw()
    bird.draw()
    
    pygame.display.flip()
    #--------------End game loop--------------#
text = font2.render("Game Over", True, (255, 50, 50))
screen.blit(text, (200, 200))
pygame.display.flip()
pygame.time.delay(2000)
pygame.quit()
