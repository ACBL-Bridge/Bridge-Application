from tkinter import *

remain = 11
_timer = None
def cdtimerr():
    global remain, _timer
    remain -= 1
    cdtext = canvas.create_text(510, 6, text=remain, font="Ubuntu 29 bold", anchor=NW)
    if remain == 0:
        canvas.delete(ALL)
    else:
        _timer = canvas.after(1000, lambda: (canvas.delete(cdtext), cdtimerr()))

root = Tk()
root.geometry('1024x768')
canvas = Canvas(root)
canvas.pack(expand=1, fill=BOTH)
_timer = canvas.after(0, cdtimerr)
Button(root, text='Cancel', command=lambda: canvas.after_cancel(_timer)).pack()
root.mainloop()