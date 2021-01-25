import random

#This is used to set the title of the game
TITLE = 'Flappy Bird'

WIDTH = 400
HEIGHT = 708

bird = Actor('bird1', (75,200))
pipe_top = Actor('top', (172,250), anchor=('left','bottom'))
pipe_bottom = Actor('bottom',(172,380), anchor=('left','top'))


score = 0

game_status = 0

GRAVITY = 0.3
bird.fall = 0
FLAP_HEIGHT = -6.5
SPEED = 1

GAP = 130

def draw():
    if game_status == 0:
        screen.blit('front',(0,0))
        screen.draw.text("Press ENTER to start", (55, 575), color="white", fontsize=40, shadow=(1, 1))

    elif game_status == 1:

        screen.blit('background',(0,0))
        screen.draw.text(str(score),(300,25),color='white',
        fontsize=70)

        pipe_top.draw()
        pipe_bottom.draw()
        bird.draw()

def start_game():
    global game_status

    # if the game status is zero
    # and if the Enter key on the keyboard is pressed
    # change the game status to 1 and start the game
    if game_status == 0:
        if keyboard.RETURN:
            game_status = 1

def update_bird():

    bird.fall += GRAVITY
    bird.y += bird.fall

    if bird.y > HEIGHT:
        bird.y = 200
        bird.fall = 0

    if bird.fall < -3:
        bird.image = 'bird2'
    else:
        bird.image = 'bird1'

def on_key_down():
    bird.fall = FLAP_HEIGHT


def reset_pipes():
    #the gap can be random, hence the random function is called
    random_pos = random.randint(200, HEIGHT - 200)

    pipe_top.pos = (WIDTH, random_pos - (GAP//2))
    pipe_bottom.pos = (WIDTH, random_pos + (GAP//2))

def update_pipes():
    pipe_top.x -= SPEED
    pipe_bottom.x -= SPEED

    if pipe_top.x < -100:
        reset_pipes()

def update():
    start_game()

    if game_status == 1:
        update_bird()
        update_pipes()

def on_mouse_move(pos):
    print(pos)
