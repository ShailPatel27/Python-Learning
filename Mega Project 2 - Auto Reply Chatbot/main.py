import pyautogui
import pyperclip
import time
import keyboard
from openai import OpenAI
import threading

stop_flag = False

def listen_for_escape():
    global stop_flag
    # This function will set stop_flag to True when the Escape key is pressed
    while True:
        if keyboard.is_pressed("esc"):
            stop_flag = True
            print("Escape key pressed. Exiting the loop.")
            break

# Start a separate thread to listen for the Escape key
listener_thread = threading.Thread(target=listen_for_escape)
listener_thread.start()

client = OpenAI(
        api_key = "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"
        # api_key = "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"
    )

# Wait for a moment before performing the action (this is useful if you need to focus on the target window)
time.sleep(2)
# Step 1: Click on the icon at position (1020, 1050)
pyautogui.click(1020, 1050)

def is_last_message_not_from_shail(copied_text):
    # Split the copied text into individual messages based on newlines
    messages = copied_text.strip().split("\n")
    
    # Get the last message
    last_message = messages[-1]
    
    # Extract the sender's name by splitting on "]" and ":"
    # The format assumed: "[time] Sender: message"
    try:
        sender = last_message.split("] ")[1].split(":")[0].strip()
        if(sender != "Shail"):
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
    

while True:
    
    if stop_flag:
        break

    # Step 2: Drag from (749, 190) to (749, 980) to select text
    pyautogui.mouseDown(749, 190)  # Press the mouse button to start the drag
    pyautogui.moveTo(749, 980, duration=1)  # Drag to the target position
    pyautogui.mouseUp()  # Release the mouse button to finish the drag

    # Step 3: Copy the selected text using Ctrl+C
    pyautogui.hotkey('ctrl', 'c')

    # Step 4: Click at a position to deselect the text
    pyautogui.click(749, 190)

    # Step 5: Wait for a moment to allow the clipboard to update
    time.sleep(1)

    # Step 6: Retrieve the copied text from the clipboard and store it in a variable
    copied_text = pyperclip.paste()

    # Print the copied text
    print("Copied Text: ", copied_text)
    
    result = is_last_message_not_from_shail(copied_text)
    if(result == True):
        # OpenAI System Characteristics
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Shail, a 20-year-old Computer Engineering student from Gujarat, India. You speak Gujarati, English and Hindi all in English and respond casually, succinctly (1-5 words). You analyze the chat history (especially the last message) and repond accordingly."},
            ]
        )

        response =  completion.choices[0].message.content
        pyperclip.copy(response)

        # Click on position (1200, 970)
        pyautogui.click(1200, 970)
        
        pyautogui.hotkey('ctrl', 'v')

        # Press Enter to confirm action or submit (depending on your use case)
        pyautogui.press('enter')
        
        print(response)
        # time.sleep(10)
        