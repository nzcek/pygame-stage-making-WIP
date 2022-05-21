import pygame
from tiles import Tile
from player import Player

levelLayout = [
'                                   ',
'                                   ',
'  XXX                  XXXXX       ',
'								    ',
'       XXXXXXXXX                   ',
'                                   ',
'                                   ',
'                XX  XXXXXXXXXXX    ',
'                XX  XXXXXXXXXXX    ',
'           XXXX XX  XXXXXXXXXXX    ',
' P    XX   XXXX XX  XXXXXXXXXXX    ',
'XXXXXXXX XXXXXX XX  XXXXXXXXXXX    ']

tileSize = 64
screenWidth = 1200
screenHeight = len(levelLayout)*tileSize

class Level:
	def __init__(self, levelData, surface):
		self.display_surface = surface
		self.makeLevel(levelData)

		self.levelShift = 0

	def makeLevel(self, layout):
		self.tiles = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()

		for row_index, row in enumerate(layout):
			for column_index, point in enumerate(row):
				print(f'{row_index},{column_index}:{point}')
				
				x = column_index * tileSize
				y = row_index * tileSize
				
				if point == "X":
					
					tile = pygame.sprite.Group(Tile((x,y), tileSize))
					self.tiles.add(tile)
				if point == "P":
					
					playerSprite = Player((x,y))
					self.player.add(playerSprite)
	
	def scrollX(self):
		player = self.player.sprite
		playerX = player.rect.centerx
		directionX = player.direction.x

		if playerX < screenWidth/4 and directionX < 0:
			self.levelShift = 6
			player.speed = 0
		elif playerX > screenWidth - (screenWidth/4) and directionX > 0:
			self.levelShift = -6
			player.speed = 0
		else:
			self.levelShift = 0
			player.speed = 6

	def horizontalMovementCollision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x *player.speed

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.x < 0:
					player.rect.left = sprite.rect.right
				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left

	def verticalMovementCollision(self):
		player = self.player.sprite
		player.gravity()

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom


	def run(self):
		
		self.tiles.update(self.levelShift)
		self.tiles.draw(self.display_surface)

		self.player.update()
		self.player.draw(self.display_surface)
		self.scrollX()
		self.horizontalMovementCollision()
		self.verticalMovementCollision()