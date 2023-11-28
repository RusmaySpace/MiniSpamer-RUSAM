import pyautogui, time, subprocess, os
bat_path = "010101.bat"
os.system(f"start cmd /c {bat_path}")
os.system(f"start cmd /c {bat_path}")
os.system(f"start cmd /c {bat_path}")
time.sleep(10)
f = open("aaa.txt", "r", encoding="utf-8")
for line in f:
    pyautogui.typewrite(line)
    pyautogui.press("enter")