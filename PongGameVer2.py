# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
Speedint = 1.1


time = 0
direction = random.choice(["LEFT","RIGHT"])
score1 = score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, Speed # these are vectors stored as lists
    direction = random.choice(["LEFT","RIGHT"])
    ball_pos = [ WIDTH/2, HEIGHT/2 ]
    
    vel_x, vel_y = random.randrange(120, 240)/60, random.randrange(60, 180)/60
    vel = [vel_x, vel_y]
    
    if direction == "RIGHT":
        ball_vel = vel
        for k,v in enumerate(ball_vel):
            ball_vel[k] = v * Speed
            print ball_vel
        
    elif direction == "LEFT":
        vel[0] = -vel[0]
        ball_vel = vel 
        for k,v in enumerate(ball_vel):
            ball_vel[k] = v * Speed
        
def simple():
    Speedint = 1.1
    new_game(Speedint)

def medium():
    Speedint = 1.3
    new_game(Speedint)

def hard():
    Speedint = 1.5
    new_game(Speedint)
    

    
    
        
     
    

# define event handlers
def new_game(Speedint):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, direction, Speed  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = paddle2_pos = HEIGHT/2
    paddle1_vel = paddle2_vel = 0
    score1 = score2 = 0
    Speed = Speedint
    
    spawn_ball(direction)
    
    
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, Speed
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    gleft = canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    gright = canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
        
    # update ball
    
    
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    
    if (HEIGHT-HALF_PAD_HEIGHT) >= paddle1_pos+ paddle1_vel >= HALF_PAD_HEIGHT :
        paddle1_pos += paddle1_vel
        
        
    if (HEIGHT-HALF_PAD_HEIGHT) >= paddle2_pos + paddle2_vel>= HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
        
    # draw paddles
    # left
    canvas.draw_polygon([(2,paddle1_pos-HALF_PAD_HEIGHT),(PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT),(PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT),
                         (2,paddle1_pos+HALF_PAD_HEIGHT)],PAD_WIDTH,"Yellow")
    # right
    canvas.draw_polygon([(WIDTH-2, paddle2_pos-HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT),
                         (WIDTH-PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT),(WIDTH-2, paddle2_pos+HALF_PAD_HEIGHT)],PAD_WIDTH,"Blue")

    # determine whether paddle and ball collide    
    if  ball_pos[0] <= BALL_RADIUS :
        if (paddle1_pos- HALF_PAD_HEIGHT) <= ball_pos[1] <= (paddle1_pos+ HALF_PAD_HEIGHT):
            ball_vel[0] = (-ball_vel[0])* Speed
        else:
            spawn_ball(direction)
            score2 +=1
            
            
    if  ball_pos[0] >= WIDTH-BALL_RADIUS:
        if (paddle2_pos- HALF_PAD_HEIGHT) <= ball_pos[1] <= (paddle2_pos+ HALF_PAD_HEIGHT):
            ball_vel[0] = (-ball_vel[0])* Speed
        else:
            spawn_ball(direction)
            score1 += 1
        
    # ball reflection- 1
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT- BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
        
    # draw scores
    canvas.draw_text(str(score1), [150, 100], 25, 'White') 
    canvas.draw_text(str(score2), [450, 100], 25, 'White')     
def restart():
    new_game(Speedint)
        
        
def keydown(key):
    global paddle1_vel, paddle2_vel, Speed
    var = 4 * (Speed * 1.1)
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel += -var
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += var
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel += -var
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += var        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
def manual():
    print """For Left-hand-side controller:
    "W" moves paddle upwards
    "S" moves paddle downwards
    """
    print """For Left-hand-side controller:
    "up" moves paddle upwards
    "down" moves paddle downwards
    """
    print """If you miss the ball:
    your opponent will get one point;
    vice versa.
    """
    
    print """Higher difficulty will accelerate
    the ball;
    However, as a compensation:
    the paddle speed will increase as well.
    """
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)
frame.add_button("Simple", simple, 100)
frame.add_button("Medium", medium, 100)
frame.add_button("Hard", hard, 100)
frame.add_button("Manual",manual,100)


# start frame
new_game(Speedint)
frame.start()

