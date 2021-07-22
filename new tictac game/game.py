from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('Tic-Tac-Toe')
root.iconbitmap('icon.ico')

def put_sign(event, f):
    global current_player, current_sign
    l1 = Label(f, image=current_sign)
    l1.pack()
    if current_sign is zero:
        current_sign = cross
        current_player = 'Player 1'
        logic(f, 0)
    else:
        current_sign = zero
        current_player = 'Player 2'
        logic(f, 1)

def logic(f, v):
    global current_player
    if f is frame1:
        values[0] = v
    elif f is frame2:
        values[1] = v
    elif f is frame3:
        values[2] = v
    elif f is frame4:
        values[3] = v
    elif f is frame5:
        values[4] = v
    elif f is frame6:
        values[5] = v
    elif f is frame7:
        values[6] = v
    elif f is frame8:
        values[7] = v
    elif f is frame9:
        values[8] = v


    if values[0] == values[1] and values[1] == values[2] \
    or values[3] == values[4] and values[4] == values[5]\
    or values[4] == values[7] and values[7] == values[8]\
    or values[0] == values[3] and values[3] == values[6]\
    or values[1] == values[4] and values[4] == values[7]\
    or values[2] == values[5] and values[5] == values[8]\
    or values[0] == values[4] and values[4] == values[8]\
    or values[2] == values[4] and values[4] == values[6]:
        messagebox.showinfo('Tic-Tac-Toe', current_player+' wins')
        root.quit()
    else:
        f = 1
        for n in values:
            if n < 0:
                f = 0
                break
        else:
            if f == 1:
                messagebox.showinfo('Tic-Tac-Toe', 'Match is draw')
                root.quit()

values = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
zero = ImageTk.PhotoImage(Image.open('zero.png').resize((92,92)))
cross = ImageTk.PhotoImage(Image.open('cross.png').resize((92,92)))
current_player = 'Player 1'
current_sign = zero
frame1 = Frame(root, height=100, width=100,highlightbackground="#65bf21", highlightthickness=2)
frame2 = Frame(root, height=100, width=100,highlightbackground="#65bf21", highlightthickness=2)
frame3 = Frame(root, height=100, width=100,highlightbackground="#65bf21", highlightthickness=2)
frame4 = Frame(root, height=100, width=100,highlightbackground="#65bf21", highlightthickness=2)
frame5 = Frame(root, height=100, width=100,highlightbackground="#65bf21", highlightthickness=2)
frame6 = Frame(root, height=100, width=100,highlightbackground="#65bf21", highlightthickness=2)
frame7 = Frame(root, height=100, width=100,highlightbackground="#65bf21", highlightthickness=2)
frame8 = Frame(root, height=100, width=100,highlightbackground="#65bf21", highlightthickness=2)
frame9 = Frame(root, height=100, width=100,highlightbackground="#65bf21", highlightthickness=2)
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=0, column=2)
frame4.grid(row=1, column=0)
frame5.grid(row=1, column=1)
frame6.grid(row=1, column=2)
frame7.grid(row=2, column=0)
frame8.grid(row=2, column=1)
frame9.grid(row=2, column=2)

frame1.bind('<Button-1>',lambda event, f=frame1: put_sign(event, frame1))
frame2.bind('<Button-1>',lambda event, f=frame2: put_sign(event, frame2))
frame3.bind('<Button-1>',lambda event, f=frame3: put_sign(event, frame3))
frame4.bind('<Button-1>',lambda event, f=frame4: put_sign(event, frame4))
frame5.bind('<Button-1>',lambda event, f=frame5: put_sign(event, frame5))
frame6.bind('<Button-1>',lambda event, f=frame6: put_sign(event, frame6))
frame7.bind('<Button-1>',lambda event, f=frame7: put_sign(event, frame7))
frame8.bind('<Button-1>',lambda event, f=frame8: put_sign(event, frame8))
frame9.bind('<Button-1>',lambda event, f=frame9: put_sign(event, frame9))

messagebox.showinfo('Tic-Tac-Toe', 'Information\nPlayer 1 = O\nPlayer 2 = X')

root.mainloop()