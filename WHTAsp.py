import  pyautogui
import  time
import emoji
time.sleep(4)
count=0
while count<500:
    pyautogui.typewrite("Web"+str(count))
    pyautogui.press("Enter")
    count=count+1
