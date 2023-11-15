# All imports for the script
import time
from tkinter import *
from tkinter import messagebox
from functools import partial
import subprocess
import os
 
 
# creating Tk window for the gui
root = Tk()
  
# setting geometry of tk window for the gui
root.geometry("300x600")
  
# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Bye Bye ssh")
  
# Declaration of variables for the timer
minute=StringVar()
second=StringVar()
  
# setting the default value as 0 for the timer so that it ticks down
minute.set("0")
second.set("15")
  
# Use of Entry class to take input from the user
  
minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=110,y=20)
  
secondEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=140,y=20)
  
# Submit is the function that starts the timer as well as messes with the process
# By editing the values in this function it allows the user to aim the attack against a service 
# as well as what happens when the timer runs out
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        global temp 
    except:
        print("Please input the right value")
    while temp >-1:
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
     
         
        # using format () method to store the value up to
        # two decimal places
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "ssh is dead X( ")
            os.system('rev ~/.ssh/config')
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
 
 
# Add_time is the function that allows for the button to add 10 seconds to the timer each time its pressed
def add_time(secs):
    global temp
    if temp < 170:
        temp = temp + int(10)
    
# Restart function will start the process to make sure that it is running correctly when the script is ran    
def restart():
    global temp
    if temp < 1:
        os.system('rev ~/.ssh/config')
        temp = 180

# More things for the gui
bg = PhotoImage(file = "/puppet/puppet.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 70)

# Adding the button and assignig it the function to add 10 seconds 
temp = int(minute.get())*60 + int(second.get())
add_button = Button(root, text="+10", font=('',20),command=partial(add_time, 10))
add_button.place(x = 55,y = 210)
restart_button = Button(root, text="restart", font=('',20),command=partial(restart))
restart_button.place(x = 55,y = 300)
# button widget
submit()
  

root.protocol("WM_DELETE_WINDOW", disable_event)
# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()