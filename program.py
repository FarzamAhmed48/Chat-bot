import pyautogui
import pyperclip
import time

pyautogui.click(1363,1042)
time.sleep(1)

pyautogui.moveTo(658,168)
pyautogui.dragTo(1917,1004, duration=1.0 ,button='left')
pyautogui.hotkey('ctrl','c')
time.sleep(1)
text=pyperclip.paste()
print(text)
