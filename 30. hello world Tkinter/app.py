import tkinter as tk

window=tk.Tk()
window.title('First Tkinter App')
window.geometry('500x400')
window.resizable(False,False)
lang1='Times New Roman'

def hello():
    name=name_input.get()
    if(name):
        name_label.config(text=f'Hello {name}!')
    else:
        name_label.config(text='Hello World!')

title_label=tk.Label(window,text='First TKinter App',font=(lang1,16))
title_label.pack(pady=10)

name_input=tk.Entry(window,width=30,font=(lang1,14))
name_input.pack(pady=10)

btn=tk.Button(window,text='Submit',font=(lang1,14),command=hello)
btn.pack(pady=20)

name_label=tk.Label(window,text='',font=(lang1,14))
name_label.pack()

window.mainloop()
