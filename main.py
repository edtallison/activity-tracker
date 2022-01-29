import sys, pygame
pygame.init()

size = width, height = 1000, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Activity Tracker')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()