# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
count = 0
# helper function to start and restart the game
range = 100
thres = 7
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global count
    global thres
    global range
    count = 0
    secret_number = random.randrange(0, range)
    print "New game. Range is", '[0,', str(range)+')'
    print "Number of remaining guesses is ", thres- count
    print ''
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    global thres
    range = 100
    thres = 7
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global range
    global thres
    range = 1000
    thres = 10
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    guess = int(guess)
    
    print "Guess was ", guess
    
    global count
    count +=1
    if thres - count == 0:
        print "You ran out of guesses.", "The number was", secret_number
        print ''
        new_game()
    elif guess > secret_number:
        
        print "Number of remaining guesses is ", thres- count
        print "Lower!"
        print ''
    elif guess < secret_number:
        
        print "Number of remaining guesses is ", thres- count
        print "Higher!"
        print ''
    elif guess == secret_number:
        
        print "Number of remaining guesses is ", thres- count
        print "Correct!"
        
        new_game()
     


    
# create frame
frame = simplegui.create_frame('Guess the number', 300, 300)

button1 = frame.add_button('Range is [0,100)', range100, 150)
button2 = frame.add_button('Range is [0,1000)', range1000, 150)
inp = frame.add_input('input guess', input_guess, 200)
# register event handlers for control elements and start frame

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric