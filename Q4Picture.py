import pygame

# Initialize pygame
pygame.init()

# Set up the window
window_size = (400, 400)
window = pygame.display.set_mode(window_size)

# Set up the colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Draw a rectangle
pygame.draw.rect(window, red, pygame.Rect(50, 50, 100, 100))

# Draw a circle
pygame.draw.circle(window, green, (250, 250), 50)

# Draw a line
pygame.draw.line(window, blue, (0, 0), (400, 400), 5)

# Update the screen
pygame.display.update()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()