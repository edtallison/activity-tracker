import sys, pygame
import math
import random
pygame.init()

size = width, height = 1020, 320
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Activity Tracker')

days = [random.random() for i in range(480)]

for i in range(len(days)):
    x_pos = (10 + i*25) % 1000
    y_pos = 10 + math.ceil(((i - 39) / 40)) * 25
    
    if i == 0:
        colour = (20,20,20)
    else:
        colour = (0, max(255*days[i]/max(days),20), 0)
    square = pygame.Surface((20,20))
    square.fill(colour)
    screen.blit(square, (x_pos, y_pos))

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()