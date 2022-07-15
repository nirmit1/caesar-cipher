import tkinter as tk

def cipher():
    s = ""
    txt = box1.get()
    key = int(box2.get())
    for i in txt:
        if 65 <= ord(i) <= 90:
            ct = ((((ord(i) - 65) + key) % 26) + 65)
            s = s + chr(ct)
        elif 97 <= ord(i) <= 122:
            ct = ((((ord(i) - 97) + key) % 26) + 97)
            s = s + chr(ct)
        else:
            s = s + i
    box3.delete(0, tk.END)
    box3.insert(0, s)


def decipher():
    s = ""
    txt = box1.get()
    key = int(box2.get())
    for i in txt:
        if 65 <= ord(i) <= 90:
            ct = ((((ord(i) - 65) - key) % 26) + 65)
            s = s + chr(ct)
        elif 97 <= ord(i) <= 122:
            ct = ((((ord(i) - 97) - key) % 26) + 97)
            s = s + chr(ct)
        else:
            s = s + i
    box3.delete(0, tk.END)
    box3.insert(0, s)


def clear():
    box1.delete(0, tk.END)
    box2.delete(0, tk.END)
    box3.delete(0, tk.END)


def end():
    exit()


root = tk.Tk()
root.title("Cipher/Di-cipher String")
root.geometry("450x300")

label1 = tk.Label(root, text="Your Text: ", font=("Arial", 14))
label1.place(x=20, y=20)

box1 = tk.Entry(root, font=("Arial", 14))
box1.place(x=180, y=20)

label2 = tk.Label(root, text="Enter Key: ", font=("Arial", 14))
label2.place(x=20, y=60)

box2 = tk.Entry(root, font=("Arial", 14))
box2.place(x=180, y=60, width=40)

button1 = tk.Button(root, text="Cipher", font=("Verdana", 12), bg="Blue", command=cipher)
button1.place(x=60, y=120, width=100)

button2 = tk.Button(root, text="De-cipher", font=("Verdana", 12), bg="Red", command=decipher)
button2.place(x=200, y=120, width=100)

label3 = tk.Label(root, text="Result text:  ", font=("Arial", 14))
label3.place(x=20, y=180)

box3 = tk.Entry(root, font=("Arial", 14))
box3.place(x=180, y=180)

button3 = tk.Button(root, text="Exit", font=("Verdana", 12), command=end)
button3.place(x=200, y=225, width=100)

button4 = tk.Button(root, text="Clear", font=("Verdana", 12), command=clear)
button4.place(x=60, y=225, width=100)

root.mainloop()