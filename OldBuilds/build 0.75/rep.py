import PySimpleGUI as sg
import webbrowser as wb
import subprocess

#[CENTER][IMG width="495px"]https://kepkuldes.com/images/831043a8837a1041c516f1ce9873b73a.png[/IMG]
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Teljes név: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]
#
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Rendfokozat: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]
#
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Beosztás: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]
#
#[IMG]https://kepkuldes.com/images/26590e0284c27766c551bd01459e305c.png[/IMG]
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Pilóta: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]
#
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Másodpilóta: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]
#
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Kísérő: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]
#
#[IMG]https://kepkuldes.com/images/26590e0284c27766c551bd01459e305c.png[/IMG]
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Egységszám: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]
#
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Lajstromszám: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]
#
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Felszállás helye és ideje: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz
#xxxx.xx.xx xx:xx[/SIZE][/I][/COLOR]
#
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Leszállás helye és ideje: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz
#xxxx.xx.xx xx:xx[/SIZE][/I][/COLOR]
#
#[IMG]https://kepkuldes.com/images/26590e0284c27766c551bd01459e305c.png[/IMG]
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Repülés típusa: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]
#
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Repült percek: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]
#
#[I][IMG]https://kepkuldes.com/images/26590e0284c27766c551bd01459e305c.png[/IMG][/I]
#[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Légi járőrszolgálat részletes leírása: [/B][/FONT][/COLOR][/SIZE]
#[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE][/CENTER]
#
#[RIGHT][FONT=book antiqua][COLOR=rgb(204, 204, 204)][SIZE=5]Aláírás:[/SIZE][/COLOR][/FONT]
#[FONT=Brush Script MT][SIZE=5][COLOR=#009fd4][I]Válasz[/I][/COLOR][/SIZE][/FONT][/RIGHT]

ver = '0.75'

colors = {'grey':'#23272a', 'green-b':'#3cb882', 'madebywsd':'#3c4043', 'green-b-not-available':'#8cb8a4', 'debug':'#23272a'} # szinek :3

minta = {
    'nev':'[CENTER][IMG width="495px"]https://kepkuldes.com/images/831043a8837a1041c516f1ce9873b73a.png[/IMG]' + \
          '\n[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Teljes név: [/B][/FONT][/COLOR][/SIZE]' + \
          '\n[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]\n\n',

    'rendfok':'[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Rendfokozat: [/B][/FONT][/COLOR][/SIZE]' + \
              '\n[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]\n\n',
    
    'beoszt':'[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Beosztás: [/B][/FONT][/COLOR][/SIZE]' + \
             '\n[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]\n\n',
    
    'pilota':'[IMG]https://kepkuldes.com/images/26590e0284c27766c551bd01459e305c.png[/IMG]' + \
               '[SIZE=6][COLOR=rgb(128, 128, 128)][FONT=georgia][B] Pilóta: [/B][/FONT][/COLOR][/SIZE]' + \
               '[SIZE=5][COLOR=rgb(204, 204, 204)][I] Válasz [/I][/COLOR][/SIZE]',
    
    
    
    'otodik':'',
    'hatodik':'',
}

def logiras(nev, rendfok, beoszt, pilota, masod, kisero, nr, start, end, type, min, detail):
    var = minta['nev'].replace("Válasz", nev) + \
    minta['rendfok'].replace("Válasz", rendfok) + \
    minta['beoszt'].replace("Válasz", beoszt) + \
    minta['pilota'].replace("Válasz", pilota)

    print(var)




layoutRep = [
    # ----------------------------- FŐ, FELSŐ RÉSZ, Ő NEM FOG VÁLTOZNI MAJD -----------------------------
    [
        sg.Push(background_color=colors['grey']), # push for align
        sg.Text('Kalkulátor', background_color=colors['grey'], font='Calibri 25'), #text
        sg.Push(background_color=colors['grey']), # push for align
        sg.Image('img/logo.png', background_color=colors['grey'], key='-LOGO_IMG-', enable_events = True), #logo
        sg.Push(background_color=colors['grey']), # push for align
        sg.Text('Jelentésíró', text_color=colors['green-b'], tooltip='Itt vagy most!', background_color=colors['grey'], font='Calibri 25'), #text2
        sg.Push(background_color=colors['grey']), # push for align
    ], # logo, ketto diszito szoveg

    [
        sg.Push(background_color=colors['grey']), # push for align
        sg.Text('Mit szeretnél csinálni?', background_color=colors['grey'], font='Calibri 15', pad=20),
        sg.Push(background_color=colors['grey']) # push for align
    ], #szoveg gomb felett

    [
        sg.Push(background_color=colors['grey']), # push for align
        sg.Button('Kalkulátor', border_width=0, button_color=colors['green-b'], size=(26, 1), font="Calibri 18", key='-MODE_CALC-'),
        sg.Push(background_color=colors['grey']), # push for align
        sg.Button('Jelentésíró', border_width=0, button_color=colors['green-b-not-available'], disabled=True, size=(26, 1), font="Calibri 18", key='-MODE_REP-'),
        sg.Push(background_color=colors['grey']), # push for align
    ], #ket gomb


    [sg.Text('asd', font='Calibri 14', text_color=colors['grey'], background_color=colors['grey'])], # space lol haha

    # ----------------------------- INNENTŐL LEFELE LESZ A MÓD SPECIFIKUS CUCCOK -----------------------------
    
    [
        sg.Push(background_color=colors['grey']), sg.Text('Teljes neved:', size=(11, 1), justification='right', font='Calibri 14', background_color=colors['grey']),
        sg.Input(size=(20, 1), border_width=0, key='-NAME-'), 

        sg.Text('Pilóta: ', size=(12, 1), justification='right', font='Calibri 14', background_color=colors['grey']),
        sg.Input(size=(20, 1), border_width=0, key='-PILOT-'), 

        sg.Text('Repülés kezdete: ', size=(16, 1), justification='right', font='Calibri 14', background_color=colors['grey']),
        sg.Input(size=(20, 1), border_width=0, key='-START-'), sg.Push(background_color=colors['grey']),
    ],

    [
        sg.Push(background_color=colors['grey']), sg.Text('Rendfokozat:', size=(11, 1), justification='right', font='Calibri 14', background_color=colors['grey']),
        sg.Input(size=(20, 1), border_width=0, key='-RANK-'),

        sg.Text('Másodpilóta: ', size=(12, 1), justification='right', font='Calibri 14', background_color=colors['grey']),
        sg.Input(size=(20, 1), border_width=0, key='-COPILOT-'),

        sg.Text('Repülés vége: ', size=(16, 1), justification='right', font='Calibri 14', background_color=colors['grey']),
        sg.Input(size=(20, 1), border_width=0, key='-END-'), sg.Push(background_color=colors['grey']),
    ],

    [
        sg.Push(background_color=colors['grey']), sg.Text('Beosztás:', size=(11, 1), justification='right', font='Calibri 14', background_color=colors['grey']),
        sg.Input(size=(20, 1), border_width=0, key='-POSITION-'),

        sg.Text('Kísérő: ', size=(12, 1), justification='right', font='Calibri 14', background_color=colors['grey']),
        sg.Input(size=(20, 1), border_width=0, key='-KISERO-'),

        sg.Text('Egységszám: ', size=(16, 1), justification='right', font='Calibri 14', background_color=colors['grey']),
        sg.Input(size=(20, 1), border_width=0, key='-NR-'), sg.Push(background_color=colors['grey']),
    ],



    [
        sg.Text('Légi járőrszolgálat részletes leírása:', expand_x=True, justification='center', font='Calibri 14', background_color=colors['grey']),
    ],

    [sg.Input(expand_x=True, border_width=0, pad=(35, 5), key='-DETAIL-')],

    [
        sg.Push(background_color=colors['grey']), 
        sg.Button('Output', font='Calibri 14', button_color=colors['green-b'], border_width=0, key='-OUTPUT_BUT-'), 
        sg.Push(background_color=colors['grey']),
        sg.Multiline('var', size=(80, 5)), 
        sg.Push(background_color=colors['grey'])
    ],

    # ----------------------------- LENTI RÉSZ -----------------------------
    [sg.VPush(background_color=colors['grey'])],

    [
        sg.Text('Coded By WSD  |  V'+ver, font='Arial 8', justification='right', expand_x=True, text_color=colors['madebywsd'], background_color=colors['grey'], enable_events=True, key='WSD')
    ]

]

mw = sg.Window(
    'LRSZ Segédeszközök | Jelentésíró V' + ver,
    layoutRep, 
    icon='img/icon.ico', 
    size=(1000, 600), 
    resizable=False, 
    margins=(0, 0), 
    background_color=colors['debug']
)



while True:

    # -------- alap dolgok --------
    event, values = mw.read()

    if event == sg.WIN_CLOSED:
        break
    # -------- end --------

    if event == '-MODE_CALC-':
        mw.close()
        cmd = ["python", "app.py"]
        subprocess.Popen(cmd, creationflags=subprocess.CREATE_NO_WINDOW)

    if event == '-OUTPUT_BUT-': #def logiras(nev, rendfok, beoszt, pilota, masod, kisero, nr, start, end, type, min, detail):
        #-NAME- -PILOT- -START- -RANK- -COPILOT- -END- -POSITION- -KISERO- -NR-
        logiras(values['-NAME-'], values['-RANK-'], values['-POSITION-'], values['-PILOT-'], values['-COPILOT-'], values['-KISERO-'] \
                , values['-NR'], values['-START-'], values['-END-'])

    if event == 'WSD':
        wb.open('https://i.postimg.cc/R069CSHg/unknown.png', 1, 1)

    if event == '-LOGO_IMG-':
        wb.open('https://forum.see-game.com/forums/jelentesek.571/', 1, 1)