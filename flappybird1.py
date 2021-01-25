import random

#This is used to set the title of the game
TITLE = 'Flappy Bird'

WIDTH = 400
HEIGHT = 708

bird = Actor('bird1', (75,200))
pipe_top = Actor('top', (172,0))
pipe_bottom = Actor('bottom',(172,707))

score = 0

def draw():
    screen.blit('background',(0,0))
    screen.draw.text(str(score),(300,25),color='white',
    fontsize=70)

    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()

def on_mouse_move(pos):
    print(pos)
