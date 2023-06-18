import tkinter as tk
import pywhatkit as w
import pyautogui
import time

def send_message():
    phone_num = phone_entry.get()
    message = message_entry.get()
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())

    w.sendwhatmsg(phone_num, message, hour, minute)

    pyautogui.press('enter')
    time.sleep(2)
    
    status_label.config(text="Message sent successfully!")

# Create the main window
window = tk.Tk()
window.title("WhatsApp Message Sender")

# Create the input fields
phone_label = tk.Label(window, text="Recipient Phone Number (ex:+60123456789):")
phone_entry = tk.Entry(window)
message_label = tk.Label(window, text="Message:")
message_entry = tk.Entry(window)
hour_label = tk.Label(window, text="Time to be sent (24-hour format) -- Hour:")
hour_entry = tk.Spinbox(window, from_=0, to=23, width=5)
minute_label = tk.Label(window, text="Time to be sent (24-hour format) -- Minute:")
minute_entry = tk.Spinbox(window, from_=0, to=59, width=5)

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message)

# Create the status label
status_label = tk.Label(window, text="")

# Layout the widgets using grid
phone_label.grid(row=0, column=0, sticky="e", padx=10, pady=5)
phone_entry.grid(row=0, column=1, padx=10, pady=5)
message_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
message_entry.grid(row=1, column=1, padx=10, pady=5)


hour_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
hour_entry.grid(row=2, column=1, padx=10, pady=5)
minute_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
minute_entry.grid(row=3, column=1, padx=10, pady=5)
send_button.grid(row=4, columnspan=2, padx=10, pady=10)
status_label.grid(row=5, columnspan=2, padx=10, pady=5)

# Start the main loop
window.mainloop()