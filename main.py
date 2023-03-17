from  tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(bg="yellow")
window.config(pady=50, padx=50,height=750)

canvas = Canvas(bg="aliceblue", width=800, height=400)
canvas.grid(row=0, column=0, columnspan=2)

spacer01 = Label(text="", bg="yellow", height=2)
spacer01.grid(column=0, row=1)

but_cross = Button()
img_cross = PhotoImage(file="images/wrong.png")
but_cross.config(image=img_cross)
but_cross.grid(column=0, row=2)

but_check = Button()
img_check = PhotoImage(file="images/right.png")
but_check.config(image=img_check, pady=25)
but_check.grid(column=1, row=2)








# stayin alive
window.mainloop()
