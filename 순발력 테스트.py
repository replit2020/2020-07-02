import pygame
import random

def startmessage():
    global gamepad, start_game
    start_game = False
    gamepad.fill(White)
    font = pygame.font.SysFont('none', 30)
    pab = font.render('Press any Button', 1, Black)
    pabrect = pab.get_rect()
    pabrect.center = (250, 250)
    gamepad.blit(pab, pabrect)

def ballon():




    
def runGame():
  global gamepad, clock
  end_game = False

  startmessage()
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          
  while not end_game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        end_game = True
    
    pygame.display.update()
    clock.tick(60)
  pygame.quit()

def initGame():
  global gamepad, clock, White, Black
  pygame.init()
  White = (255, 255, 255)
  Black = (0,0,0)
  width = 500
  height = 500
  gamepad = pygame.display.set_mode((width, height))
  pygame.display.set_caption('순발력 테스트')
  clock = pygame.time.Clock()
  runGame()

initGame()

