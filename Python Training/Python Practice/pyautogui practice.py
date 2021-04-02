import pyautogui

print(pyautogui.position())

pyautogui.click(x=537, y=69)

pyautogui.typewrite("hello world!")
pyautogui.typewrite(["enter"])

pyautogui.hotkey("ctrl", "c")
