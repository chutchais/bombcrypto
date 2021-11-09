import pyautogui
import re, traceback
import time


def main():
    try:
        while True:
            x1,y1 = pyautogui.position()
            print (f'X:{x1}/Y:{y1}')
            time.sleep(0.5)


        



        



    except:
        f = open("log.txt", "w")
        f.write(traceback.format_exc())
        print(traceback.format_exc())






main()

#2558