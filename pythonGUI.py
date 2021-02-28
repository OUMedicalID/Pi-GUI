import tkinter as tk
import sys
import os

win = tk.Tk() 

win.title("Medical ID") 

win.resizable(False,False)

win.attributes('-fullscreen',True)

win.bind("<Escape>", lambda x: win.destroy())

titleLbl = tk.Label(win, text = "Medical ID\n__________________")


labelfont = ('Ariel', 40, 'bold')

titleLbl.config(font=labelfont)

titleLbl.config(fg='#03adfc')

label2 = tk.Label(win, text = "Scan Phone Here\n...")
label2.config(font=labelfont)


fName = "Yousif" 

label3 = tk.Label(win, text = "Data Transfer Complete!\nWelcome " + fName)
label3.config(font=labelfont)


def nfcScan():
	label2.destroy()
	simBtn.destroy()
	label3.pack(pady=300)
	win.after(5000,refresh) 

def refresh():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	


simBtn = tk.Button(text = "Simulate Scan", command = nfcScan) 





titleLbl.pack()
simBtn.pack()

label2.pack(pady=300)






win.mainloop() 

