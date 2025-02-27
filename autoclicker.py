import threading
import time

import pyautogui
from pynput import keyboard

clicking = False  # Flag to control clicking


def clicker():
    global clicking
    while True:
        if clicking:
            pyautogui.click()
        time.sleep(0.001)  # Adjust speed of clicks


def on_press(key):
    global clicking
    try:
        if key.char == '[':  # Toggle clicking when '[' is pressed
            clicking = not clicking
            print("Autoclicker toggled", "ON" if clicking else "OFF")
    except AttributeError:
        pass


def main():
    click_thread = threading.Thread(target=clicker, daemon=True)
    click_thread.start()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
