import time, random
from tkinter import *

win = False
a = 0
tk = Tk()
can = Canvas(tk, width=1000, height=1000)
can.pack()
can.focus_set()
file_photo_fon = "D:/Программирование/Python/fly_bird/images/fon.png"
photo_fon = PhotoImage(file=file_photo_fon)
for y in range(3):
    for x in range(3):
        can.create_image(155 + 310 * x, 155 + 310 * y, image=photo_fon)
file_photo_bird = "D:/Программирование/Python/fly_bird/images/bird.png"
file_photo_trub_1 = "D:/Программирование/Python/fly_bird/images/труба.png"
file_photo_trub_2 = "D:/Программирование/Python/fly_bird/images/труба_2.png"
photo_bird = PhotoImage(file=file_photo_bird)
bird = can.create_image(300, 500, image=photo_bird)
photo_trub_1 = PhotoImage(file=file_photo_trub_1)
trub_1 = can.create_image(795, 700, image=photo_trub_1)
photo_trub_2 = PhotoImage(file=file_photo_trub_2)
trub_2 = can.create_image(795, 100, image=photo_trub_2)
trub_3 = can.create_image(1200, 700, image=photo_trub_1)
trub_4 = can.create_image(1200, 100, image=photo_trub_2)
trubs_2 = False
record = []


def up(event):
    can.move(bird, 0, -40)
    tk.update()


while not win:
    can.move(bird, 0, 10)
    can.move(trub_1, -10, 0)
    can.move(trub_2, -10, 0)
    can.move(trub_3, -10, 0)
    can.move(trub_4, -10, 0)
    if can.coords(bird)[1] + 95 > 850 or can.coords(bird)[1] < 60 or (can.coords(bird)[0] + 130 >= can.coords(trub_1)[0] and can.coords(bird)[1] + 100 > can.coords(trub_1)[1]) or (can.coords(bird)[0] + 120 >= can.coords(trub_2)[0] and can.coords(bird)[1] < can.coords(trub_2)[1] + 171):
        win = True
        can.unbind("<space>")
        fail = Label(tk, text="fail", font=("Arial", 23), fg="red")
        fail.place(relx=0.5, rely=0.5, anchor=CENTER)
        record.append(a)
    if trubs_2:
        if can.coords(bird)[1] + 95 > 850 or can.coords(bird)[1] < 60 or (can.coords(bird)[0] + 130 >= can.coords(trub_3)[0] and can.coords(bird)[1] + 100 > can.coords(trub_3[1]) or (can.coords(bird)[0] + 120 >= can.coords(trub_4)[0] and can.coords(bird)[1] < can.coords(trub_4)[1] + 171)):
            win = True
            can.unbind("<space>")
            fail = Label(tk, text="fail", font=("Arial", 23), fg="red")
            fail.place(relx=0.5, rely=0.5, anchor=CENTER)
            record.append(a)
    if can.coords(trub_1)[0] < -103 or can.coords(trub_2)[0] < -103:
        if trubs_2:
            random_y = random.randint(300, 500)
            random_x = random.randint(300, 500)
            trub_1 = can.create_image(1000 + random_x, random_y+400, image=photo_trub_1)
            trub_2 = can.create_image(1000 + random_x, random_y-400, image=photo_trub_2)
            trubs_2 = False
    if can.coords(trub_3)[0] < -103 or can.coords(trub_4)[0] < -103:
            random_y = random.randint(300, 500)
            trub_3 = can.create_image(1000, random_y+400, image=photo_trub_1)
            trub_4 = can.create_image(1000, random_y-400, image=photo_trub_2)
            trubs_2 = True
    for y in range(10):
        if can.coords(trub_1)[0] == 305+y or can.coords(trub_3)[0] == 305+y:
            a += 1
            l = Label(tk, text=a)
            l.place(relx=0.1, rely=0.1, anchor=CENTER)
    tk.update()
    can.bind("<space>", up)
    time.sleep(0.2)
tk.mainloop()
