import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.Surface((32, 64))
		self.image.fill("blue")
		self.rect = self.image.get_rect(topleft = pos)
		
		

		self.speed = 6
		self.direction = pygame.math.Vector2(0, 0)
		self.playerGravity = 0.8
		self.jumpSpeed = -16

	def inputs(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0
		if keys[pygame.K_SPACE]:
			self.jump()

	def gravity(self):
		self.direction.y += self.playerGravity
		self.rect.y += self.direction.y

	def jump(self):
		self.direction.y = self.jumpSpeed



	def update(self):
		self.inputs()
		