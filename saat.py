import datetime
import locale
import PySimpleGUI as gui
locale.setlocale(locale.LC_ALL,'turkish')
gui.theme('black')


    

   
layout = [[gui.Text('',key='_zaman_',pad=(0,120),size = (300,300),font=("Consolas",30),justification = 'center')]
         ]

window = gui.Window("Dijital Saat", layout,size =(300,300))

def zamaniGuncelle():
    return datetime.datetime.now().strftime('%H:%M:%S')

def main(pencere):
    
    while True:
        event, values = pencere.Read(timeout=10)
        if event in (None, 'Quit'):
            break
        pencere.FindElement('_zaman_').Update(zamaniGuncelle())

if __name__ == '__main__':
    main(window)



