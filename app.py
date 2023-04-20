# majd kell jobb kommenteles, fontos megjegyezni való!!!
# ja es az anime nem cringe csak rossz sztereotipiak terjednek a weebekrol, not my problem honestly
# coded by WSD a román

import PySimpleGUI as sg
import webbrowser as wb
import subprocess

ver = '1.0alpha'

colors = {'grey':'#23272a', 'green-b':'#3cb882', 'madebywsd':'#3c4043', 'green-b-not-available':'#8cb8a4'} # szinek :3


# a kalkulátornak a layoutja. két layout van, az egyik az amikor percet kalkulalsz, masik a jelentesiro
# jelenlegi elmeletem szerint ugy lesz megoldva, hogy gomb nyomasra bezarjuk az ablakot, majd egy ujat hozunk letre a megfelelo layoutra. 
# by default a kalkulator lesz
layoutCalculator = [
    # ----------------------------- FŐ, FELSŐ RÉSZ, Ő NEM FOG VÁLTOZNI MAJD -----------------------------
    [
        sg.Push(background_color=colors['grey']), # push for align
        sg.Text('Kalkulátor', text_color=colors['green-b'], tooltip='Itt vagy most!', background_color=colors['grey'], font='Calibri 25'), #text
        sg.Push(background_color=colors['grey']), # push for align
        sg.Image('img/logo.png', background_color=colors['grey'], key='-LOGO_IMG-', enable_events = True), #logo
        sg.Push(background_color=colors['grey']), # push for align
        sg.Text('Jelentésíró', background_color=colors['grey'], font='Calibri 25'), #text2
        sg.Push(background_color=colors['grey']), # push for align
    ], # logo, ketto diszito szoveg

    [
        sg.Push(background_color=colors['grey']), # push for align
        sg.Text('Mit szeretnél csinálni?', background_color=colors['grey'], font='Calibri 15', pad=20),
        sg.Push(background_color=colors['grey']) # push for align
    ], #szoveg gomb felett

    [
        sg.Push(background_color=colors['grey']), # push for align
        sg.Button('Kalkulátor', border_width=0, button_color=colors['green-b-not-available'], disabled=True, size=(26, 1), font="Calibri 18", key='-MODE_CALC-'),
        sg.Push(background_color=colors['grey']), # push for align
        sg.Button('Jelentésíró', border_width=0, button_color=colors['green-b'], size=(26, 1), font="Calibri 18", key='-MODE_REP-'),
        sg.Push(background_color=colors['grey']), # push for align
    ], #ket gomb


    [sg.Text('asd', font='Calibri 25', text_color=colors['grey'], background_color=colors['grey'])], # space lol haha

    # ----------------------------- INNENTŐL LEFELE LESZ A MÓD SPECIFIKUS CUCCOK -----------------------------

    [ # Kezdés text, és két input field. 
        sg.Push(background_color=colors['grey']),
        sg.Text('Kezdés időpontja:', font='Calibri 14', background_color=colors['grey']), 
        sg.Input( border_width=0, size=(3, 1), justification="center", key='-INPUT_H_START-'), 
        sg.Text('óra', font='Calibri 10', background_color=colors['grey']), 
        sg.Input(border_width=0, size=(3, 1), justification="center", key='-INPUT_M_START-'), 
        sg.Text('perc', font='Calibri 10', background_color=colors['grey']),
        sg.Push(background_color=colors['grey'])

    ], 

    [ # A vége text, két input field
        sg.Push(background_color=colors['grey']),
        sg.Text('Befejezés időpontja:', font='Calibri 14', background_color=colors['grey']), 
        sg.Input(border_width=0, size=(3, 1), justification="center", key='-INPUT_H_END-'), 
        sg.Text('óra', font='Calibri 10', background_color=colors['grey']), 
        sg.Input(border_width=0, size=(3, 1), justification="center", key='-INPUT_M_END-'), 
        sg.Text('perc', font='Calibri 10', background_color=colors['grey']),
        sg.Push(background_color=colors['grey']),
    ],

    [ # számítás gomb || eredetileg egy működő gomb volt, de 0.49.9 óta más feladata van.
      # mostmár csak arra használom, hogy helyet töltsön ki.
        sg.Push(background_color=colors['grey']),
        sg.Button('', border_width=0,button_color=colors['grey'], size=(26, 1), font="Calibri 18", disabled=True),
        sg.Push(background_color=colors['grey']),
    ],

    [
        sg.Text('A számítás eredménye: ', font='Calibri 14', background_color=colors['grey'], expand_x=True, justification="center", visible=False, key="-RESULT_TEXT-")
    ],

    # szoveg
    # a szoveg alapbol ures lesz, kalkulalas utan lesz update-elve, 
    # nem visibilityvel lesz megoldva mint 0.49.5 elott. szar rendszer, raadasul buggos is

    [
        sg.Text('', font='Calibri 14', background_color=colors['grey'], expand_x=True, justification="center", visible=False, key="-CONGRAT_TEXT-"),
    ],

    [
        sg.VPush(background_color=colors['grey']),
        
    ],

    [
        sg.Text('Log:', pad=(30, 20), background_color=colors['grey'], visible=False, key="-ERROR_LOG-")
    ],
    
    [
        sg.Text('Coded By WSD  |  V'+ver, font='Arial 8', justification='right', expand_x=True, text_color=colors['madebywsd'], background_color=colors['grey'], enable_events=True, key='WSD')
    ]

]

# maga az ablak
mw = sg.Window(
    'LRSZ Segédeszközök | Kalkulátor V' + ver,
    layoutCalculator, 
    icon='img/icon.ico', 
    size=(1000, 650), 
    resizable=False, 
    margins=(0, 0), 
    background_color=colors['grey']
)

modeNow = 'calc' # calc vagy rep

def errorText(text):
    szoveg = str(text)
    mw['-ERROR_LOG-'].update(visible=True)
    mw['-ERROR_LOG-'].update('Log: ' + szoveg)

def calc():
    rezultzero = False
    mw['-CONGRAT_TEXT-'].update(visible=False)
    mw['-RESULT_TEXT-'].update(visible=False)
    # ellenorzes hogy minden fieldbe van-e vmi
    if '' not in (values['-INPUT_H_START-'], values['-INPUT_M_START-'], values['-INPUT_H_END-'], values['-INPUT_M_END-']): 
            #mw['-ERROR_LOG-'].update(visible=False) # alapbol is false, de ha hiva utan ujra kalkulaljuk es jo, akkor a logot tuntesse el

            hs = values['-INPUT_H_START-'] # atnevezes a konnyebb kod kedveert
            ms = values['-INPUT_M_START-'] # atnevezes a konnyebb kod kedveert
            he = values['-INPUT_H_END-'] # atnevezes a konnyebb kod kedveert
            me = values['-INPUT_M_END-'] # atnevezes a konnyebb kod kedveert

            # ha minden fasza es minden szam, akkor megyunk tovabb csak
            if hs.isnumeric() and ms.isnumeric() and he.isnumeric() and me.isnumeric():
                # muveletek sorrendje itt kezdodik
                # HA a befejezes kissebb mint a kezdes, akkor 24-bol kivonjuk a kezdest, atalakitjuk percbe a kapott idot, 
                # majd a befejezest is atalakitjuk es egyszeruen hozzaadjuk
                # faszer magyarazok ennyit bar jo ha tudom mit csinalok (sokszor thats not the case lmao)
                # ja meg valamiert nem megy ha nem baszom az osszeset intre kinda szar

                if he < hs:
                    elsoresz = (24 - int(hs)) * 60 + int(ms)
                    masodik = int(he) * 60 + int(me)
                    result = elsoresz + masodik
                else:
                    result = (int(he) * 60 + int(me)) - (int(hs) * 60 + int(ms))

                if result < 0:
                    mw['-RESULT_TEXT-'].update(visible=False)
                    mw['-CONGRAT_TEXT-'].update(visible=False)
                    rezultzero = True
                #    mw['-ERROR_LOG-'].update(visible=True)
                #    mw['-ERROR_LOG-'].update('Log: Nem lehet a vége hamarabb, mint az eleje.')
                else:
                    mw['-RESULT_TEXT-'].update(visible=True)
                    mw['-RESULT_TEXT-'].update('A számítás eredménye: ' + str(result) + ' perc')

                    with open("percek.txt", "w") as f:
                        f.write(str(result))

                    # based on milyen eredményeket ért el a csávó, megdícsérjük! Vagy nem!
                    # előbb a textet beállítjuk úgy hogy látszódjon mert na. másképp yk nem igazán megy XD
                mw['-CONGRAT_TEXT-'].update(visible=True)
                if not rezultzero:
                    if result >= 0 and result <= 60:
                            mw['-CONGRAT_TEXT-'].update('Lehetett volna több is!')
                            mw['-ERROR_LOG-'].update(visible=False)
                    elif result > 60 and result <= 180:
                            mw['-CONGRAT_TEXT-'].update('Szép munka!')
                            mw['-ERROR_LOG-'].update(visible=False)
                    elif result > 180 and result <= 240:
                            mw['-CONGRAT_TEXT-'].update('Wow, sokat repültél!')
                            mw['-ERROR_LOG-'].update(visible=False)
                    elif result > 240:
                            mw['-CONGRAT_TEXT-'].update('Van életed? Nem úgy tűnik.')
                            mw['-ERROR_LOG-'].update(visible=False)
                else: 
                    mw['-CONGRAT_TEXT-'].update(visible=False)

                # Ha a szám check failed, akkor kiírja a hibát
            else:
                mw['-RESULT_TEXT-'].update(visible=False)
                mw['-ERROR_LOG-'].update(visible=True)
                mw['-ERROR_LOG-'].update('Log: Kérlek, csak számokat írj be.')



while True:

    # -------- alap dolgok --------
    event, values = mw.read(timeout=100)

    if event == sg.WIN_CLOSED:
        break
    # -------- end --------


    # -------- ha ráklikkelsz a logóra, megnyitja a jelentés részt fórumnál. ha már jelentésíró, legyen ilyen funkció is
    if event == '-LOGO_IMG-':
        wb.open('https://forum.see-game.com/forums/jelentesek.571/', 1, 1)
    # -------- end --------



    # -------- ez a rész limitálja azt, hogy hány számot lehet beírni az input widgetbe. kettőt enged jelenleg, több úgysem kell. --------
    if len(values['-INPUT_H_START-']) > 2:
        mw.Element('-INPUT_H_START-').Update(values['-INPUT_H_START-'][:-1])
    if len(values['-INPUT_M_START-']) > 2:
        mw.Element('-INPUT_M_START-').Update(values['-INPUT_M_START-'][:-1])
    if len(values['-INPUT_H_END-']) > 2:
        mw.Element('-INPUT_H_END-').Update(values['-INPUT_H_END-'][:-1])
    if len(values['-INPUT_M_END-']) > 2:
        mw.Element('-INPUT_M_END-').Update(values['-INPUT_M_END-'][:-1])
    # -------- end --------

    # -------- ha invalid az idő, akkor törli meg ilyenek yk -------
    if '' not in (values['-INPUT_H_START-'], values['-INPUT_M_START-'], values['-INPUT_H_END-'], values['-INPUT_M_END-']): 
        if values['-INPUT_H_START-'].isnumeric() and values['-INPUT_M_START-'].isnumeric() and values['-INPUT_H_END-'].isnumeric() and values['-INPUT_M_END-'].isnumeric():
            if int(values['-INPUT_H_START-']) > 24:
                mw.Element('-INPUT_H_START-').Update('')
                errorText('Hibás adat! Az óra nem lehet nagyobb 24-nél, a perc pedig 59-nél. A hibás mezők törölve lettek.')
                mw['-RESULT_TEXT-'].update(visible=False)
                mw['-CONGRAT_TEXT-'].update(visible=False)

            if int(values['-INPUT_M_START-']) > 59:
                mw.Element('-INPUT_M_START-').Update('')
                errorText('Hibás adat! Az óra nem lehet nagyobb 24-nél, a perc pedig 59-nél. A hibás mezők törölve lettek.')
                mw['-RESULT_TEXT-'].update(visible=False)
                mw['-CONGRAT_TEXT-'].update(visible=False)

            if int(values['-INPUT_H_END-']) > 24:
                mw.Element('-INPUT_H_END-').Update('')
                errorText('Hibás adat! Az óra nem lehet nagyobb 24-nél, a perc pedig 59-nél. A hibás mezők törölve lettek.')
                mw['-RESULT_TEXT-'].update(visible=False)
                mw['-CONGRAT_TEXT-'].update(visible=False)

            if int(values['-INPUT_M_END-']) > 59:
                mw.Element('-INPUT_M_END-').Update('')
                errorText('Hibás adat! Az óra nem lehet nagyobb 24-nél, a perc pedig 59-nél. A hibás mezők törölve lettek.')
                mw['-RESULT_TEXT-'].update(visible=False)
                mw['-CONGRAT_TEXT-'].update(visible=False)

    calc()

    #húsvéti tojás UwU >_< XDDDDDDDDDDDDDD
    if event == 'WSD':
        wb.open('https://i.postimg.cc/R069CSHg/unknown.png', 1, 1)

    if event == '-MODE_REP-':
        mw.close()
        cmd = ["python", "rep.py"]
        subprocess.Popen(cmd, creationflags=subprocess.CREATE_NO_WINDOW)


mw.close()