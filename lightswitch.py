import tkinter as tk
# schijf hier tussen je code
text = str or float
lijstbenodigdheden=["Light is on","Light is off"]
lijstachtergronden=["Yellow","Black"]
lijstberichten=["Switch the light off","Switch the light on"]
counter = 0


def benodigheden():
    global counter
    if counter > 1:
        counter = 0
    print(lijstbenodigdheden[counter])
    window.config(bg=lijstachtergronden[counter])
    button["text"] = lijstberichten[counter]
    counter+=1

window = tk.Tk()

window.config(bg="Black")

button = tk.Button(
    text= "Switch the light on",
    bg="white", 
    fg="black",
    command = benodigheden 
)

button.pack(
    pady = 20,
    padx = 20
)

window.geometry("200x200")

window.mainloop()



