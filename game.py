import random
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

try:
    screen = Tk()

    count = 0
    X_score = 0
    O_score = 0
    screen.title("tic tac toe")


    def breaks():
        global count
        a = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        if count < 9:
            for i in a:
                i['state'] = DISABLED
        count = 9


    def com_choice():
        global count
        a = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        com = random.choice(a)
        you_can = 0
        if count != 9:
            if com['state'] != DISABLED:
                com['image'] = o_img
                com['text'] = "O"
                winners()
                com['state'] = DISABLED
                count += 1

            else:
                for i in a:
                    if i['state'] == NORMAL:
                        you_can += 1
                if you_can > 1:
                    com_choice()
                else:
                    pass


    winner = True


    def winners():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9, winner, X_score, O_score, count
        if count <= 9:
            if (b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X") or (
                    b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X") or (
                    b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X") or (
                    b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X") or (
                    b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X") or (
                    b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X") or (
                    b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X") or (
                    b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X"):
                messagebox.showinfo("showinfo", "you won")
                X_score += 1
                buttons()

                count = 0

                winner = False
                # breaks()

            elif (b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O") or (
                    b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O") or (
                    b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O") or (
                    b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O") or (
                    b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O") or (
                    b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O") or (
                    b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O") or (
                    b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O"):

                messagebox.showinfo("showinfo", "computer won")
                O_score += 1
                buttons()

                count = 0

                winner = False
                # breaks()
        if count == 9:
            buttons()


    def click(b):
        global count
        if count == 9:
            pass
        if count != 9:
            b['image'] = x_img
            b['text'] = "X"
            winners()
            b['state'] = DISABLED

            com_choice()
            count += 1


    # images for X and O and also black image

    empty_img = ImageTk.PhotoImage(Image.open("images/empty.png"))
    x_img = ImageTk.PhotoImage(Image.open("images/x.png"))
    o_img = ImageTk.PhotoImage(Image.open("images/o.png"))


    def buttons():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9, X_score, O_score, count
        count = 0
        b1 = Button(screen, text="", image=empty_img, command=lambda: click(b1), padx=50, pady=50, borderwidth=0)
        b2 = Button(screen, text="", image=empty_img, command=lambda: click(b2), padx=50, pady=50, borderwidth=0)
        b3 = Button(screen, text="", image=empty_img, command=lambda: click(b3), padx=50, pady=50, borderwidth=0)

        b4 = Button(screen, text="", image=empty_img, command=lambda: click(b4), padx=50, pady=50, borderwidth=0)
        b5 = Button(screen, text="", image=empty_img, command=lambda: click(b5), padx=50, pady=50, borderwidth=0)
        b6 = Button(screen, text="", image=empty_img, command=lambda: click(b6), padx=50, pady=50, borderwidth=0)

        b7 = Button(screen, text="", image=empty_img, command=lambda: click(b7), padx=50, pady=50, borderwidth=0)
        b8 = Button(screen, text="", image=empty_img, command=lambda: click(b8), padx=50, pady=50, borderwidth=0)
        b9 = Button(screen, text="", image=empty_img, command=lambda: click(b9), padx=50, pady=50, borderwidth=0)

        b10 = Label(screen, text="O score", padx=40, pady=40)
        b10.grid(row=0, column=3)

        b10 = Label(screen, text="X score", padx=40, pady=40)
        b10.grid(row=1, column=3)

        b11 = Button(screen, text="reset", padx=40, pady=40, borderwidth=0, command=buttons)
        b11.grid(row=2, column=3)

        b12 = Button(screen, text="exit", bg="red", fg="white", padx=40, pady=40, command=screen.quit)
        b12.grid(row=2, column=4)

        b13 = Label(screen, text=X_score, font=("Arial", 25))
        b13.grid(row=1, column=4)

        b14 = Label(screen, text=O_score, font=("Arial", 25))
        b14.grid(row=0, column=4)

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)


    buttons()

    screen.mainloop()

except RecursionError:
    print("nice")
