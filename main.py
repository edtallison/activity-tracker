import sys, pygame
pygame.init()

size = width, height = 1000, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Activity Tracker')

green = 0, 255, 0

for i in range(30):
    square = pygame.Surface((20,20))
    square.fill(green)
    screen.blit(square, (10+25*i, 10))

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()