from time import sleep
import pyautogui
import pydirectinput
from functions import tirade, takePlace, goToMultiplayer


def main() :
    
    goToMultiplayer()

    #main loop from start to end
    for loops in range(0,20) :

        takePlace()

        tirade()


        sleep(7)
        pyautogui.press('tab')
        sleep(3)
        pydirectinput.press('up')
        sleep(1)
        pydirectinput.press('up')
        sleep(1)
        pydirectinput.press('up')
        sleep(1)
        


if __name__ == "__main__" :
    main()


