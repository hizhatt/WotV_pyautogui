import pyautogui
import time
import cv2
import winsound
import sys
import datetime


l, top, w, h = 860, 0, 1060, 630  # left,top,width,height

def butClick(name):
    t = 0  # timer starts at 0
    b = False  # b stands for button
    global l, top, w, h
    while not b:  # will enter this loop
        if t % 2 == 0:  # so that it will only print every 2 seconds. Every sec is too frequent
            print('Looking for:', name, t, 's')  # notification
        b = pyautogui.locateOnScreen(name, region=(l, top, w, h), confidence=0.9)  # if found, button is now true
        t += 1  # increase timer
        time.sleep(1)
        if t % 5 == 0:
            if t % 30 == 0:  # nudge the mouse every 30 seconds
                pyautogui.move(1, 1)
                pyautogui.move(-1, -1)
                print('Nudging the mouse a little...')
            # check if the party has disbanded
            if pyautogui.locateOnScreen('Disband.png', region=(l, top, w, h), confidence=0.8):
                print('Room has DISBANDED!')
                winsound.PlaySound('Trumpet', winsound.SND_FILENAME)
                butClick('MidOK.png')
                time.sleep(3)
                sys.exit()
            # idle too long, leave the party/room
            if pyautogui.locateOnScreen('RoomWaitTag.png', region=(l, top, w, h), confidence=0.9) and t == 100:
                print('10+ mins has passed and still idle!')
                butClick('CancelPrep.png')
                butClick('LeaveRoom.png')
                winsound.PlaySound('Trumpet', winsound.SND_FILENAME)
                sys.exit()
            # sometimes there's some error and dismissed the disband window, so this will check that
            if pyautogui.locateOnScreen('MultiQuestList.png', region=(l, top, w, h), confidence=0.8):
                print('I think the party has disbanded and the bot has click past it...')
                winsound.PlaySound('Trumpet', winsound.SND_FILENAME)
                sys.exit()
            # check for lost connection
            if pyautogui.locateOnScreen('ConnectionLost.png', region=(l, top, w, h), confidence=0.7):
                print('Connection lost...')
                winsound.PlaySound('Trumpet', winsound.SND_FILENAME)
                sys.exit()

    x, y = pyautogui.locateCenterOnScreen(name, region=(l, top, w, h), confidence=0.9)  # set coord of button
    while b:  # while the next button is there, keep clicking
        print('Clicking:', name, 'at', x, ',', y)
        p = pyautogui.position()
        pyautogui.click(x, y)
        pyautogui.click(x, y)
        pyautogui.moveTo(p)
        time.sleep(0.5)
        b = pyautogui.locateOnScreen(name, region=(l, top, w, h), confidence=0.9)  # if button still on screen


# run
cycle = 0
while True:
    butClick('Ready.png')
    butClick('Next.png')

    cycle += 1
    print('----------- THIS IS CYCLE NUMBER:', cycle, '--------------')
    f = open("BattleLog.txt", "a")
    myTime = datetime.datetime.now()
    f.write(myTime.strftime('%w %b %X'))
    f.write(' Cycle:')
    f.write(str(cycle))
    f.write('\n')
    f.close()

    butClick('Cancel.png')
    butClick('Return.png')
