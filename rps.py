from random import choice
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mess


def result(user):
    print(user)
    options = ('rock','paper','scissor')
    compu = choice(options)
    print(compu)
    if (user == compu):
        print('draw')
    elif (user == 'rock'):
        if (compu == 'scissor'):print('win')
        else: print('lose')
    elif (user == 'paper'):
        if (compu == 'rock'):print('win')
        else: print('lose')
    elif (user == 'scissor'):
        if (compu == 'paper'):print('win')
        else: print('lose')
        
window = Tk()
window.title("hello app")


for x,option in enumerate(options):
    butt = Button(window,text=option,width=10)
    butt.bind("<Button-1>",lambda event,user=option : result(event,user))
    butt.pack()
    window.update()

'''
butt1 = Button(window,text='Rock',command=lambda: result('rock'))
#butt1.pack()
butt1.grid(column=0,row=0)
butt2 = Button(window,text='Paper',command=lambda: result('paper'))
#butt2.pack()
butt2.grid(column=0,row=1)
butt3 = Button(window,text='Scissor',command=lambda: result('scissor'))
#butt3.pack()
butt3.grid(column=0,row=2)

'''

window.mainloop()
