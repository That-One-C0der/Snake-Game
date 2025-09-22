import pygame
import random
pygame.init()
screenSize = (500,500)
screenColor = (255,255,255)
snakeColor = (0,0,0)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(screenSize)
screen.fill(screenColor)
snake = [(5,5),(5,6),(6,6)]
running = True
xdir = 0
ydir = -1
apple = (0,0)
gamerunning = False
startscreen = True
subtextshowing = True
background = pygame.image.load("pixil-frame-0 (1).png")
screen.blit(background,(0,0,500,500))
eyes = pygame.image.load("pixil-frame-0.png")
if startscreen:
    title = pygame.font.SysFont("Consolas", 50, bold=False, italic=False)
    title_surface = title.render("Snake Game",True,(100,100,100))
    subtext = pygame.font.SysFont("Consolas", 20, bold=False, italic=False)
    subtext_surface = subtext.render("Press \"S\" to start",True,(100,100,100))
    pygametext = pygame.font.SysFont("Consolas", 10, bold=False, italic=False)
    pygametext_surface = pygametext.render("Made with Pygame",True,(100,100,100))
clockspeed = 5
def drawsnake():
    for i in snake:
        pygame.draw.rect(screen,(100,100,100),(i[0]*50,i[1]*50,50,50))
    screen.blit(eyes,(snake[0][0]*50,snake[0][1]*50,50,50))
def shiftsnake():
    snake.insert(0,(snake[0][0]+xdir,snake[0][1]+ydir))
    snake.pop()
    if(snake[0][0]<0 or snake[0][0]>10 or snake[0][1]<0 or snake[0][1]>10):
        return False
    else:
        return True
def spawnapple():  
    return (random.randint(0,9),random.randint(0,9))
def drawapple():
    pygame.draw.rect(screen,(255,0,0),(apple[0]*50,apple[1]*50,50,50))  
print(pygame.font.get_fonts())
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :  # Checks if the user clicked the close button
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT and xdir == 0:
                xdir = -1
                ydir = 0
            if event.key == pygame.K_RIGHT and xdir == 0:
                xdir = 1
                ydir = 0 
            if event.key == pygame.K_UP and ydir == 0:
                ydir = -1
                xdir = 0
            if event.key == pygame.K_DOWN and ydir == 0:
                ydir = 1
                xdir = 0
            if event.key == pygame.K_s:
                    startscreen = False
                    gamerunning = True
    if gamerunning:
        running = shiftsnake()
        screen.blit(background,(0,0,500,500))
        if snake[0] == apple:
            apple = spawnapple()
            snake.append(((snake[0][0]+xdir,snake[0][1]+ydir)))
        drawapple()
        drawsnake()
        pygame.display.flip()
        clockspeed = 5 
    elif startscreen:
        screen.fill(screenColor)
        screen.blit(title_surface,(50,100))
        screen.blit(pygametext_surface,(10,480))
        if subtextshowing:
            screen.blit(subtext_surface,(50,150))
        subtextshowing = not subtextshowing
        pygame.display.flip()
        clockspeed = 3
        
    clock.tick(clockspeed)
pygame.quit()