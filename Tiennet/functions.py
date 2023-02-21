import pydirectinput
import pyautogui
import subprocess
from time import  sleep
from python_imagesearch.imagesearch import imagesearch



# setting up the tractor
def settingUpTractor():

    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 2):
        print(".", end="", flush=True)
        sleep(1)

    # giving intertia to all the direction cause the game is shit
    pydirectinput.keyDown('a')
    sleep(1)
    pydirectinput.keyUp('a')

    pydirectinput.keyDown('s')
    sleep(1)
    pydirectinput.keyUp('s')

    pydirectinput.keyDown('d')
    sleep(1)
    pydirectinput.keyUp('d')

    pydirectinput.keyDown('1')
    sleep(1)
    pydirectinput.keyUp('1')

    pydirectinput.keyDown('w')
    sleep(1)
    pydirectinput.keyUp('w')

    sleep(3)

    print("Go")



# Turning sequence of action for the tractor
def turn(key,dir,seconds=1.00):

    pydirectinput.keyDown(dir)

    pydirectinput.keyDown(key)

    sleep(seconds)

    pydirectinput.keyUp(dir)

    pydirectinput.keyUp(key)

    sleep(2)



# moving forward sequence of action for the tractor
def move(key,segment_length) :

    pydirectinput.keyDown(key)

    sleep(segment_length)

    pydirectinput.keyUp(key)

    pydirectinput.keyDown('s')

    sleep(0.50)

    pydirectinput.keyUp('s')



# startup function, including mounting farm simulator, navigate through the menu
# then create a server, connect and wait
def startup(montage=1) :
    
    #mount disk if it's the first iteration since main script run
    if montage == 1 :

        #switch to daemon tools
        pyautogui.hotkey('alt','tab')
        sleep(2)
        pyautogui.rightClick(650,580)
        sleep(1)
        pyautogui.leftClick(655,585)
        sleep(8)
        pyautogui.press('right')
        sleep(2)
        pyautogui.press('enter')
        sleep(8)

    #open disk
    pyautogui.rightClick(650,580)
    sleep(1)
    pyautogui.leftClick(655,585)
    sleep(4)
    pyautogui.press('enter')
    sleep(5)

    #start game in popup app
    pyautogui.leftClick(443,461)
    sleep(35)

    #go in multiplayer
    pydirectinput.press('down')
    sleep(0.6)
    pydirectinput.press('down')
    sleep(0.6)
    pydirectinput.press('enter')
    sleep(1)

    #create game
    pydirectinput.press('down')
    sleep(0.25)
    pydirectinput.press('enter')
    sleep(0.25)
    pydirectinput.press('enter')
    sleep(0.25)

    #add mode
    pydirectinput.press('right')
    sleep(0.6)
    pydirectinput.press('down')
    sleep(0.6)
    pydirectinput.press('down')
    sleep(0.6)
    pydirectinput.press('down')
    sleep(0.6)
    pydirectinput.press('down')
    sleep(0.6)
    pydirectinput.press('enter')
    sleep(3)

    # select the mods with a function dedicated to it
    # also save mods with a similar function
    select_mods()
    sleep(1)
    save()

    #finish server configuration and launch
    pydirectinput.press('up')
    sleep(0.6)
    pydirectinput.press('enter')
    sleep(40)
    
    #Press enter
    pyautogui.leftClick(500,500)
    pydirectinput.press('down')
    sleep(0.25)
    pydirectinput.press('enter')
    sleep(6)



# startup player sequence of action in game
def in_game_startup() :

    #go to tractor
    pydirectinput.press('tab')
    sleep(3)

    #start tractor and setup
    pydirectinput.press('q')
    sleep(2)
    pydirectinput.press('v')
    sleep(2)
    pydirectinput.press('f')
    sleep(2)

    # dezoom the view
    for scrolling in range(1,20) :
        pyautogui.scroll(-50)
    sleep(4)



# select mods with image search loop.
#typical loop for searching for a particulare image
def select_mods() :

    select_all_button_found = False

    while select_all_button_found == False :

        pos = imagesearch("./select_all_mods.PNG")

        if pos [0] != -1 :

            print("select_all_mods image found")
            sleep(1)
            pyautogui.leftClick(pos[0]+10,pos[1]+10)
            sleep(2)
        
            select_all_button_found = True

        else : 

            print("select_all_mods image not found, retrying...")
            sleep(2)



# save all mods with the same technique as 
# select mods function, more info in function file of Huriel
def save() :

    save_button_found = False

    while save_button_found == False :

        pos = imagesearch("./save.PNG")

        if pos [0] != -1 :

            print("save_button image found")
            sleep(1)
            pyautogui.leftClick(pos[0]+10,pos[1]+10)
            sleep(3)

            save_button_found = True 

        else : 

            print("save_button image not found, retrying...")
            sleep(2)
            


# shutdown func to kill Farming Simulator process,
# quickest way to do so
def shutdown() :

    subprocess.call("taskkill /f /im game.exe", shell=True)



# image search loop to wait for Huriel connection request
# and accept it then 
def wait_for_Huriel() :

    accept_button_found = False

    while accept_button_found == False :

        pos = imagesearch("./accept_button.PNG")

        if pos [0] != -1 :

            print("accept_button image found")
            sleep(1)
            pyautogui.leftClick(pos[0]+10,pos[1]+10)
            sleep(50)

            accept_button_found = True
        
        else : 

            print("accept_button image not found, retrying...")
            sleep(2)



# L-system axiom and rules declarations
axiom = "F-F-F-F-F"
rules = {
    "F" : "F-F-F++F+F-F"  
}


# number of iterations declaration,
# usually 2.
iterations = 1



#L-system string generator
def generate_lsystem(axiom,rules,iterations) :

    lsystem_string = axiom

    for i in range(iterations) :

        new_string = ""

        for c in lsystem_string :

            if c in rules:

                new_string = new_string + rules[c]

            else :

                new_string = new_string + c

        lsystem_string = new_string

    return lsystem_string

lsystem_string = generate_lsystem(axiom,rules,iterations)


# variable and contants declaration for draxing l system,
# it assume that 72 degrees angle of rotation for our
#l system is equal to a 3.620 seconds keyDown of turning and forward keys
angle_converted = 3.620
segment_length = 3.35



# drawing function with loop that seek in the string of the generated 
# l system and give response in the game with pydirectinput depending
# on the string.
def draw_lsystem(lsystem_string):
    
    for c in lsystem_string :

        print(c)

        #Forward
        if c == "F" : 

            move('1',segment_length)

        #turn right
        elif c == "+" :

            turn('d','w', abs(angle_converted))
                        
        #turn left
        elif c == "-" :
            
            turn('a','w', abs(angle_converted))


