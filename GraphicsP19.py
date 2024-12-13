from tkinter import *

def main():
    print('--> start <--')
    mainwin = Tk()
    wcan = Canvas(mainwin, bg='white', width=600, height=800)
    wcan.pack()
    
    wcan.create_oval(127, 200, 221, 299, fill='red', outline="black", width=5)
    wcan.create_oval(276, 200, 399, 302, fill='blue', outline="black", width=5)
    wcan.create_oval(74, 75, 524, 500, outline="black", width=5)
    wcan.create_rectangle(198, 326, 377, 349, fill='yellow', outline="black", width=7)
    points = [175, 450, 300, 550, 300, 530 , 225, 460]
    wcan.create_polygon(points, outline='black', fill='black', width=3)
    points = [350, 450, 175, 450, 225, 460 , 320, 460]
    wcan.create_polygon(points, outline='black', fill='black', width=3)
    points = [350, 450, 300, 550, 300, 530 , 320, 460]
    wcan.create_polygon(points, outline='black', fill='black', width=3)


    mainwin.mainloop()

main()
