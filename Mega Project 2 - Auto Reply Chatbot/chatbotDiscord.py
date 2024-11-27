import pyautogui
import pyperclip
import time
from openai import OpenAI
import keyboard
import threading

client = OpenAI(
    api_key="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"
)

stop_flag = False

def listen_for_escape():
    global stop_flag
    while True:
        if keyboard.is_pressed("esc"):
            stop_flag = True
            print("Escape key pressed. Exiting the loop.")
            break

# Start a separate thread to listen for the Escape key
listener_thread = threading.Thread(target=listen_for_escape)
listener_thread.start()

# Wait for a moment before performing the action
time.sleep(5)

# Step 1: Click on the icon at position (1020, 1050)
pyautogui.click(1020, 1050)

def is_last_message_not_from_darkslayer(copied_text):
    """
    Checks if the last message in the copied text is not from 'Dark Slayer'.
    """
    # Split the copied text into individual lines
    messages = copied_text.strip().split("\n")
    
    # Iterate from the last message upwards to find the latest full message
    for line in reversed(messages):
        # Check if the line includes a sender and is not empty
        if "—" in line:
            sender = line.split("—")[0].strip()
            # Return True if the sender is not "Dark Slayer"
            return sender != "Dark Slayer"
    
    return False  # If no valid message is found, return False to avoid replying

while True:
    if stop_flag:
        break
    
    # Step 2: Drag from (900, 189) to (900, 980) to select text
    pyautogui.mouseDown(900, 189)
    pyautogui.moveTo(900, 980, duration=1)
    pyautogui.mouseUp()

    # Step 3: Copy the selected text using Ctrl+C
    pyautogui.hotkey('ctrl', 'c')

    # Step 4: Click at a position to deselect the text
    pyautogui.click(900, 189)

    # Step 5: Wait for the clipboard to update
    time.sleep(1)

    # Step 6: Retrieve the copied text from the clipboard
    copied_text = pyperclip.paste()
    print("Copied Text:", copied_text)
    
    # Check if the last message is from someone other than "Dark Slayer"
    if is_last_message_not_from_darkslayer(copied_text):
        # Generate a response with OpenAI API
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Dark Slayer who speaks Hindi. You are from India and respond casually, succinctly (1-5 words). You analyze the chat history (especially the last message) and repond accordingly. You both play a game called Valorant."},
                {"role": "user", "content": copied_text}
            ]
        )

        # Access only the content of the response message
        response = completion.choices[0].message.content
        print(response)
        response = response.replace(".", "").replace("!", "").replace(",", "")
        response = response.capitalize()
        pyperclip.copy(response)

        # Step 7: Click on the Discord input field to paste the response
        pyautogui.click(1200, 970)
        
        # Use ctrl+v to paste the response and press Enter to send
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        
        # Print the response content
        print("Response:", response)
        time.sleep(10)