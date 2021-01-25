import random

#This is used to set the title of the game
TITLE = 'Flappy Bird'

WIDTH = 400
HEIGHT = 708

#this is used to keep the gap between the pipes
GAP = 130

#speed of the pipes
SPEED = 3

#maintaining the gravity of the bird
GRAVITY = 0.3

#mainting the flap velocity of the bird, how high the bird will go on_key_down
FLAP_VELOCITY = -6.5

game_status = 0

bird = Actor('bird1', (75,200))
pipe_top = Actor('top', anchor=('left','bottom'))
pipe_bottom = Actor('bottom', anchor=('left','top'))

#the bird status
bird.dead = False
bird.vy = 0
bird.score = 0
level = 1

def draw():

    global level

    if game_status == 0:
        screen.blit('front',(0,0))
        screen.draw.text("Press ENTER to start", (55, 575), color="white", fontsize=40, shadow=(1, 1))

    if game_status == 1:
        screen.blit('background',(0,0))
        screen.draw.text("LEVEL: " + str(level),color='white',midtop=(WIDTH // 2, 10),fontsize=50,shadow=(1, 1))
        screen.draw.text(str(bird.score),color='white',midtop=(WIDTH // 2, 50),fontsize=70,shadow=(1, 1))
        pipe_top.draw()
        pipe_bottom.draw()
        bird.draw()

    if level == 3:
        screen.blit('front',(0,0))
        screen.draw.text("CONGRATULATIONS!!!\nYOU WON!!", (50, 575), color="white", fontsize=40, shadow=(1, 1))
        sounds.die.stop()
        sounds.swooshing.stop()
        sounds.wing.stop()
        #sounds.point.stop()


def start_game():
    global game_status

    if game_status == 0:
        if keyboard.RETURN:
            game_status = 1

def update():
    start_game()

    update_pipes()
    update_bird()

#this function is used to maintain the flap velocity of the bird if the bird is not dead
def on_key_down():
    sounds.wing.play()
    if not bird.dead:
        bird.vy = FLAP_VELOCITY

#assigning the height and positions of the pipes
def reset_pipes():
    #the gap can be random, hence the random function is called
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)

#change the position of the pipes and calculate the level and score
def update_pipes():
    global level
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED

    #if the top pipe reaches the left of the screen
    if pipe_top.right < 0:
        #then reset the pipes
        reset_pipes()
        #if the bird is not dead
        if not bird.dead:
            #increase the bird score and play the point.wav
            #sounds.point.play()
            bird.score += 1
            #if the bird score is more than five
            if bird.score >= 5:
                #increment the level and make the bird score to 0
                sounds.swooshing.play()
                level += 1
                bird.score = 0
        #else if the bird dies
        else:
            bird.score = 0
            level = 1

#this function is mainly to set the velocity of the bird and to change the images on conditions
def update_bird():
    uy = bird.vy
    bird.vy += GRAVITY
    bird.y += bird.vy
    bird.x =75

    if not bird.dead:
        if bird.vy < -3:
            bird.image = 'bird2'
        else:
            bird.image = 'bird1'

    #this checks whether the bird has collided with the wall
    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.dead = True
        bird.image = 'birddead'
        sounds.die.play()

    if not 0 < bird.y < 720:
        bird.y = 200
        bird.dead = False
        bird.vy = 0
        reset_pipes()
