import sys, pygame
pygame.init()

size = width, height = 1000, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Activity Tracker')

days = [5,1,0,10,8,7,6,4,3,8,9,0,5]

# green = 0, 255, 0

for i in range(len(days)):
    colour = (0, 255*days[i]/max(days), 0)
    square = pygame.Surface((20,20))
    square.fill(colour)
    screen.blit(square, (10+25*i, 10))

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()