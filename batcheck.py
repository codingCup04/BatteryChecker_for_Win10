from win10toast import ToastNotifier
import psutil, time
a = "%"
ch = True
toaster = ToastNotifier()
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent
print(f"{percent}%, Plugged: {plugged}")
while True:
    toaster = ToastNotifier()
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    if percent <= 25 and plugged == False and ch == True:
        toaster.show_toast(
                    "Low battery notifications...",
                    f"Warning: you have {percent}{a} left.",
                    duration=5
                   )
        ch = False
    elif ch == False:
        time.sleep(300)
"""
toaster.show_toast(
                    "Low battery notifications...",
                    f"Warning: you have lower than 20{a} left.",
                    duration=10
                   )
"""
"""

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
print(f"{percent}%, Plugged: {plugged}")
"""