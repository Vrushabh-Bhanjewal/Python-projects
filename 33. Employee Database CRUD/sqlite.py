import tkinter as tk
from PIL import ImageTk,Image 
from tkinter import filedialog
import sqlite3

root=tk.Tk()
root.title('File Open')
root.geometry('400x500')

conn=sqlite3.connect('address_book.db',autocommit=True)
c=conn.cursor()
# * create table
# c.execute('''create table address (
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text,
#           zipcode integer
#           )
# ''')

# * Frame
window=tk.Frame(root,padx=10)
window.pack(pady=20)

def submit():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    # for fun must create/close again connection,cursor obj

    # check value
    try:
        a=int(zipcode.get())
        status_label.config(text='Status: Added Succesfully')
    except ValueError:
        status_label.config(text='Status: error! zip code must be integer')
        return
    
    # * insert Data
    c.execute('insert into address values(?,?,?,?,?,?)',(first.get(),last.get(),address.get(),city.get(),state.get(),zipcode.get()))

    # For delete after select
    first.delete(0,tk.END)
    last.delete(0,tk.END)
    address.delete(0,tk.END)
    city.delete(0,tk.END)
    state.delete(0,tk.END)
    zipcode.delete(0,tk.END)

    conn.commit()
    conn.close()

def show():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()

    # * select 
    c.execute('select *,oid from address')
    sf=tk.Frame(window,padx=10,pady=10)
    sf.grid(row=9,column=0,columnspan=4)

    if(c.rowcount==0):
        tk.Label(sf,text='No data found').pack()
        return
    status_label.config(text='Status: Showing Data')
    tk.Label(sf,text='First\tLast\tAddress\tCity\tState\tZipcode\tid',pady=10,bd=2,fg='blue').pack()
    while True:
        data = c.fetchone()
        if not data:
            break
        s1=''
        for i in data:
            s1=s1+str(i)+"\t"

        tk.Label(sf,text=s1).pack()
        # print('one: ',data)
    # print("All Data: ",c.fetchall())

    conn.commit()
    conn.close()

def delid():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    try:
        a=id.get() 
        if(not a):
            status_label.config(text='Status: Enter id to Delete')
            return
        c.execute('delete from address where oid=?',(a))
        id.delete(0,tk.END)
    except ValueError as e:
        status_label.config(text='Status: error'+e)
        return
    
    conn.commit()
    conn.close()

def editid():
    try:
        conn=sqlite3.connect('address_book.db')
        c=conn.cursor()
        a=id.get() 
        if(not a):
            status_label.config(text='Status: ID not Given')
            id.delete(0,tk.END)
            return
        c.execute('select * from address where oid=?',(a,))
        res=c.fetchone()
        # print(res)
        if not res:
            status_label.config(text='Status: No Data Found ')
            id.delete(0,tk.END)
            return
        
    except ValueError:
        status_label.config(text='Status: Wrong ID ')
        return
        
    edit=tk.Tk()
    edit.title('Update Data')
    edit.geometry('400x400')

    # * editer frame
    editer=tk.Frame(edit,padx=10)
    editer.pack(pady=20)

    # * labels
    first_label=tk.Label(editer,text='First Name').grid(row=0,column=0)
    last_label=tk.Label(editer,text='Last Name').grid(row=1,column=0)
    address_label=tk.Label(editer,text='Address Name').grid(row=2,column=0)
    city_label=tk.Label(editer,text='City Name').grid(row=3,column=0)
    state_label=tk.Label(editer,text='State Name').grid(row=4,column=0)
    zipcode_label=tk.Label(editer,text='Zip Code Name').grid(row=5,column=0)
    update_label=tk.Label(editer,text='Status: ',padx=10,fg='red')
    update_label.grid(row=6,column=0,columnspan=2)

    # * input
    first=tk.Entry(editer,width=30)
    first.grid(row=0,column=1)
    last=tk.Entry(editer,width=30)
    last.grid(row=1,column=1)
    address=tk.Entry(editer,width=30)
    address.grid(row=2,column=1)
    city=tk.Entry(editer,width=30)
    city.grid(row=3,column=1)
    state=tk.Entry(editer,width=30)
    state.grid(row=4,column=1)
    zipcode=tk.Entry(editer,width=30)
    zipcode.grid(row=5,column=1)

    # enter data
    first.insert(0,res[0])
    last.insert(0,res[1])
    address.insert(0,res[2])
    city.insert(0,res[3])
    state.insert(0,res[4])
    zipcode.insert(0,res[5])
    
    def saveid():
        try:
            conn=sqlite3.connect('address_book.db')
            c=conn.cursor()
            # check value
            a=int(zipcode.get())
            update_label.config(text='Status: Updated Succesfully')

            # * insert Data
            c.execute('update address set first_name=?, last_name=?, address=?, city=?, state=?, zipcode=? where oid=?',(first.get(),last.get(),address.get(),city.get(),state.get(),zipcode.get(),id.get()))
            edit.destroy()
        except ValueError:
            update_label.config(text='Status: error! zip code must be integer')
        except :
            update_label.config(text='Status: error occured')
        finally:
            conn.commit()
            conn.close()

    # * Save Data btn
    u1=tk.Button(editer,text='Update Data',padx=10,command=saveid)
    u1.grid(row=7,column=0,columnspan=2)
    
    conn.commit()
    conn.close()
    editer.mainloop()

# * labels
first_label=tk.Label(window,text='First Name').grid(row=0,column=0)
last_label=tk.Label(window,text='Last Name').grid(row=1,column=0)
address_label=tk.Label(window,text='Address Name').grid(row=2,column=0)
city_label=tk.Label(window,text='City Name').grid(row=3,column=0)
state_label=tk.Label(window,text='State Name').grid(row=4,column=0)
zipcode_label=tk.Label(window,text='Zip Code Name').grid(row=5,column=0)
status_label=tk.Label(window,text='Status: ',padx=10,fg='red')
status_label.grid(row=6,column=0,columnspan=2)
id_label=tk.Label(window,text='Select ID').grid(row=10,column=0)

# * input
first=tk.Entry(window,width=30)
first.grid(row=0,column=1)
last=tk.Entry(window,width=30)
last.grid(row=1,column=1)
address=tk.Entry(window,width=30)
address.grid(row=2,column=1)
city=tk.Entry(window,width=30)
city.grid(row=3,column=1)
state=tk.Entry(window,width=30)
state.grid(row=4,column=1)
zipcode=tk.Entry(window,width=30)
zipcode.grid(row=5,column=1)
id=tk.Entry(window,width=30)
id.grid(row=10,column=1)

# * Add Data
btn1=tk.Button(window,text='Add Data',command=submit,padx=20)
btn1.grid(row=7,column=0,columnspan=2)

# * Show Data
btn2=tk.Button(window,text='Show Data',padx=20,command=show)
btn2.grid(row=8,column=0,columnspan=2,pady=20)

# * Delete Data
btn3=tk.Button(window,text='Delete Data',padx=20,command=delid)
btn3.grid(row=11,column=0,columnspan=2,pady=20)

# * Update Data
btn4=tk.Button(window,text='Update Data',padx=10,command=editid)
btn4.grid(row=12,column=0,columnspan=2)

conn.commit()
conn.close()
root.mainloop()

