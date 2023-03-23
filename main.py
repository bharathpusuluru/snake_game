import pygame
import random
pygame.init()

red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
game_window = pygame.display.set_mode((900,500))

pygame.display.set_caption("First game ")

exit_game = False
snake_x = 45
snake_y =  55
snake_size = 10
fps = 30

font = pygame.font.SysFont(None, 55)

def text_screen(text , color , x ,  y):
    screen_text = font.render(text,True,color)
 
    game_window.blit(screen_text , [x,y])

score = 0 

speed_x = 0
speed_y = 0


food_x = random.randint(20, 900/2)
food_y = random.randint(20, 500/2)

clock = pygame.time.Clock()



while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit_game = True
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                speed_x = 10
                speed_y = 0
            if event.key == pygame.K_LEFT:
                speed_x = -10
                speed_y = 0 
            if event.key == pygame.K_DOWN:
                speed_y = 10
                speed_x = 0
            if event.key == pygame.K_UP:
                speed_y = - 10
                speed_x = 0
    snake_x = snake_x + speed_x    
    snake_y = snake_y + speed_y 
    if (snake_x>900 or snake_y>500) or (snake_x<0 or snake_y<0):
                exit_game = True 
                print('The Score is: ',score*10)  
    #print(speed_x)
    if abs(snake_x - food_x)<9 and abs(snake_y - food_y)<9:
        score = score+1
        print("Score: ",score)
        food_x = random.randint(20, 900/2)
        food_y = random.randint(20, 500/2)
    game_window.fill(white)
    text_screen("Score: "+str(score*10), red, 5, 5)
    pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size,snake_size])
    pygame.draw.rect(game_window, red, [food_x, food_y, snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)
        