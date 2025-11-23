import datetime
import time
import tkinter as tk
from tkinter import messagebox
import winsound
import threading


def start_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    
    def alarm_thread():
        while True:
            current_time = time.strftime("%H:%M:%S")
            if current_time == alarm_time:
                messagebox.showinfo("Alarm", "⏰ Wake Up! Alarm is ringing!")
                # Alarm Sound (beeps for 5 seconds)
                for _ in  range(5):
                    winsound.Beep(2000, 500)
                break
            time.sleep(1)

    t = threading.Thread(target=alarm_thread)
    t.start()


# GUI window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("350x250")
root.config(bg="white")

tk.Label(root, text="⏰ Alarm Clock", font=("Arial", 20, "bold"), bg="white").pack(pady=10)

# Time Input Frame
frame = tk.Frame(root, bg="white")
frame.pack(pady=20)

hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

tk.Label(frame, text="Hour", bg="white").grid(row=0, column=0)
tk.Label(frame, text="Minute", bg="white").grid(row=0, column=1)
tk.Label(frame, text="Second", bg="white").grid(row=0, column=2)

hour_entry = tk.Entry(frame, textvariable=hour, width=5)
minute_entry = tk.Entry(frame, textvariable=minute, width=5)
second_entry = tk.Entry(frame, textvariable=second, width=5)

hour_entry.grid(row=1, column=0)
minute_entry.grid(row=1, column=1)
second_entry.grid(row=1, column=2)

# Start Button
set_btn = tk.Button(root, text="Set Alarm", command=start_alarm,
                    bg="green", fg="white", font=("Arial", 16, "bold"))
set_btn.pack(pady=20)

root.mainloop()