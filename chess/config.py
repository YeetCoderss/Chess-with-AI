import os
import pygame

class Config:
	def __init__(self):
		self.move_sound = pygame.mixer.Sound(os.path.join(
			"assets/sounds/move.wav"))

		self.capture_sound = pygame.mixer.Sound(os.path.join(
			"assets/sounds/capture.wav"))


	def play_sound(self, sound):
		pygame.mixer.Sound.play(sound)