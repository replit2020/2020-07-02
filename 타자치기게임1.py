import pygame
import random


WHITE = (255, 255, 255)
pad_width = 500
pad_height = 500


def runGame():
  global gamepad
  end_game = False
  while not end_game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        end_game = True
    gamepad.fill(WHITE)
    pygame.display.update()
  pygame.quit()

def initGame():
  global gamepad
  pygame.init()
  gamepad = pygame.display.set_mode((pad_width, pad_height))
  pygame.display.set_caption('타자 치기 게임')
  runGame()

initGame()
