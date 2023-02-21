import pyautogui
import pydirectinput
import random
from time import sleep
from phrases import phrases
from python_imagesearch.imagesearch import imagesearch



# core function for writing in Farm Sim chat
def writeInChat(string) :

    pydirectinput.press('t')

    # filter to avoid accent in the phrases (can't be written by pyautogui)
    for c in string :

        if c == 'é' :
            pyautogui.press('e')
        elif c == 'è' :
            pyautogui.press('e')
        elif c == 'ë' :
            pyautogui.press('e')
        elif c == 'ê' :
            pyautogui.press('e')
        elif c == 'à' :
            pyautogui.press('a')
        elif c == 'â' :
            pyautogui.press('a')        
        elif c == 'ô' :
            pyautogui.press('o')
        elif c == 'î' : 
            pyautogui.press('i')
        elif c == 'ç' :
            pyautogui.press('c')
        elif c == 'ï' :
            pyautogui.press('i')
        else :
            pyautogui.press(c)

    pydirectinput.press('enter')
    


# function that loop through all the phrases of the phrases list 
def tirade() :
    
    #loop to write again and again phrases, also looking for any server shutdown by Tiennet (if so break the loop)
    quit_image_found = False

    while quit_image_found ==  False :

        #typical block of code for images searching, in this case write in chat if not found
        for interjection in range(0,len(phrases)) :
        
            pos = imagesearch("./quit_image.PNG")

            if pos[0] != -1:

                print("quit image found")
                sleep(1)
                pyautogui.leftClick(pos[0]+10,pos[1]+10)
                
                quit_image_found = True

                break

            else:

                print("quit image not found, keep going")

            random_pause = random.randint(1,3)

            sleep(random_pause)

            writeInChat(phrases[interjection])

        wait_bt_tirades = random.randint(20,50)
            
        sleep(wait_bt_tirades)



# Go to multi chain of automation
def goToMultiplayer() :

    sleep(2)
    pyautogui.hotkey('alt','tab')
    sleep(1)
    pydirectinput.press('down')
    sleep(0.6)
    pydirectinput.press('down')
    sleep(0.6)
    pydirectinput.press('enter')
    sleep(0.6)



# function for initiating connection to server and press start regarding time of connection
def startup() :

    pydirectinput.press('enter')
    sleep(3.5)
    pydirectinput.press('up')
    sleep(1)
    pydirectinput.press('down')
    sleep(1)

    # typical loop for searching an image. In this case the serveur up image
    serveur_up_found = False

    while serveur_up_found == False :
        
            pos = imagesearch("./serveur_up.PNG")

            if pos[0] != -1:

                print("serveur_up image found")
                sleep(1)
                pyautogui.doubleClick(pos[0]+10,pos[1]+10)
                
                serveur_up_found = True

            else:

                print("serveur_up image not found, retrying...")
                pydirectinput.press('enter')
                sleep(2)
           
    # loop to press start 
    demarrer_found = False

    while demarrer_found == False :
        
            pos = imagesearch("./demarrer.PNG")

            if pos[0] != -1:

                print("demarrer image found")
                sleep(1)
                pyautogui.leftClick(pos[0]+10,pos[1]+10)
                sleep(3)

                demarrer_found = True

            else:

                print("demarrer image not found, retrying...")
                sleep(2)


  
#take place on the hill in the game
def takePlace() :

    sleep(1)
    pydirectinput.press('tab')

    miniFinder()

    sleep(1)
    pydirectinput.press('e')
    sleep(1)
    pydirectinput.keyDown('w')
    sleep(3.5)
    pydirectinput.keyUp('w')



# image search function to find the good vehicule for Huriel, the minicooper
def miniFinder() :

    gallons_found = False

    while gallons_found == False :
        
            pos = imagesearch("./gallons.PNG")

            if pos[0] != -1:

                print("gallons image found")
                sleep(1)

                gallons_found = True

            else:

                print("gallons image not found, retrying...")
                sleep(1)
                pydirectinput.press('tab')
                sleep(2)
