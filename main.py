from tkinter import *
from random import *
from  datetime import datetime

window = Tk()
window.geometry('620x420')
window.resizable(width=False, height=False)
window.title('Main')
window.iconbitmap('img/logo.png')
window.config(bg='#FFE4C4')

# ------------------------------------------------------

count = 0

Click = Label(window, text='0', font='Arial 35', bg='#FFE4C4')
Click.place(x=300, y=40)

# ------------------------------------------------------


def add():
    inpt.insert(END, 'Hello')


def delete():
    inpt.delete(0, END)


def get():
    label_inpt['text'] = inpt.get()


inpt = Entry(window)
inpt.insert(0, 'Name')
inpt.place(x=20, y=20)

btn_go = Button(window, text='Go', font='Arial 15', command=get)
btn_go.place(x=20, y=60)

label_inpt = Label(window, bg='#FFE4C4', fg='Black')
label_inpt.place(x=550, y=20)

# ------------------------------------------------------

img = PhotoImage(file='img/logo.png')
logo = Label(window, image=img, bg='#FFE4C4')
logo.place(x=295, y=160)

# ------------------------------------------------------


def click():
    variations = ['scissors', 'paper', 'rock']
    value = choice(variations)
    label_variations.configure(text=value)
    global count
    count += 1
    Click.configure(text=count)


btn_rock = Button(window,
             text='Rock',
             command=click,
             font=('Arial', 20, 'bold'),
             width=10,
             height=1,
             bg='#F08080',
             activebackground='#CD5C5C',
             activeforeground='#FFF5EE',
             )
btn_rock.place(x=20, y=300)

btn_paper = Button(window,
             text='Paper',
             command=click,
             font=('Arial', 20, 'bold'),
             width=10,
             height=1,
             bg='#F08080',
             activebackground='#CD5C5C',
             activeforeground='#FFF5EE',
             )
btn_paper.place(x=220, y=300)

btn_scissors = Button(window,
             text='Scissors',
             command=click,
             font=('Arial', 20, 'bold'),
             width=10,
             height=1,
             bg='#F08080',
             activebackground='#CD5C5C',
             activeforeground='#FFF5EE',
             )
btn_scissors.place(x=420, y=300)

label_variations = Label(window,
             text='variations',
             font=('Arial', 20, 'bold'),
             width=10,
             height=1,
             bg='#F08080',
             activebackground='#CD5C5C',
             activeforeground='#FFF5EE',
             )
label_variations.place(x=220, y=240)

# ------------------------------------------------------

temp = 0
after_id =''


def timer():
    global temp, after_id
    after_id = window.after(1000, timer)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label_timer.configure(text=str(f_temp))
    temp += 1


def timerStart():
    btn_timer_start.pack_forget()
    btn_timer_stop.place(x=450, y=380)
    timer()


def timerStop():
    btn_timer_stop.pack_forget()
    btn_timer_continue.place(x=300, y=380)
    btn_timer_reset.place(x=250, y=380)
    window.after_cancel(after_id)


def timerContinue():
    btn_timer_continue.pack_forget()
    btn_timer_reset.pack_forget()
    btn_timer_stop.place(x=450, y=380)
    timer()


def timerReset():
    global temp
    temp = 0
    label_timer.configure(text='00:00')
    btn_timer_continue.pack_forget()
    btn_timer_reset.pack_forget()



label_timer = Label(window, font=('Arial', 15), text='00:00', bg='#FFE4C4')
label_timer.place(x=520, y=380)

btn_timer_start = Button(window, text='Start', font='Arial 10', command=timerStart)
btn_timer_stop = Button(window, text='Stop', font='Arial 10', command=timerStop)
btn_timer_continue = Button(window, text='Continue', font='Arial 10', command=timerContinue)
btn_timer_reset = Button(window, text='Reset', font='Arial 10', command=timerReset)
btn_timer_start.place(x=400, y=380)

window.mainloop()