# -*- coding: Utf-8 -*

"""
Game MacGyver escapes ! (mge)
Control the hero and collect the 3 items before reaching the end of the labyrinth.

Although the game is working as intended in this version, the code is extremely clunky, major change are coming shortly

Coded in Python
Files : mge_game.py, classes.py, constants.py, n2 and images folder
"""

import pygame
import random
from pygame.locals import *

from classes import *
from constants import *

pygame.init()

#Opening of the initial window, initial size of 450*500
window = pygame.display.set_mode((side_window, side_window + height_inventory_space))

icon = pygame.image.load(image_window_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption(window_title)

#MAIN LOOP
continue_main = 1
while continue_main:	
	#Loading and display of home window
	home = pygame.image.load(image_main_menu).convert()
	window.blit(home, (0,0))

	pygame.display.flip()

	#Variables for the different loops
	continue_game = 1
	continue_home = 1
	continue_victory_screen = 0
	continue_death_screen = 0


	#HOME LOOP
	while continue_home:
	
		#Loop speed limitation
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#End of all the loops if escape is pressed, works at any moment of the game
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continue_home = 0
				continue_game = 0
				continue_main = 0
				#Variable for a level choice in case of new additions
				choice = 0
			
			#Here is the line of code that need to be changed if there is new levels	
			elif event.type == KEYDOWN and event.key != K_ESCAPE:				
				continue_home = 0
				choice = 'level1'

	#Check if a choice as been made by the user, in case of future levels and user input required
	if choice != 0:
		
		#Creation and loading of the level + characters and objects
		fond = pygame.image.load(image_floor).convert()
		inventory = pygame.image.load(image_inventory).convert()	
		
		level = Level(choice)
		level.generate()
		level.show_game(window)

		macgyver = Hero(image_hero, level)
		badguy = Enemy(image_badguy, level, 13, 14, 390, 420)


		#Really clunky way of random position for objects, will be changed
		#We assign random x and y position for the 3 objects directly
		#and test they are not similar or ending in a wall
		object1_case_y = 14
		object1_case_x = 14
		object2_case_y = 14
		object2_case_x = 14
		object3_case_y = 14
		object3_case_x = 14

		while level.structure[object1_case_y][object1_case_x] != 'O' or level.structure[object2_case_y][object2_case_x] != 'O' or level.structure[object3_case_y][object3_case_x] != 'O':

			object1_case_y = random.randint(0,14)
			object1_case_x = random.randint(0,14)
			object2_case_y = random.randint(0,14)
			object2_case_x = random.randint(0,14)
			object3_case_y = random.randint(0,14)
			object3_case_x = random.randint(0,14)

			if object1_case_y == object2_case_y and object1_case_x == object2_case_x:
				object2_case_y = 14
				object2_case_x = 14
			elif object1_case_y == object3_case_y and object1_case_x == object3_case_x:
				object3_case_y = 14
				object3_case_x = 14
			elif object3_case_y == object2_case_y and object3_case_x == object2_case_x:
				object3_case_y = 14
				object3_case_x = 14

		#Creation of the 3 objects with the random x and y attributed above
		object1 = QuestObjects(image_object1, level, object1_case_x, object1_case_y)
		object2 = QuestObjects(image_object2, level, object2_case_x, object2_case_y)
		object3 = QuestObjects(image_object3, level, object3_case_x, object3_case_y)
		
		#Counter for the object, hero need that variable to be at 3 to finish the game
		object_count = 0




	#GAME LOOP
	while continue_game:

		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continue_game = 0
				continue_main = 0

			#Massive code, need to find a way to reduce the hard move of objects to inventory
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT:
					macgyver.move('right')
					if macgyver.x == object1.x and macgyver.y == object1.y :
						object1.move_inventory(150,460)
						object_count += 1
					elif macgyver.x == object2.x and macgyver.y == object2.y :
						object2.move_inventory(200,460)
						object_count += 1
					elif macgyver.x == object3.x and macgyver.y == object3.y :
						object3.move_inventory(250,460)
						object_count += 1
				elif event.key == K_LEFT:
					macgyver.move('left')
					if macgyver.x == object1.x and macgyver.y == object1.y :
						object1.move_inventory(150,460)
						object_count += 1
					elif macgyver.x == object2.x and macgyver.y == object2.y :
						object2.move_inventory(200,460)
						object_count += 1
					elif macgyver.x == object3.x and macgyver.y == object3.y :
						object3.move_inventory(250,460)
						object_count += 1
				elif event.key == K_UP:
					macgyver.move('up')
					if macgyver.x == object1.x and macgyver.y == object1.y :
						object1.move_inventory(150,460)
						object_count += 1
					elif macgyver.x == object2.x and macgyver.y == object2.y :
						object2.move_inventory(200,460)
						object_count += 1
					elif macgyver.x == object3.x and macgyver.y == object3.y :
						object3.move_inventory(250,460)
						object_count += 1
				elif event.key == K_DOWN:
					macgyver.move('down')
					if macgyver.x == object1.x and macgyver.y == object1.y :
						object1.move_inventory(150,460)
						object_count += 1
					elif macgyver.x == object2.x and macgyver.y == object2.y :
						object2.move_inventory(200,460)
						object_count += 1
					elif macgyver.x == object3.x and macgyver.y == object3.y :
						object3.move_inventory(250,460)
						object_count += 1

				#Instant death for random test
				#elif event.key == K_d:
				#	continue_game = 0


		#Display of graphic elements
		window.blit(fond, (0,0))
		window.blit(inventory, (0,450))

		level.show_game(window)

		window.blit(badguy.sprite, (badguy.x, badguy.y))
		window.blit(object1.sprite, (object1.x, object1.y))
		window.blit(object2.sprite, (object2.x, object2.y))
		window.blit(object3.sprite, (object3.x, object3.y))
		window.blit(macgyver.direction, (macgyver.x, macgyver.y))

		pygame.display.flip()

		#Condition for putting the badguy to sleep, dying and winning base on the level structure
		#T in file stand for 'Test', where the program test if the user got the 3 items or not
		#If he does, the guard sleeps and he can progress to the Finish (F) case
		if level.structure[macgyver.case_y][macgyver.case_x] == 'T' and object_count == 3:
			badguy.sleep(image_badguy_sleeping, level, 13, 14, 390, 420)
			window.blit(badguy.sprite, (badguy.x, badguy.y))
			pygame.display.flip()

		if level.structure[macgyver.case_y][macgyver.case_x] == 'T' and object_count < 3:
			continue_death_screen = 1

		if level.structure[macgyver.case_y][macgyver.case_x] == 'F':
			continue_victory_screen = 1


		#VICTORY SCREEN LOOP
		while continue_victory_screen:
			
			pygame.time.Clock().tick(30)
			for event in pygame.event.get():
			
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					continue_home = 0
					continue_game = 0
					continue_victory_screen = 0
					continue_main = 0
					
				elif event.type == KEYDOWN and event.key != K_ESCAPE:				
					continue_victory_screen = 0
					continue_game = 0

			victory_screen = pygame.image.load(image_victory_screen).convert()
			window.blit(victory_screen, (0,0))
			pygame.display.flip()

		#DEATH SCREEN LOOP
		while continue_death_screen:
			
			pygame.time.Clock().tick(30)
			for event in pygame.event.get():
			
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					continue_home = 0
					continue_game = 0
					continue_victory_screen = 0
					continue_death_screen = 0
					continue_main = 0
					
				elif event.type == KEYDOWN and event.key != K_ESCAPE:				
					continue_death_screen = 0
					continue_game = 0

			death_screen = pygame.image.load(image_death_screen).convert()
			window.blit(death_screen, (0,0))
			pygame.display.flip()

