import tkinter as tk
window=tk.Tk()
window.title('Simple Calculator')
window.geometry('300x360')
# window.resizable(False,False)

# predefine
lang='Times New Roman'
blue1='#021d47'
orange='#9c3905'
pad=20
num_size=(lang,14)
oper_size=(lang,14)


# input 
i1=tk.Entry(window,width=20,font=(lang,20))
i1.grid(row=0,column=0,pady=10,padx=10,columnspan=5)

# button
def btn_click(no):
    i1.insert(tk.END,f"{no}")

def btn_clear():
    i1.delete(0,tk.END)
def oper_click(p):
    i1.insert(tk.END,p)

def btn_eval():
    try:
        data=eval(i1.get())
        i1.delete(0,tk.END)
        i1.insert(0,str(data))
    except ZeroDivisionError:
        i1.delete(0,tk.END)
        i1.insert(0,'Divide by Zero Error')
    except:
        i1.delete(0,tk.END)
        i1.insert(0,'Error')
        
button_1=tk.Button(window,text='1',padx=pad+5,pady=pad,fg=blue1,font=num_size, command=lambda:btn_click(1))
button_2=tk.Button(window,text='2',padx=pad+5,pady=pad,fg=blue1,font=num_size, command=lambda:btn_click(2))
button_3=tk.Button(window,text='3',padx=pad+5,pady=pad,fg=blue1,font=num_size, command=lambda:btn_click(3))
button_4=tk.Button(window,text='4',padx=pad+5,pady=pad,fg=blue1,font=num_size, command=lambda:btn_click(4))
button_5=tk.Button(window,text='5',padx=pad+5,pady=pad,fg=blue1,font=num_size, command=lambda:btn_click(5))
button_6=tk.Button(window,text='6',padx=pad+5,pady=pad,fg=blue1,font=num_size, command=lambda:btn_click(6))
button_7=tk.Button(window,text='7',padx=pad+5,pady=pad,fg=blue1,font=num_size, command=lambda:btn_click(7))
button_8=tk.Button(window,text='8',padx=pad+5,pady=pad,fg=blue1,font=num_size, command=lambda:btn_click(8))
button_9=tk.Button(window,text='9',padx=pad+5,pady=pad,fg=blue1,font=num_size, command=lambda:btn_click(9))
button_0=tk.Button(window,text='0',padx=pad+5,pady=pad,fg=blue1,font=num_size, command=lambda:btn_click(0))

button_add=tk.Button(window,text='+',padx=pad+5,pady=pad,fg=orange,font=oper_size,command=lambda:oper_click('+'))
button_sub=tk.Button(window,text='-',padx=pad+5,pady=pad,fg=orange,font=oper_size,command=lambda:oper_click('-'))
button_mul=tk.Button(window,text='*',padx=pad+5,pady=pad,fg=orange,font=oper_size,command=lambda:oper_click('*'))
button_div=tk.Button(window,text='/',padx=pad+5,pady=pad,fg=orange,font=oper_size,command=lambda:oper_click('/'))
button_equal=tk.Button(window,text='=',padx=pad,pady=pad,fg=orange,font=oper_size,command=btn_eval)
button_clear=tk.Button(window,text='AC',padx=pad-5,pady=pad,fg=orange,font=oper_size, command=btn_clear)

button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)
button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)
button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)
button_0.grid(row=4 ,column=1)

button_add.grid(row=1,column=4)
button_sub.grid(row=2,column=4)
button_mul.grid(row=4,column=2)
button_div.grid(row=4,column=0)
button_equal.grid(row=4,column=4)
button_clear.grid(row=3,column=4)

window.mainloop()