import pygame, os, sys, Laser, Enemy, Battlecruiser, Background
from pygame.locals import *
from random import randint

FPS = 50
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
ENMY_MX_SPD = 10
GAME_OVER = False

# Game loop, event handling, collision detection, rendering of score
def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Ram Aras')
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 28)
	score = 0

	# Prepare objects to be used in the game
	background = Background.Background(screen)
	lasers = []
	player = Battlecruiser.Battlecruiser(screen, "assets/battlecruiser.gif", SCREEN_WIDTH/2, 
						   SCREEN_HEIGHT/2, 0, 0)
	enemy  = Enemy.Enemy(screen, 10, 10, randint(-1*ENMY_MX_SPD, ENMY_MX_SPD),
						 randint(-1*ENMY_MX_SPD, ENMY_MX_SPD), player)

	while True:
		time_passed = clock.tick(FPS)
		screen.fill(BACKGROUND_COLOR)
		text = font.render("Score: " + str(score), 1, (255, 255, 255))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					lasers.append(Laser.Laser(screen, "assets/laser.gif", player.x,
								  player.y - (player.image_h/2), 0, -9))
					player.laserClip()
				if (event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or
					event.key == K_RIGHT):
					player.update(event.key)
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

		if GAME_OVER == False:
			background.update()
			background.draw()

			for l in lasers:
				l.update()
				l.draw()

			enemy.update()
			enemy.draw()

			player.update(None)
			player.draw()

			screen.blit(text, (10, 10))

			if pygame.sprite.collide_rect(player, enemy):
				try: 
					sound = pygame.mixer.Sound("assets/death_explode.wav")
					sound.play()
					gameOver(screen)
				except pygame.error, message:
					pass
			
			breakEnemy = False

			for l in lasers:
				if pygame.sprite.collide_rect(enemy, l):
					breakEnemy = True

			if breakEnemy == True:
				enemy.destroy()
				enemy.active = False
				enemy = Enemy.Enemy(screen, 10, 10, randint(-1*ENMY_MX_SPD, ENMY_MX_SPD),
						 randint(-1*ENMY_MX_SPD, ENMY_MX_SPD), player) 
				score += 100
			
			pygame.display.flip()

def gameOver(screen):
	font = pygame.font.Font(None, 45) 
	gameOverText = font.render("GAME OVER", 1, (255, 255, 255))
	screen.blit(gameOverText, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
	global GAME_OVER
	GAME_OVER = True

if __name__ == "__main__":
	main()
