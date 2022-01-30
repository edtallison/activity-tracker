import sys, pygame
import math
pygame.init()

size = width, height = 995, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Activity Tracker')

days = [i*i for i in range(200)]

for i in range(len(days)):
    x_pos = (10 + i*25) % 975
    y_pos = 10 + math.ceil(((i - 38) / 39)) * 25
    colour = (0, 255*days[i]/max(days), 0)
    square = pygame.Surface((20,20))
    square.fill(colour)
    screen.blit(square, (x_pos, y_pos))

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()