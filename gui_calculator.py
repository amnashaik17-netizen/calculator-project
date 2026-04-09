import tkinter as tk

def click(x):
    entry.insert(tk.END, x)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
'7','8','9','/',
'4','5','6','*',
'1','2','3','-',
'0','C','=','+'
]

r = 1
c = 0

for b in buttons:
    cmd = lambda x=b: click(x)

    if b == '=':
        cmd = equal
    elif b == 'C':
        cmd = clear

    tk.Button(root, text=b, width=5, height=2, command=cmd).grid(row=r, column=c)

    c += 1
    if c > 3:
        c = 0
        r += 1

root.mainloop()