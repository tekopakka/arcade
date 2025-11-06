import sys
import pygame
# from snake import Snake
from map import Map
#from food import Food

def restart():
    res = input("Dead, try again?")
    if res:
        run()

def run():
    print("Running Snake")
    running = True
    pygame.init()
    screen = pygame.display.set_mode((900,900))
    clock = pygame.time.Clock()
    
    map = Map()
    # snake = Snake()
    # food = Food()
    dead = False
    
    while running:
        screen.fill("gray")
        if dead:
            restart()
            break
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit(0)
            
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                pass
                # snake.handle_movement()
                
        # if not snake.move():
        #     dead = True
        # snake.draw()
        map.draw(screen)
        # food.draw()
        
        pygame.display.flip()
        clock.tick(60)
        
