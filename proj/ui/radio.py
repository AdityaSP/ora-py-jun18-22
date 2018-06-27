import Tkinter as tk
def clickme():
    print "User selected"
    print package.get()
    print mealoption.get()

mw = tk.Tk()

package = tk.StringVar()
package.set('DAY_NIGHT_PACK')
r1 = tk.Radiobutton(mw,variable=package, text='Day', value='DAY_PACK')
r1.pack()
r2 = tk.Radiobutton(mw, variable=package, text='Night', value='DAY_NIGHT_PACK')
r2.pack()

mealoption = tk.StringVar()
mealoption.set('VEG')
r3 = tk.Radiobutton(mw, variable=mealoption, text='Veg', value='VEG')
r3.pack()
r4 = tk.Radiobutton(mw, variable=mealoption, text='Non-Veg', value='NON_VEG')
r4.pack()

button1 = tk.Button(mw, text= "Click me", command=clickme)
button1.pack()

mw.mainloop()