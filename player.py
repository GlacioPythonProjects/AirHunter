import sys
import pygame

class Player:
    def __init__(self):
        
        # Enter your code here
        
        pass

    def action(self, spaceship, asteroid_ls, bullet_ls, fuel, score):
        
        thrust = False 
        right = False 
        left = False
        bullet = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: # left
            left = True
        if keys[pygame.K_d]: # right
            right = True
        if keys[pygame.K_w]: # up
            thrust = True
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
     
        return (thrust, left, right, bullet)

    # You can add additional methods if required
 