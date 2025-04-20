# Import Module
from tkinter import *
from main import main, notification_get

# create root window
root = Tk()

# root window title and dimension
root.title("Pomodoro Timer")
# Set geometry (widthxheight)
root.geometry('400x100')

##################################################################################################


#Label and text 1
label1 = Label(root, text='How many minutes would you like to work?')
label1.grid()

text1 = Entry(root, width=15)
text1.grid(column=1, row=0)

#Label and text 2
label2= Label(root, text='How many minutes would you like your breaks to be?')
label2.grid()

text2 = Entry(root, width=15)
text2.grid(column=1, row=1)

#Label and text 3
label3 = Label(root, text='How many cycles would you like this to last?')
label3.grid()

text3 = Entry(root, width=15)
text3.grid(column=1, row=2)

def save():
    x = text1.get()
    y = text2.get()
    z = text3.get()

    x = int(x)
    y = int(y)
    z = int(z)

    main(x, y, z)

def end():
    exit()


button1 = Button(root, text='Start', fg='green', command=save)
button1.grid(column=0, row=4)

button2 = Button(root, text='End', fg='red', command=end)
button2.grid(column=1, row=4)


########################################################################################

#Execute
root.mainloop()