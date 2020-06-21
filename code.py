import pyautogui
from PIL import Image, ImageGrab
import time

def action(key):
    pyautogui.keyDown(key)
    return

def isColliding(data):
        # checking for cactus
    for i in range(220,260):
        for j in range(410, 470):
            if data[i, j] > 100:
                action('up')
                return

    # checking for brid
    for i in range(180,225):
        for j in range(350, 400):
            if data[i, j] > 100:
                action('down')
                return


    return 

if __name__ == "__main__":
    time.sleep(5)
    action('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isColliding(data)
        
        #cactus
        # for i in range(220,260):
        #      for j in range(410, 470):
        #         data[i, j] = 0
        
        # image.show()
        # break