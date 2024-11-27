# Copied Text:  [12:14 pm, 31/10/2024] Sujal: Fees bhari deje
# [12:14 pm, 31/10/2024] Sujal: Last date 8th chhe
# [12:20 pm, 31/10/2024] Shail: Minor ni bharvani che?
# [12:22 pm, 31/10/2024] Sujal: Minor ni j to bharavni chhe
# [12:22 pm, 31/10/2024] Shail: Drop nai levo?
# [12:22 pm, 31/10/2024] Sujal: Peli to bhari didhi ti ne
# [12:22 pm, 31/10/2024] Sujal: Me to bhari didhi
# [12:22 pm, 31/10/2024] Sujal: Pachhi tari ichha

import pyautogui
import pyperclip
import time
# from openAi import OpenAI

# client = OpenAI(
#         # api_key = "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
#         api_key = "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",
#     )

# Wait for a moment before performing the action (this is useful if you need to focus on the target window)
time.sleep(2)

# Step 1: Click on the icon at position (1020, 1050)
pyautogui.click(1020, 1050)

# Step 2: Drag from (724, 189) to (724, 980) to select text
pyautogui.mouseDown(724, 189)  # Press the mouse button to start the drag
pyautogui.moveTo(724, 980, duration=1)  # Drag to the target position
pyautogui.mouseUp()  # Release the mouse button to finish the drag

# Step 3: Copy the selected text using Ctrl+C
pyautogui.hotkey('ctrl', 'c')

# Step 4: Click at a position to deselect the text
pyautogui.click(724, 189)

# Step 5: Wait for a moment to allow the clipboard to update
time.sleep(1)

# Step 6: Retrieve the copied text from the clipboard and store it in a variable
copied_text = pyperclip.paste()

# Print the copied text
print("Copied Text: ", copied_text)
    
# # OpenAI System Characteristics
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a person named Shail who speaks Hindi, English as well as Gujarati all written in english text. You are from India, Gujarat. You analyze chat history and respond like Shail. Output should be the next chat response as Shail"},
#         {"role": "user", "content": copied_text}
#     ]
# )

# response =  completion.choices[0].message
# pyperclip.copy(response)

# # Click on position (1200, 970)
# pyautogui.click(1200, 970)

# # Press Enter to confirm action or submit (depending on your use case)
# pyautogui.press('enter')