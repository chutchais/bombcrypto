import pyautogui
pyautogui.FAILSAFE = False

# hero                = 11
# backMenu            = 260,140
# heroButton          = 1105,638
# firstHeroWorking    = 0,0
# lastHeroWorking     = 0,0
# working_y_next      = 70
# closeCharecter      = 755,214
# startGame           = 719,420
# startNewMap         = 694,593

isWorking = False

def click_start_new_game(settings):
    if isWorking : #if set Working , will reject
        pass

    from datetime import datetime
    now = datetime.now()
    print (f'Start new MAP on {now}')
    for account in settings['accounts']:
        startNew_x,startNew_y = account['startNewMap']
        pyautogui.moveTo(startNew_x+10,startNew_y+10)
        time.sleep(1)
        pyautogui.moveTo(account['startNewMap'])
        time.sleep(1)
        pyautogui.click()


def schedule_working(settings):
    global isWorking
    isWorking = True

    minimize    = settings['minimize']

    for account in settings['accounts']:
        working(account,minimize)
        time.sleep(1)

    isWorking = False

# Set working for individual Account
def working(account_dict,minimize=[0,0]):
    from datetime import datetime
    now = datetime.now()
    print (f'Set Working account {account_dict["name"]} on {now}')
    delay_click = 2

    hero                = account_dict['hero_count']
    backMenu            = account_dict['backMenu']
    heroButton          = account_dict['heroButton']
    firstHeroWorking    = account_dict['firstHeroWorking']
    lastHeroWorking     = account_dict['lastHeroWorking']
    working_y_next      = account_dict['working_y_next']
    closeCharecter      = account_dict['closeCharecter']
    startGame           = account_dict['startGame']
    # Added on Nov 11,2021 -- To support Maximize window before start.
    maximize            = account_dict['maximize']
    if maximize != [0,0] : #if setting program will maximize window first
        pyautogui.moveTo(maximize)
        pyautogui.click()
        time.sleep(delay_click)

    
    pyautogui.moveTo(backMenu)
    pyautogui.click()
    time.sleep(delay_click)
    pyautogui.moveTo(heroButton)
    pyautogui.click()
    time.sleep(delay_click)

    working_x,working_y = firstHeroWorking
    
    # First 5 Hero
    for i in range(5):
        pyautogui.moveTo(working_x,working_y)
        working_y = working_y + working_y_next
        
        pyautogui.click()
        time.sleep(delay_click)
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
        time.sleep(delay_click)
    
    # Move to Last hero
    pyautogui.moveTo(lastHeroWorking)
    time.sleep(delay_click)
    pyautogui.click()


    pyautogui.moveTo(closeCharecter)
    pyautogui.click()
    time.sleep(delay_click)
    pyautogui.moveTo(startGame)
    pyautogui.click()
    time.sleep(delay_click)

    if minimize != [0,0] : #if setting program will minimize window
        pyautogui.moveTo(minimize)
        pyautogui.click()

import sys
settings = {
            'loop' : 1, # Minutes
            'minimize' : [0,0], #all account using same Minimize Position
            'accounts':[
                {
                    'name':'Account1',
                    'hero_count'        : 15,
                    'backMenu'          : [258,128],
                    'heroButton'        : [1111,630],
                    'firstHeroWorking'  : [612,291],
                    'lastHeroWorking'   : [612,601],
                    'working_y_next'    : 72,
                    'closeCharecter'    : [753,211],
                    'startGame'         : [704,404],
                    'startNewMap'       : [694,593],
                    'maximize'          : [0,0]
                },
                ]
        }


import schedule
import time

# Initial run on first time , after 30 secs.
time_delay = 30
print(f'Program started , waiting for {time_delay} Secs....')
time.sleep(time_delay)
schedule_working (settings)

sys.exit()

# Click for detect window saver mode
schedule.every(30).seconds.do(click_start_new_game,settings)
# Main Job interval time (minutes)
schedule.every(settings['loop']*60).seconds.do(schedule_working ,settings)

while True:
	schedule.run_pending()
	time.sleep(1)
