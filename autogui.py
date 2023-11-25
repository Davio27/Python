# Use .hotkey para criar atalhos de teclas duplas ex: pyautogui.hotkey('ctrl', 'l')
# Use .press para criar atalhos de teclas simples (uma tecla) ex: pyautogui.press('enter')
# # Use .write para escrever em caixas de textos
# # Use o .click para direcionar com o mouse e clicar (obs: use o mouseinfo para saber as coordenadas)
import pyautogui
import time
def abrir_spotify():
    pyautogui.press('win')
    pyautogui.click(1197,549,duration=1)
    time.sleep(2)
    pyautogui.hotkey('win', 'up')
    
    
def reproduzir():
    time.sleep(2)
    pyautogui.click(153,119,duration=4)
    pyautogui.click(471,32,duration=1)
    pyautogui.write("Megabaile Do Areias")
    pyautogui.click(680,422,duration=1.5)
    pyautogui.click(680,422,duration=10)
    
def chrome():
    pyautogui.press('win')
    pyautogui.write("Chrome")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write("Udemy")
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write("https://portal.siaaluno.com.br/sianet/logon")
    pyautogui.press('enter')

# abrir_spotify()
# reproduzir()
chrome()