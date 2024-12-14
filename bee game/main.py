import pgzrun
import random

TITLE = "bee game"
WIDTH = 600
HEIGHT = 500

bee = Actor("bee")
flower = Actor("flower")
game_over = False
score = 0
score_text = "your score is: "

def place_random(actor):
    actor.pos = (
        random.randint(100,WIDTH-100),
        random.randint(100,HEIGHT-100)
    )

place_random(bee)
place_random(flower)

def draw():
    screen.blit("bg", (0,0))
    screen.draw.text(
        score_text + str(score), 
        center=(WIDTH/2,50), 
        fontsize=40
    )
    bee.draw()
    flower.draw()

    if game_over:
        screen.fill("pink")
        screen.draw.text("game over. your score is " + str(score), center=(WIDTH/2,50), fontsize=40)


def update():
    global score
    if keyboard.left:
        bee.x -= 10
    elif keyboard.right:
        bee.x += 10
    elif keyboard.up:
        bee.y -= 10
    elif keyboard.down:
        bee.y += 10
    
    if bee.colliderect(flower):
        score += 10
        place_random(flower)

def end_game():
    global game_over
    game_over = True
    

clock.schedule(end_game, 30)
pgzrun.go()