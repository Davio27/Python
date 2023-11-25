import pyautogui
import time
def chrome():
    pyautogui.press('win')
    pyautogui.write("Chrome")
    pyautogui.press('enter')
    
def site():
    time.sleep(2)
    pyautogui.hotkey('win', 'up')
    time.sleep(1)
    pyautogui.write("https://portal.siaaluno.com.br/sianet/logon")
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    
chrome()
site()
        