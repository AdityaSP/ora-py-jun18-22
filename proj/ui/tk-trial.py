import Tkinter as tk
def clickme():
    print "User clicked me"

mw = tk.Tk()
hello_label = tk.Label(mw, text='Hello UI')
hello_label.pack()
enter_label = tk.Label(mw, text='Enter your name')
enter_label.pack()
enter = tk.Entry(mw)
enter.pack()
button1 = tk.Button(mw, text= "Click me", command=clickme)
button1.pack()
r1 = tk.Radiobutton(mw, text='Day')
r1.pack()
r2 = tk.Radiobutton(mw, text='Night')
r2.pack()

cb1 = tk.Checkbutton(mw, text='Sports')
cb1.pack()
cb2 = tk.Checkbutton(mw, text='Politics')
cb2.pack()
cb3 = tk.Checkbutton(mw, text='Tech')
cb3.pack()
cb3 = tk.Checkbutton(mw, text='Art')
cb3.pack()


mw.mainloop()