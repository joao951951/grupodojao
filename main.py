import sys

import pygame
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
losango = [(50, 30), (250, 250), (200, 300), (150, 250)]
pygame.display.set_caption('Hello World!')
while True:
  pygame.draw.rect(DISPLAYSURF, (255, 255, 255), pygame.Rect(2, 1, 380, 275))
  pygame.draw.rect(DISPLAYSURF, (0, 0, 205), pygame.Rect(2, 1, 100, 100))
  pygame.draw.polygon(DISPLAYSURF, (255, 255, 255),
                      ((80, 80), (45, 8), (10, 80)))
  pygame.draw.rect(DISPLAYSURF, (200, 0, 0), pygame.Rect(100, 44, 282, 57))
  pygame.draw.rect(DISPLAYSURF, (200, 0, 0), pygame.Rect(2, 155, 380, 57))
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
