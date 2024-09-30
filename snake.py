import random
import sys
import pygame

#khoi tao
pygame.init()
pygame.display.set_caption("snake game")

length=600
height=600

screen=pygame.display.set_mode((length, height))

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
GREY=(130, 130, 130)
YELLOW=(255, 255, 0)
GREEN=(0, 255, 0)

x, y=60, 60
dx, dy=0, 0
speed=10
snake_len=15

food_x, food_y=60, 60
food_size=snake_len

quit_game=False
step=15

clock=pygame.time.Clock()

score=0
best_score=0

snake_body=[(x, y)]

def start(): #ham khoi tao game
    global x, y, dx, dy, snake_len, score, snake_body
    snake_len=15
    x=random.randint(0, (length-snake_len)//step)*step
    y=random.randint(0, (height-snake_len)//step)*step
    dx, dy=0, 0
    score=0

    snake_body.clear()

def show_game_over(): #ham ket thuc-tiep tuc neu game over
    #ve con ran va thuc an
    pygame.draw.rect(screen, WHITE, (food_x, food_y, food_size, food_size))
    for part in snake_body:
        pygame.draw.rect(screen, GREEN, (*part, snake_len, 15))

    font=pygame.font.SysFont(None, 30)
    text=font.render('Game Over! Press "C" to Play Again or "ESC" to Quit', True, BLACK)
    font=pygame.font.SysFont(None, 50)
    point=font.render("YOUR SCORE: "+str(score), True, BLACK)
    font=pygame.font.SysFont(None, 35)
    best_point=font.render("(best score: "+str(best_score)+')', True, BLACK)

    screen.blit(text, (55, height//2-35))
    screen.blit(point, (145, height//2+25))
    screen.blit(best_point, (180, height//2+65))

    pygame.display.update()

    #cac thao tac
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys=pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_c]:
            return

def random_food(): #ham xuat hien thuc an
    global food_x, food_y
    food_x=random.randint(0, (length-food_size)//food_size)*food_size
    food_y=random.randint(0, (length-food_size)//food_size)*food_size

def game_loop_main(): #ham main cua game
    global x, y, dx, dy, quit_game, score, best_score, snake_body, speed
    start()
    random_food()

    game_over=False

    while not quit_game:
        screen.fill(GREY)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        #cac nut di chuyen
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and dx!=step:
            dx=-step
            dy=0
        if keys[pygame.K_RIGHT] and dx!=-step:
            dx=step
            dy=0
        if keys[pygame.K_UP] and dy!=step:
            dx=0
            dy=-step
        if keys[pygame.K_DOWN] and dy!=-step:
            dx=0
            dy=step

        x+=dx
        y+=dy

        #neu dam vao tuong hoac vao than - ban thua
        if x<0 or x>length-15 or y<0 or y>height-15 or (x, y) in snake_body[:-1]:
            game_over=True

        if game_over:
            show_game_over()
            start()
            game_over=False

        #an thuc an cong diem
        while food_x==x and food_y==y :
            score+=1
            best_score=max(best_score, score)
            random_food()

        while (food_x, food_y) in snake_body:
            random_food()

        snake_body.append((x, y))
        if len(snake_body)>score+1:
            del snake_body[0]

        #so diem ban dang co
        font=pygame.font.SysFont(None, 25)
        text=font.render(str(score), True, YELLOW)
        screen.blit(text, (length//2, 40))

        #ve ran va thuc an
        pygame.draw.rect(screen, WHITE, (food_x, food_y, food_size, food_size))
        for part in snake_body:
            pygame.draw.rect(screen, GREEN, (*part, snake_len, 15))

        #tang toc moi 15 diem
        speed=15+score//15

        #toc do di chuyen
        clock.tick(speed)

        pygame.display.update()

game_loop_main()

pygame.quit()

"""
    NGUYEN VU QUANG _ B23DCVT363
"""
