#Jayden Williams
#9/19
#Alarm clock
import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound

h = 0
m = 0
s = 0
t = "am"


def current_time(h,m,s,t):
    total_seconds = calendar.timegm(time.gmtime())
    current_second = total_seconds%60

    total_minutes= total_seconds//60
    current_minute=total_minutes%60

    total_hours = total_minutes//60
    current_hour = (total_hours%24)-6

    am_pm= " "
    if current_hour>=12:
        current_hour=current_hour-12
        am_pm="PM"
        if current_hour ==0:
            current_hour=current_hour+12
    else:
        am_pm="AM"
        if current_hour==0:
            current_hour=current_hour+12
    alarm = str(h) +":" +str(m)+":"+str(s)+t
    timex= str(current_hour)+":"+str(current_minute)+":"+str(current_second)+am_pm

    if timex == alarm:
        beep()

    
    return timex
def beep():
    winsound.Beep(640,5000)

def show_time():
    global h
    global m
    global s
    global t
    time = current_time(h,m,s,t)
    txt.set(time)
    root.after(1000, show_time)

def get_alarm(*args):
    global h
    h = input("what hour")
    global m
    m = input("what minute")
    global s
    s = input("what second")
    global t
    t= input("am or pm").upper()
def quit(*args):
    root.destroy()


#create root window

root= Tk()
root.geometry("500x500")
root.attributes("-fullscreen",False)
root.title("Clock:")

#set window color background
root.configure(background="Black")
root.bind("x",quit)
root.bind("a",get_alarm)
root.after(1000, show_time)

fnt = font.Font(family='Agency',size = 60, weight='bold')
txt=StringVar()
#display time and set up the colors of text and background
lbl=ttk.Label(root,textvariable = txt, font= fnt, foreground="Red",background="Black")
#place time in center of screen
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#start main loop
root.mainloop()














