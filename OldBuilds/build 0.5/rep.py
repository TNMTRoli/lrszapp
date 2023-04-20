import PySimpleGUI as sg
import webbrowser as wb
import subprocess

ver = '0.5'

colors = {'grey':'#23272a', 'green-b':'#3cb882', 'madebywsd':'#3c4043', 'green-b-not-available':'#8cb8a4'} # szinek :3

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


    [sg.Text('asd', font='Calibri 25', text_color=colors['grey'], background_color=colors['grey'])], # space lol haha

    # ----------------------------- INNENTŐL LEFELE LESZ A MÓD SPECIFIKUS CUCCOK -----------------------------
    
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
    background_color=colors['grey']
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

    if event == 'WSD':
        wb.open('https://i.postimg.cc/R069CSHg/unknown.png', 1, 1)

    if event == '-LOGO_IMG-':
        wb.open('https://forum.see-game.com/forums/jelentesek.571/', 1, 1)