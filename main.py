import base64
import PySimpleGUI as sg
import pyperclip
import keyboard
import pygetwindow
import time

base64.b64encode(bytes.fromhex("0264f62d0100")).decode()

def paste():
    keyboard.press_and_release('enter')
    keyboard.press('ctrl+v')
    time.sleep(0.2)
    keyboard.release('ctrl+v')
    keyboard.press_and_release('enter')

sg.theme('Reddit')
layout = [ 
    [sg.Text('Please enter the wanted legendary insight amount!')], 
    [sg.Text('Amount', size =(10, 1)), sg.InputText()], 
    [sg.Button('Generate', key='-gen-')]
]

if __name__ == '__main__':
    
    window = sg.Window('GW2 LI generator by Ladis', layout=layout, size=(400,100), keep_on_top = True, finalize=True)
    while True:
        event, values = window.read(timeout=1)
        if event == None:
            break
        if event == '-gen-':
            try:
                amount = int(values[0])
            except:
                sg.popup("please enter a number between 1 - 250!", keep_on_top= True)
                continue
            if amount > 250:
                sg.popup("please enter a number between 1 - 250!", keep_on_top= True)
                continue
            if amount <16:
                hexed_amount = "0" + str(hex(amount).lstrip("0x").rstrip("L"))
            else:
                hexed_amount = hex(amount).lstrip("0x").rstrip("L")
            
            li_hexed = "02"+str(hexed_amount)+"f62d0100"
            chat_code = base64.b64encode(bytes.fromhex(li_hexed)).decode()
            chat_code = pyperclip.copy("[&"+str(chat_code)+"]")
            try:
                gw2 = pygetwindow.getWindowsWithTitle("Guild Wars 2")[0]
            except:
                sg.popup("It seems like Guild wars 2 is not running!", keep_on_top= True)
                continue
            gw2.activate()
            time.sleep(0.5)
            keyboard.press_and_release('esc')
            paste()
            paste()
            paste()
            paste()
            paste()
            
            # keyboard.press('enter')
            # keyboard.release('enter')


                