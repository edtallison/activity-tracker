import sys, pygame
import math
pygame.init()

size = width, height = 1000, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Activity Tracker')

days = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]*9

for i in range(len(days)):
    x_pos = (10 + i*25) % 950
    y_pos = 25 + math.ceil(((i - 49) / 40)) * 25
    colour = (0, 255*days[i]/max(days), 0)
    square = pygame.Surface((20,20))
    square.fill(colour)
    screen.blit(square, (x_pos, y_pos))

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()