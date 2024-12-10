from tkinter import *

def convertTemperature(Txtbox1, Txtbox2, Txtbox3, Txtbox4):
    try:
        KelvinInput = Txtbox1.get("1.0", "end-1c")
        if not KelvinInput:
            Txtbox4.delete('1.0', 'end')
            Txtbox4.insert('1.0', "Input cannot be blank")
            Txtbox1.config(bg='red')
            return 
        KelvinValue = float(KelvinInput)
        if KelvinValue <= 0:
            Txtbox4.delete('1.0', 'end')
            Txtbox4.insert('1.0', "Kelvin must be greater than 0")
            Txtbox1.config(bg='red')
            return
        Txtbox1.config(bg='white')
        Celsius = KelvinValue - 273.15
        Fahrenheit = (KelvinValue - 273.15) * 9 / 5 + 32
        Txtbox2.delete('1.0', 'end')
        Txtbox2.insert('1.0', Celsius)
        Txtbox3.delete('1.0', 'end')
        Txtbox3.insert('1.0', Fahrenheit)
        Txtbox4.delete('1.0', 'end')
    except ValueError:
        Txtbox4.delete('1.0', 'end')
        Txtbox4.insert('1.0', "Please enter a valid number")
        Txtbox1.config(bg='red')
def clearAll(Txtbox1, Txtbox2, Txtbox3, Txtbox4):
    Txtbox1.config(bg='white')
    Txtbox1.delete('1.0', 'end')
    Txtbox2.delete('1.0', 'end')
    Txtbox3.delete('1.0', 'end')
    Txtbox4.delete('1.0', 'end')
def main():
    Winmain = Tk()
    Winmain.geometry('800x600')
    Winmain.configure(bg='cyan')
    Top = Label(Winmain, text='Temperature Conversion', fg='White', bg='black', font=('Terminal', 25))
    Top.place(x=120, y=50)
    Kelvin = Label(Winmain, text='Kelvin:', fg='white', bg='black', font=('Terminal', 15))
    Kelvin.place(x=20, y=200)
    Celsius = Label(Winmain, text='Celsius:', fg='white', bg='black', font=('Terminal', 15))
    Celsius.place(x=20, y=250)
    Fahrenheit = Label(Winmain, text='Fahrenheit:', fg='white', bg='black', font=('Terminal', 15))
    Fahrenheit.place(x=20, y=300)
    Txtbox1 = Text(Winmain, width=20, height=1, font=('Terminal', 20))
    Txtbox1.place(x=130, y=195)
    Txtbox2 = Text(Winmain, width=20, height=1, font=('Terminal', 20))
    Txtbox2.place(x=130, y=250)
    Txtbox3 = Text(Winmain, width=20, height=1, font=('Terminal', 20))
    Txtbox3.place(x=145, y=300)
    Txtbox4 = Text(Winmain, width=20, height=2, font=('Terminal', 20))
    Txtbox4.place(x=260, y=355)
    Btn1 = Button(Winmain, text='Convert', command=lambda: convertTemperature(Txtbox1, Txtbox2, Txtbox3, Txtbox4))
    Btn1.place(x=300, y=450)
    Btn2 = Button(Winmain, text='Clear', command=lambda: clearAll(Txtbox1, Txtbox2, Txtbox3, Txtbox4))
    Btn2.place(x=500, y=450)
    Winmain.mainloop()
main()
