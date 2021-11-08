import win32gui,win32con,win32api,win32ui
# import re
import pyautogui

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""
    settingFile =''


    def __init__ (self):
        """Constructor"""
        self.hwnd = None

    def find_window(self,title):
        try:
            self.hwnd = win32gui.FindWindow(None, title)
            assert self.hwnd
            return self.hwnd
        except:
            pyautogui.alert(text='Not found program name ' + title + '\n' 
                            'Please open program before excute script', title='Unable to open program', button='OK')
            # print ('Not found program')
            return None


    def set_onTop(self,hwnd):
        win32gui.SetForegroundWindow(hwnd)
        return win32gui.GetWindowRect(hwnd)



    def Maximize(self,hwnd):
        win32gui.ShowWindow(hwnd,win32con.SW_RESTORE)#, win32con.SW_MAXIMIZE

    def get_mouseXY(self):
        return win32gui.GetCursorPos()

    def set_mouseXY(self):
        import os.path
        import json
        x,y,w,h = win32gui.GetWindowRect(self.hwnd)
        print ('Current Window X : %s  Y: %s' %(x,y))
        fname = 'setting.json'
        if os.path.isfile(fname) :
            dict = eval(open(fname).read())
            x1 = dict['x']
            y1 = dict['y']
            print ('Setting X : %s  Y: %s' %(x1,y1))
        win32api.SetCursorPos((x+x1,y+y1))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x+x1, y+y1, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x+x1, y+y1, 0, 0)
        print ('Current Mouse X %s' % self.get_mouseXY()[0])
        print ('Current Mouse Y %s' % self.get_mouseXY()[1])


    def saveFirstDataPos(self):
        x,y,w,h = win32gui.GetWindowRect(self.hwnd)
        print ('Window X : %s  Y: %s' %(x,y))
        x1,y1 = self.get_mouseXY()
        print ('Mouse X : %s  Y: %s' %(x1,y1))
        data={}
        data['x'] = x1-x
        data['y'] = y1-y
        # f = open("setting.json", "w")
        # self.settingFile
        f = open(settingFile, "w")
        f.write(str(data))

        f.close()

    def wait(self,seconds=1,message=None):
        """pause Windows for ? seconds and print
an optional message """
        win32api.Sleep(seconds*1000)
        if message is not None:
            win32api.keybd_event(message, 0,0,0)
            time.sleep(.05)
            win32api.keybd_event(message,0 ,win32con.KEYEVENTF_KEYUP ,0)

    def typer(self,stringIn=None):
        PyCWnd = win32ui.CreateWindowFromHandle(self.hwnd)
        for s in stringIn :
            if s == "\n":
                self.hwnd.SendMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
                self.hwnd.SendMessage(win32con.WM_KEYUP, win32con.VK_RETURN, 0)
            else:
                print ('Ord %s' % ord(s))
                PyCWnd.SendMessage(win32con.WM_CHAR, ord(s), 0)
        PyCWnd.UpdateWindow()

    def WindowExists(windowname):
        try:
            win32ui.FindWindow(None, windowname)

        except win32ui.error:
            return False
        else:
            return True


# Start Program
x = 0
y = 0 
w = 0
h = 0

hero                = 11
backMenu            = 260,140
heroButton          = 1105,638
closeCharecter      = 755,214
startGame           = 719,420
startNewMap         = 694,593

def click_start_new_game():
    print (f'Start new MAP...')
    time.sleep(1)
    pyautogui.moveTo(startNewMap)


def working():
    print (f'To Menu')
    pyautogui.moveTo(backMenu)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(heroButton)
    pyautogui.click()
    time.sleep(1)
    # Click Working for all hero
    working_x           = 612
    working_y           = 300
    working_y_next      = 70
    # First 5 Hero
    for i in range(5):
        pyautogui.moveTo(working_x,working_y)
        working_y = working_y + working_y_next
        
        pyautogui.click()
        time.sleep(1)
    # --------------------------

    # Next another , No need to move mouse
    # hero
    previous_hero_y = 0
    for i in range(hero-5):
        pyautogui.scroll(-1)
        time.sleep(0.5)
        pyautogui.scroll(-1)
        time.sleep(0.5)
        pyautogui.scroll(-1)
        time.sleep(0.5)
        pyautogui.scroll(-1)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1)
    
    # Move to Last hero
    x,y = pyautogui.position()
    pyautogui.moveTo(x,y+ 20)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)


    pyautogui.moveTo(closeCharecter)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(startGame)
    pyautogui.click()
    time.sleep(1)


import schedule
import time
schedule.every(60).seconds.do(click_start_new_game)
schedule.every(30).seconds.do(working)

# working()

while True:
	schedule.run_pending()
	time.sleep(1)
