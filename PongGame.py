import pygame,sys
pygame.init()

WHITE = [255,255,255]
BLACK = [0,0,0]
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
CIRCLE_RADIUS = 25
PADDLE_WIDTH = 25
PADDLE_HEIGHT = 200

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

class Paddle:
    def __init__(self, xp):
       self.pxpos = xp
       self.pypos = SCREEN_HEIGHT/2

class Ball:
    def __init__(self):
        self.bxpos = SCREEN_WIDTH/2
        self.bypos = SCREEN_HEIGHT/2
        self.bvely = 0.3
        self.bvelx = 0.3
    def movement(self):
        if self.bypos >= (SCREEN_HEIGHT - CIRCLE_RADIUS) or self.bypos <= CIRCLE_RADIUS:
            self.bvely *= -1
        self.bypos += self.bvely
        self.bxpos += self.bvelx

p1 = Paddle(SCREEN_WIDTH - 50)
p2 = Paddle(50)
ball = Ball()
p1score = 0
p2score = 0
def collision():
    if ball.bxpos + CIRCLE_RADIUS >= p1.pxpos:
        if (((p1.pypos + PADDLE_HEIGHT) >= (ball.bypos - CIRCLE_RADIUS) and (p1.pypos <= (ball.bypos + CIRCLE_RADIUS)))):
            ball.bvelx *= -1
            
    if ball.bxpos - CIRCLE_RADIUS <= p2.pxpos + PADDLE_WIDTH:
        if ((p2.pypos + PADDLE_HEIGHT) >= (ball.bypos - CIRCLE_RADIUS) and (p2.pypos <= (ball.bypos + CIRCLE_RADIUS))):
            ball.bvelx *= -1
            
def reset(p1score, p2score):
    if ball.bxpos + CIRCLE_RADIUS > SCREEN_WIDTH:
        p2score += 1
        ball.bxpos = SCREEN_WIDTH/2
        ball.bypos = SCREEN_HEIGHT/2
        print(p2score)
    
        

    if ball.bxpos - CIRCLE_RADIUS < 0:
        p1score += 1
        ball.bxpos = SCREEN_WIDTH/2
        ball.bypos = SCREEN_HEIGHT/2
        print(p1score)
    return [p1score, p2score]
        


font = pygame.font.SysFont(None, 50)
while True:
    #Step 1: Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
       
            
       

    #Step 2: Calculations / Update variables / positions / etc
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p1.pypos -= 1
    if keys[pygame.K_DOWN]:
        p1.pypos += 1
    if keys[pygame.K_w]:
        p2.pypos -= 1
    if keys[pygame.K_s]:
        p2.pypos += 1
    collision()     
    ball.movement()
    p1score, p2score = reset(p1score, p2score)
    #Step 3: Fill the screen with background color (usually white)
    screen.fill(BLACK)

    #Step 4: Draw your stuff
    img = font.render(str(p1score), True, WHITE)
    screen.blit(img, (1450, 20))
    img2 = font.render(str(p2score), True, WHITE)
    screen.blit(img2, (20, 20))
    
    pygame.draw.circle(screen, WHITE, [ball.bxpos, ball.bypos], CIRCLE_RADIUS)
    pygame.draw.rect(screen, WHITE, [p1.pxpos, p1.pypos, PADDLE_WIDTH, PADDLE_HEIGHT])
    pygame.draw.rect(screen, WHITE, [p2.pxpos, p2.pypos, PADDLE_WIDTH, PADDLE_HEIGHT])
    
    #Step 5: Flip the screen
    pygame.display.flip()
