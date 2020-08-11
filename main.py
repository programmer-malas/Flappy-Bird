"""
Made By Rafli
Please dont delete this credit
"""
import pygame
import random as rd

pygame.init()
win_w = 1280
win_h = 720
win = pygame.display.set_mode((win_w, win_h))
clock = pygame.time.Clock()

class Burung():
    def __init__(self):
        self.x = win_w * 0.2
        self.y = win_h * 0.5
        self.vsp = 0
        self.jumpsp = win_h * 0.015
        self.grv = win_h*0.00069
        self.body = pygame.Rect(self.x, self.y, win_h*0.05, win_h*0.05)

    def jump(self):
        self.vsp = -self.jumpsp
    
    def move(self):
        self.vsp += self.grv
        self.y += self.vsp
        self.body.y = self.y
    
    def checkForDeath(self, obstacles):
        for obstacle in obstacles:
            if burung.body.colliderect(obstacle) or burung.body.colliderect(pygame.Rect(
                obstacle.x,
                obstacle.y-win_h*1.25,
                obstacle.width,
                obstacle.height
            )):
                pygame.quit()

class ObstaclesManager():
    def __init__(self):
        self.obstacles_list = []
    
    def generateObstacles(self):
        can_gen = True
        for obstacle in self.obstacles_list:
            if obstacle.x > win_w*0.75:
                can_gen = False
        
        if can_gen:
            self.obstacles_list.append(pygame.Rect(
                win_w,
                rd.randint(win_h*0.25, win_h*0.8),
                win_w*0.075,
                win_h
            ))
    
    def scrollScene(self):
        for obstacle in self.obstacles_list:
            obstacle.x -= win_w*0.0025
            if obstacle.x < 0 - obstacle.width:
                self.obstacles_list.remove(obstacle)

manager = ObstaclesManager()
burung = Burung()

game_resumed = False
pygame.display.set_caption("Flappy Bird")

while True:
    clock.tick(60)
    win.fill((36, 136, 163))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                burung.jump()
                game_resumed = True
    
    if game_resumed:
        manager.generateObstacles()
        manager.scrollScene()
        burung.move()
        burung.checkForDeath(obstacles = manager.obstacles_list)

    pygame.draw.rect(win, (255, 174, 0), burung.body)
    for obstacle in manager.obstacles_list:
        pygame.draw.rect(win, (0, 255, 8), obstacle)
        pygame.draw.rect(win, (0, 255, 8), pygame.Rect(
            obstacle.x,
            obstacle.y-win_h*1.25,
            obstacle.width,
            obstacle.height
        ))

    pygame.display.update()
