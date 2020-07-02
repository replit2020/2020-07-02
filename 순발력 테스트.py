import pygame
import random
import time

pygame.init()
White = (255, 255, 255)
Black = (0,0,0)
width = 500
height = 500
ran = 1
font = pygame.font.SysFont('none', 30)

def printmessage(msg, color=Black, pos=(250,250)):
    textsurface = font.render(msg, True, Black)
    textrect = textsurface.get_rect()
    textrect.center = pos
    gamepad.blit(textsurface, textrect)

def pop():
    global gamepad, x1, y1
    x1 = random.randint(50, 450)
    y1 = random.randint(50, 450)
    pygame.draw.circle(gamepad, Black, [x1, y1], 30, 2)

def pop2():
    global gamepad, x2, y2
    x2 = random.randint(50, 450)
    y2 = random.randint(50, 450)
    pygame.draw.rect(gamepad, Black, [x2-25, y2-25, 50, 50], 2)

def pop3():
    global gamepad, x3, y3
    x3 = random.randint(50, 450)
    y3 = random.randint(50, 450)
    pygame.draw.polygon(gamepad, Black, [[x3, y3-34], [x3-30, y3+17], [x3+30, y3+17]], 2)

   
def runGame1():
  global gamepad
  start_game = False
  middle_game1 = False
  end_game = False
  while not start_game:
      gamepad.fill(White)
      printmessage('Press any Key')
      pygame.display.update()
      for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
              start_game = True
  while not middle_game1:
      gamepad.fill(White)
      printmessage('Click Circle')
      pop()
      pygame.display.update()
      while not middle_game1:
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if x1-30 < pos[0] < x1+30 and y1-30 < pos[1] < y1+30:
              gamepad.fill(White)
              printmessage("This time We're Recording Time")
              pygame.display.update()
              time.sleep(1.5)
              middle_game1 = True
              runGame2()
  
def runGame2():
  middle_game2 = False
  gamepad.fill(White)
  printmessage('Get Ready and Press any Key')
  pygame.display.update()
  while not middle_game2:
      for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            gamepad.fill(White)
            pop()
            pop2()
            pop3()
            if 3 < ran < 7:
                printmessage("Click Rectangle")
                start_time = pygame.time.get_ticks()
                pygame.display.update()
                while not middle_game2:                                                                      
                  for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                      pos2 = pygame.mouse.get_pos()               
                      if x2-25 < pos2[0] < x2+25 and y2-25 < pos2[1] < y2+25:
                        end_time = pygame.time.get_ticks()
                        time_taken = end_time - start_time                       
                        tt = "{0:.3f}".format(time_taken/1000)
                        gamepad.fill(White)
                        printmessage("You've taken %s sec" %tt)
                        pygame.display.update()
                        middle_game2 = True
                        time.sleep(2)
                        retry()       
            if ran < 4:
                printmessage("Click Circle")
                start_time = pygame.time.get_ticks()
                pygame.display.update()
                while not middle_game2:                                                                      
                  for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                      pos2 = pygame.mouse.get_pos()               
                      if x1-28 < pos2[0] < x1+28 and y1-28 < pos2[1] < y1+28:
                        end_time = pygame.time.get_ticks()
                        time_taken = end_time - start_time                       
                        tt = "{0:.3f}".format(time_taken/1000)
                        gamepad.fill(White)
                        printmessage("You've taken %s sec" %tt)
                        pygame.display.update()
                        middle_game2 = True
                        time.sleep(2)
                        retry()
            if ran > 6:
                printmessage("Click Triangle")
                start_time = pygame.time.get_ticks()
                pygame.display.update()
                while not middle_game2:                                                                      
                  for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                      pos2 = pygame.mouse.get_pos()               
                      if x3-25 < pos2[0] < x3+25 and y3-25 < pos2[1] < y3+17:
                        end_time = pygame.time.get_ticks()
                        time_taken = end_time - start_time                       
                        tt = "{0:.3f}".format(time_taken/1000)
                        gamepad.fill(White)
                        printmessage("You've taken %s sec" %tt)
                        pygame.display.update()
                        middle_game2 = True
                        time.sleep(2)
                        retry()

def retry():
    global ran
    pygame.init()
    ran = random.randint(1, 9)
    runGame2()

def initGame():
  global gamepad
  pygame.init()
  gamepad = pygame.display.set_mode((width, height))
  pygame.display.set_caption('순발력 테스트')
  gamepad.fill(White)
  runGame1()

initGame()
