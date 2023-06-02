from pynput import mouse
from pynput import keyboard
import time
import json
import sys
import sys,glob,re
import datetime,os



def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


files = glob.glob('data/*.json')
for json_file in files:
    diff_sec = (datetime.datetime.now() - modification_date(json_file)).total_seconds()
    if(diff_sec>15):
        os.remove(json_file)
        print("remove file "+json_file)



name_of_recording = "TEST"
record_all = True
storage = []
print("start mouse recording...")

count = 0





def save_log(json_object):
    file_name = 'data/'+str(time.time()).replace(".","_")+'.json'
    with open(file_name, 'w') as outfile:
        json.dump(json_object, outfile)



def on_click(x, y, button, pressed):
    global storage
    json_object = {'action':'pressed' if pressed else 'released', 'button':str(button), 'x':x, 'y':y, '_time':time.time()}
    print(json_object)
    storage.append(json_object)

    # print(len(storage))
    if len(storage) > 1:
        if (pressed == False):
            # files = glob.glob('data/*.json')
            # for json_file in files:
            #     diff_sec = (datetime.datetime.now() - modification_date(json_file)).total_seconds()
            #     if(diff_sec>5):
            #         os.remove(json_file)
            #         print("remove file "+json_file)
                
            print("*:::::::::: save log *::::::::::::::")
            save_log(storage)
            storage = []
            

mouse_listener = mouse.Listener(
        on_click=on_click)

mouse_listener.start()
mouse_listener.join()