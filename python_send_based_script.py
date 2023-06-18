import pywhatkit as w
import time
import pyautogui

message_sent = False
while not message_sent:
    try:
        phone_num = str(input("Input Phone Number (ex:60123456789): "))
        message = str(input("Input Message: "))
        hour = int(input("Hour (Time to be sent): "))
        minute = int(input("Minute (Time to be sent): "))

        w.sendwhatmsg(phone_num, message, hour, minute) 

        pyautogui.press('enter')
        time.sleep(2)
        message_sent = True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        time.sleep(10)  # Add a delay of 10 seconds before retrying

print("Message sent successfully!") 