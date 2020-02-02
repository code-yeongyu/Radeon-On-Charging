#!/usr/bin/env python3
import subprocess
import pync
from time import sleep
from threading import Thread

# Below OSASCRIPT is from https://apple.stackexchange.com/questions/362502/how-can-i-toggle-automatic-graphics-switching-using-terminal
OSASCRIPT_TOGGLE_GRAPHICS_SWITCHING = """if running of application "System Preferences" then
    try
        quit application "System Preferences"
    on error
        do shell script "killall 'System Preferences'"
    end try
end if
repeat while running of application "System Preferences" is true
    delay 0.1
end repeat
tell application "System Preferences"
    reveal pane id "com.apple.preference.energysaver"
    repeat until exists window "Energy Saver"
        delay 0.1
    end repeat
end tell
tell application "System Events" to tell ¬ 
    group 1 of window "Energy Saver" of application process "System Preferences"
    repeat until exists checkbox "Automatic graphics switching"
        delay 0.1
    end repeat
    click checkbox "Automatic graphics switching"
    set gr to (value of checkbox "Automatic graphics switching") as boolean
end tell
quit application "System Preferences"
if gr then
    return "GPU: INTEGRATED"
else
    return "GPU: RADEON"
end if """

OSASCRIPT_GET_GRAPHICS_SWITCHING = """if running of application "System Preferences" then
    try
        quit application "System Preferences"
    on error
        do shell script "killall 'System Preferences'"
    end try
end if
repeat while running of application "System Preferences" is true
    delay 0.1
end repeat
tell application "System Preferences"
    reveal pane id "com.apple.preference.energysaver"
    repeat until exists window "Energy Saver"
        delay 0.1
    end repeat
end tell
tell application "System Events" to tell ¬ 
    group 1 of window "Energy Saver" of application process "System Preferences"
    repeat until exists checkbox "Automatic graphics switching"
        delay 0.1
    end repeat
    set gr to (value of checkbox "Automatic graphics switching") as boolean
end tell
quit application "System Preferences"
if gr then
    return "GPU: INTEL UHD GRAPHICS 630"
else
    return "GPU: RADEON PRO 560X"
end if """


def system(script):
    return subprocess.Popen(script.split(" "),
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)


def execute_osascript(script):
    return get_result(system('osascript -'),
                      input=script.encode()).replace(script, "")


def get_result(process, **kwargs):
    return process.communicate(input=kwargs.get('input'))[0].decode()


def get_is_charging_from_text(result):
    return not "discharging" in result


def is_graphics_switching_on():
    return "INTEL" in execute_osascript(OSASCRIPT_GET_GRAPHICS_SWITCHING)


def is_battery_charging():
    return get_is_charging_from_text(get_result(system("pmset -g batt")))


def toggle_graphics_switching():
    return execute_osascript(OSASCRIPT_TOGGLE_GRAPHICS_SWITCHING)


def set_graphics_switching():
    if (is_battery_charging() and is_graphics_switching_on()) or (
            not is_battery_charging() and not is_graphics_switching_on()):
        # currently on charging but using intel graphics
        # or currently on not charging but using radeon graphics
        toggle_graphics_switching()


def notify_toggle():
    pync.notify(toggle_graphics_switching())


def main():
    pync.notify("GPU Changer Service Started.")
    set_graphics_switching()
    while True:
        recent_charging_log = is_battery_charging()
        sleep(5)
        if is_battery_charging() != recent_charging_log:
            Thread(target=notify_toggle, args=()).start()


main()
