from pynput import mouse
import pyautogui
import time

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")
        click_positions.append((x, y))
        if len(click_positions) >= 10:  # Stop after 10 clicks
            return False

def move_mouse():
    click_positions = []

    # Collect events until 10 clicks are recorded
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    print("Recorded click positions:", click_positions)

    # Replay the click pattern
    for pos in click_positions:
        print(pos[0], pos[1])
        pyautogui.click(pos[0], pos[1])
        time.sleep(3)

    print("Click pattern executed.")

