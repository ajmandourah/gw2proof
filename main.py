import base64
import PySimpleGUI as sg
import pyperclip
import keyboard
import pygetwindow
import time

#defining various killing proof
#w1
vale = "892f0100"
gorseval = "b72f0100"
sabetha = "a02f0100"
#w2
sloth = "8a2f0100"
matthias = "6f2f0100"
#w3
kc = "36340100"
xera = "5e340100"
#w4
carin = "ef3a0100"
Murssat = "8d390100"
samarog = "d7380100"
demios = "9e3a0100"
#w5
desmina = "e94f0100"
statue = "284f0100"
dhuum = "814e0100"
#w6
ca = "df590100"
twin = "1c5b0100"
qadim = "455a0100"
#w7
sabir = "86640100"
adina = "6e640100"
qadim2 = "27640100"

li = "f62d0100"

def paste():
    keyboard.press_and_release('enter')
    keyboard.press('ctrl+v')
    time.sleep(0.2)
    keyboard.release('ctrl+v')
    keyboard.press_and_release('enter')

def getCode(n,kp):
    li_hexed = "02"+str(n)+kp
    chat_code = base64.b64encode(bytes.fromhex(li_hexed)).decode()
    chat_code = pyperclip.copy("[&"+str(chat_code)+"]")

sg.theme('Reddit')
layout = [ 
    [sg.Text('Choose he KP\LI you want to ping!'),
    sg.Combo([
        "Legendary Insight",
        "W1 Vale Gurdian",
        "W1 Gorseval",
        "W1 Sabetha",
        "W2 Sloth",
        "W2 Matthaias",
        "W3 KC",
        "W3 Xera",
        "W4 Carin",
        "W4 Murssat",
        "W4 Samarog",
        "W4 Demios",
        "W5 Desmina",
        "W5 Statue",
        "W5 Dhuum",
        "W6 CA",
        "W6 Twin",
        "W6 Qadim",
        "W7 Sabir",
        "W7 Adina",
        "W7 Quadim"
    ],default_value="Legendary Insight")],
    [sg.Text('Amount', size =(10, 1)), sg.InputText(default_text=1)], 
    [sg.Button('Generate', key='-gen-'), sg.Text('how many pings', size =(15, 1)), sg.InputText(default_text=1)]
]

if __name__ == '__main__':
    
    window = sg.Window('GW2proof by Ladis', layout=layout, size=(400,100), keep_on_top = True, finalize=True)
    while True:
        event, values = window.read(timeout=1)
        if event == None:
            break
        if event == '-gen-':
            try:
                amount = int(values[1])
                ping = int(values[2])
            except:
                sg.popup("please enter a number between 1 - 250!", keep_on_top= True)
                continue
            if amount > 250 or amount < 1 or ping > 5 or ping < 1:
                sg.popup("please enter a number between 1 - 250! \n Also thr ping amount should not exceed 5 !", keep_on_top= True)
                continue
            if amount <16:
                hexed = "0" + str(hex(amount).lstrip("0x").rstrip("L"))
            else:
                hexed = hex(amount).lstrip("0x").rstrip("L")
            
            toPing = values[0]
            if toPing == "Legendary Insight":
                getCode(hexed, li)
            if toPing == "W1 Vale Gurdian":
                getCode(hexed, vale)                
            if toPing == "W1 Gorseval":
                getCode(hexed, gorseval)
            if toPing == "W1 Sabetha":
                getCode(hexed, sabetha)
            if toPing == "W2 Sloth":
                getCode(hexed, sloth)                
            if toPing == "W2 Matthaias":
                getCode(hexed, matthias)  
            if toPing == "W3 KC":
                getCode(hexed, kc)
            if toPing == "W3 Xera":
                getCode(hexed, xera)                
            if toPing == "W4 Carin":
                getCode(hexed, carin)
            if toPing == "W4 Murssat":
                getCode(hexed, Murssat)
            if toPing == "W4 Samarog":
                getCode(hexed, samarog)                
            if toPing == "W4 Demios":
                getCode(hexed, demios) 
            if toPing == "W5 Desmina":
                getCode(hexed, desmina)
            if toPing == "W5 Statue":
                getCode(hexed, statue)                
            if toPing == "W5 Dhuum":
                getCode(hexed, dhuum)  
            if toPing == "W6 CA":
                getCode(hexed, ca)
            if toPing == "W6 Twin":
                getCode(hexed, twin)                
            if toPing == "W6 Qadim":
                getCode(hexed, qadim)
            if toPing == "W7 Sabir":
                getCode(hexed, sabir)
            if toPing == "W7 Adina":
                getCode(hexed, adina)                
            if toPing == "W7 Quadim":
                getCode(hexed, qadim2) 

            try:
                gw2 = pygetwindow.getWindowsWithTitle("Guild Wars 2")[0]
            except:
                sg.popup("It seems like Guild wars 2 is not running!", keep_on_top= True)
                continue
            gw2.activate()
            time.sleep(0.5)
            keyboard.press_and_release('esc')
            for _ in range(ping):
                paste()

           


                
