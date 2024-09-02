import pyautogui
import time


delay = 0.1  

clicks = 100 

# Wait 5 seconds
print("Starting in 5 seconds...")
time.sleep(5)

for i in range(clicks):
    pyautogui.click()
    time.sleep(delay)

print("completed!")
