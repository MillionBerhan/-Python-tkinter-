import tkinter as tk

# schijf hier tussen je code

def achtergrondgeel():
    window.config(bg="Yellow")

def achtergrondzwart():
    window.config(bg="Black")

window = tk.Tk()

achtergrondzwart()

button = tk.Button(
    text='Switch light on!',
    bg="black", 
    fg="white",
    command = achtergrondgeel
)
button.pack(
    pady = 20,
    padx = 20
)

button = tk.Button(
    text='Switch light off!',
    bg="black", 
    fg="white",
    command = achtergrondzwart
)

button.pack(
    pady = 20,
    padx = 20
)
window.geometry("200x200")
window.mainloop()

