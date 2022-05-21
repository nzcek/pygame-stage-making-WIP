import pygame
import sys
from settings import *
from level import Level
from tiles import Tile
from player import Player

pygame.init()

screen = pygame.display.set_mode((screenWidth,screenHeight))
clock = pygame.time.Clock()
level = Level(levelLayout, screen)
testTile = pygame.sprite.Group(Tile((100,100), 200))

while True:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
	
	screen.fill('black')
	level.run()

	pygame.display.update()
	clock.tick(60)