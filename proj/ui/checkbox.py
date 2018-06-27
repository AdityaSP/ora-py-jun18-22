import Tkinter as tk
def clickme():
    print "User selected"
    print [texts[idx] for idx, v in enumerate(interest_vars) if v.get()]

def select(num):
    for v in interest_vars:
        v.set(num)

def selectall():
    select(1)

def reset():
    select(0)

mw = tk.Tk()
s = tk.IntVar()

texts = ['Sports', 'Politics', 'Tech', 'Art', 'Baking', 'Fitness', 'Movies']
interest_vars = [tk.IntVar() for t in texts]

for t,v in zip(texts, interest_vars):
    cb = tk.Checkbutton(mw, variable = v, text = t)
    cb.pack()

button1 = tk.Button(mw, text= "Click me", command=clickme)
button1.pack()

button2 = tk.Button(mw, text= "Select all", command=selectall)
button2.pack()

button2 = tk.Button(mw, text= "Reset", command=reset)
button2.pack()
mw.mainloop()
