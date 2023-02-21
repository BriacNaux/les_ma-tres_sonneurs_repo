from time import sleep
from functions import settingUpTractor, startup, shutdown, in_game_startup, draw_lsystem, generate_lsystem, wait_for_Huriel
from functions import axiom, rules, iterations, lsystem_string



# Main function
def main():

    for loops in range(0,20) :

        #start without mounting if it's the first iteration
        if loops == 0 :
            startup(1)  
        else :
            startup(0)

        wait_for_Huriel()

        in_game_startup()

        settingUpTractor()

        print(lsystem_string)  

        generate_lsystem(axiom,rules,iterations)

        draw_lsystem(lsystem_string)

        #draw two l system in the field to have a 1h and 10 min loop
        print("second L-system engaged")

        draw_lsystem(lsystem_string)

        # print warning message of rebooting  
        for warnings in range(0,5) :
            print('Rebooting loop')
            sleep(1)

        # shutdown
        shutdown()



    



if __name__ == "__main__":
    main()





