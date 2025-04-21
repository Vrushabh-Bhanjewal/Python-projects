import tkinter as tk
from PIL import ImageTk,Image

window=tk.Tk()
window.title('Images ')
window.geometry('1200x1500')
# window.resizable(False,False)
font1=('Times New Roman',14)

# ? icon
window.iconbitmap(r'avalanche.ico')

# ? image
img1=ImageTk.PhotoImage(Image.open(r'Castle.png'))
img2=ImageTk.PhotoImage(Image.open(r'Balloon.png'))
img3=ImageTk.PhotoImage(Image.open(r'Car.png'))
img4=ImageTk.PhotoImage(Image.open(r'Deer.png'))
img5=ImageTk.PhotoImage(Image.open(r'Holiday.png'))
img6=ImageTk.PhotoImage(Image.open(r'Riding.png'))
img7=ImageTk.PhotoImage(Image.open(r'Lavender.png'))

img_list=[img1,img2,img3,img4,img5,img6,img7]
cur_img=0
il1=tk.Label(image=img_list[cur_img])
il1.grid(row=0,column=0,columnspan=5)

def next_img():
    global cur_img
    global il1
    global img_list
    il1.grid_forget()
    if(cur_img == (len(img_list)-1) ):
        next_btn.config(state='disabled')
    else:
        cur_img+=1
        il1=tk.Label(image=img_list[cur_img])
        next_btn.config(state='normal')
    prev_btn.config(state='normal')
    il1.grid(row=0,column=0,columnspan=4)
    status_lbl.config(text=f'Status {cur_img + 1} of {len(img_list)}')

def prev_img():
    global cur_img
    global il1
    global img_list
    il1.grid_forget()
    if(cur_img==0):
        prev_btn.config(state='disabled')
    else:
        cur_img-=1
        prev_btn.config(state='normal')
        il1=tk.Label(image=img_list[cur_img])
    next_btn.config(state='normal')
    il1.grid(row=0,column=0,columnspan=4)
    status_lbl.config(text=f'Status {cur_img + 1} of {len(img_list)}')

# prev
prev_btn=tk.Button(window,text='<<',padx=10,font=font1,command=prev_img,state='disabled')
prev_btn.grid(row=1,column=0,pady=10)

# ? exit application btn
exit_btn=tk.Button(window,text='Exit',command=window.quit,padx=30,font=font1)
exit_btn.grid(row=1,column=2,pady=10)

# next
next_btn=tk.Button(window,text='>>',padx=10,font=font1,command=next_img,state='active')
next_btn.grid(row=1,column=3,pady=10)

# status label
status_lbl=tk.Label(window,text=f'Status {cur_img} of {len(img_list)}',font=font1,bd=1,padx=20,relief='sunken',anchor='e',justify='right')
status_lbl.grid(row=2,column=1,columnspan=5)

window.mainloop()