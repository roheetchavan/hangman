import pygame
import math
import random

# Setup Window
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('--:: HANGMAN ::--')

# Setup Buttons
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400

def display_letters():
  letters.clear()
  A = 65
  for i in range(26):
      x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
      y = starty + ((i // 13) * (GAP + RADIUS * 2))
      letters.append([x, y, chr(A + i), True])

# Setup fonts
LETTER_FONT = pygame.font.SysFont('comincsans', 40)
WORD_FONT = pygame.font.SysFont('comincsans', 60)
TITLE_FONT = pygame.font.SysFont('comincsans', 70)

# Load images
images = []
for i in range(7):
    img_name = 'hangman'+ str(i) + '.png'    
    img = pygame.image.load(img_name)
    print(img)
    images.append(img)

# Game variable
hangman_status = 0
words = ['C', 'CPP', 'PYTHON', 'JAVA', 'PERL']
word = random.choice(words)
guessed = []

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)

def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("Guess the word to save him!", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ''
    for letter in word:
        if letter in guessed:
            display_word += letter + ' '
        else:
            display_word += '_ '
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons 
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

# Setup Game loop
FPS = 60
clock = pygame.time.Clock()
run = True


def main():
    global hangman_status
    global run

    # Reset status
    hangman_status = 0
    guessed.clear()
    display_letters()    
    while run:
      clock.tick(FPS)
    
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          m_x, m_y = pygame.mouse.get_pos()
          for letter in letters:
            x, y, ltr, visible = letter
            if visible:
              dist = math.sqrt((x-m_x)**2  + (y-m_y)**2)
              if dist < RADIUS:
                letter[3] = False
                guessed.append(ltr)
                if ltr not in word:
                  hangman_status += 1

      draw()
    
      won  = True
      for letter in word:
        if letter not in guessed:
          won = False
          break            

      if won:
        display_message('YOU WON!')
        break

      if hangman_status == 6:
        display_message('YOU LOST!')
        break

while run: 
    main()

pygame.quit()
