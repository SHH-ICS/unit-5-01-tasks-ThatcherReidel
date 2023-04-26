import pygame, sys

pygame.init()

Display = pygame.display.set_mode((500,500))

Clock = pygame.time.Clock()
FPS = 60

while True:
    Display.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Draw stuff

    pygame.display.flip()
    Clock.tick(FPS)