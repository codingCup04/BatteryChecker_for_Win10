from win10toast import ToastNotifier
import psutil, time
a = "%"
bat = int(input("Battery %: "))
delay = int(input("Delay (s): "))
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
    if percent <= bat and plugged == False and ch == True:
        toaster.show_toast(
                    "Low battery notifications...",
                    f"Warning: you have {percent}{a} left.",
                    duration=delay
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