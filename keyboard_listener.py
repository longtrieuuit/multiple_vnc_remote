from pynput import mouse
from pynput import keyboard
import time
import json
import sys



name_of_recording = "TEST"
record_all = True
storage = []

count = 0
print("start keyboard recording...")

def save_log(json_object):
    file_name = 'data/'+str(time.time()).replace(".","_")+'.json'
    with open(file_name, 'w') as outfile:
        json.dump(json_object, outfile)

def on_press(key):
    global storage
    try:
        json_object = {'action':'pressed_key', 'key':key.char, '_time': time.time()}
        print(json_object)
        storage.append(json_object)
    except AttributeError:
        # if key == keyboard.Key.esc:
        #     return False
        json_object = {'action':'pressed_key', 'key':str(key), '_time': time.time()}
        print(json_object)
        
        storage.append(json_object)
        print(json_object)
    

def on_release(key):
    global storage
    try:
        json_object = {'action':'released_key', 'key':key.char, '_time': time.time()}
        storage.append(json_object)
    except AttributeError:
        json_object = {'action':'released_key', 'key':str(key), '_time': time.time()}
        storage.append(json_object)
    if(len(storage)>1):
        save_log(storage)
        storage = []




keyboard_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)



keyboard_listener.start()

keyboard_listener.join()
