import pyautogui
import pydirectinput
import random
from time import sleep
from phrases import phrases
from python_imagesearch.imagesearch import imagesearch

# function to hide vscode window
def hide_vscode() :

    sleep(5)
    pyautogui.click(1165,15)
    sleep(1)
    
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

#function to drag the tab to avoit button regognition bug
def ongletdrag() :
    sleep(1)
    onglet_found = False

    while onglet_found == False :
        
            pos = imagesearch("./onglet.PNG")

            if pos[0] != -1:

                print("onglet image found")
                sleep(1)
                pyautogui.moveTo(pos[0]+160,pos[1]+10)
                pyautogui.mouseDown(button='left')
                pyautogui.moveTo(200,50)
                sleep(5)
                onglet_found = True

            else:

                print("onglet image not found, retrying...")
                
                sleep(2)

# Go to multi chain of automation
def goToMultiplayer() :

    # sleep(3)
    # pyautogui.hotkey('alt','tab')
    sleep(4)
    pydirectinput.press('down')
    sleep(0.6)
    pydirectinput.press('down')
    sleep(0.6)
    pydirectinput.press('enter')
    sleep(1)



# function for initiating connection to server and press start regarding time of connection
def startup() :

    pydirectinput.press('enter')
    sleep(6)
    
    pydirectinput.press('up')
    sleep(2)
    pydirectinput.press('down')
    sleep(2)
    pydirectinput.press('enter')
    sleep(2)
    pydirectinput.press('up')
    sleep(2)
    pydirectinput.press('down')
    sleep(2)

    # typical loop for searching serveur up image
    serveur_up_found = False

    while serveur_up_found == False :
        
            pos = imagesearch("./serveur_up.PNG")

            if pos[0] != -1:

                print("serveur_up image found")
                sleep(1)
                pyautogui.doubleClick(pos[0]+10,pos[1]+10)
                sleep(5)
                serveur_up_found = True

            else:

                print("serveur_up image not found, retrying...")
                pydirectinput.press('enter')
                sleep(2)

    sleep(40)

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

    sleep(4)
    pydirectinput.press('tab')
    sleep(1)
    pydirectinput.press('tab') 
    # miniFinder()

    sleep(1)
    pydirectinput.press('e')
    sleep(1)
    pydirectinput.keyDown('w')
    sleep(3.5)
    pydirectinput.keyUp('w')


