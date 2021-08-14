# template for "Stopwatch: The Game"
import simplegui
# define global variables
t = 0
canvas_w = 300
canvas_h = 300
timer_int = 100
current = 0
A = 0
B = 0
C = 0
D = 0
x, y = 0, 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A, B, C, D
    A = t // 600
    B = ((t // 10) % 60) // 10
    C = ((t // 10) % 60) % 10
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startbutton():
    timer.start()

def stopbutton():
    timer.stop()
    global x, y
    if t % 10 == 0:
        x +=1
        y +=1
    else:
        y +=1
    
def resetbutton():
    global t, A, B, C, D, x, y
    timer.stop()
    t = 0
    A = 0
    B = 0
    C = 0
    D = 0
    x, y = 0, 0
    

# define event handler for timer with 0.1 sec interval   
def tick():
    global t
    t += 1

def result():
    global x, y
    return str(x) + "/" + str(y)
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [100,150], 30, "White")
    canvas.draw_text(result(), [200,20], 30, "Aqua")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", canvas_w, canvas_h)

# register event handlers
button1 = frame.add_button("Start", startbutton, 100)
button2 = frame.add_button("Stop", stopbutton, 100)
button3 = frame.add_button("Reset", resetbutton, 100)

frame.set_draw_handler(draw)

timer = simplegui.create_timer(timer_int, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
