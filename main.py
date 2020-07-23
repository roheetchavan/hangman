import pygame

# Setup Window
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('--:: HANGMAN ::--')

# Load images
images = []
for i in range(7):
    img_name = 'hangman'+ str(i) + '.png'    
    img = pygame.image.load(img_name)
    print(img)
    images.append(img)

# Game variable
hangman_status = 0

# Colours
WHITE = (255,255,255)

# Setup Game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    win.fill(WHITE)
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
pygame.quit()
