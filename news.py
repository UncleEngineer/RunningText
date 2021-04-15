from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as st


GUI = Tk()
GUI.title('โปรแกรมไว้อ่านข่าวของลุง')
GUI.state('zoomed')
GUI.configure(background='black')
fullscreen = True
GUI.attributes("-fullscreen", fullscreen)

def Fullscreen(event):
    global fullscreen
    GUI.attributes("-fullscreen", not fullscreen)
    fullscreen = not fullscreen

GUI.bind('<F5>',Fullscreen)

green = '#00ff01'
FONT1 = (None,120)

MAINTEXT = '''สวัสดีจ้าา
ลุงเองจ้าาาาา
ไม่มีอะไรทำ
เลยเขียนโปรแกรมเล่น
'''

MTEXT = StringVar()
MTEXT.set(MAINTEXT)


MT = Label(GUI,textvariable=MTEXT,font=FONT1, foreground = green, background='black')
MT.place(x=50,y=0)
global ypos
global runafter

ypos = 0

def MoveText(event=None):
    global ypos
    global runafter
    MT.place(x=50,y=ypos)
    ypos -= 5
    runafter = MT.after(60,MoveText)
    
def ResetText(event=None):
	global ypos
	MT.place(x=50,y=0)
	ypos = 0
	MT.after_cancel(runafter)

def GUI2(event):
	EDT = Toplevel()

	w = 300
	h = 500

	ws = EDT.winfo_screenwidth() #screen width
	hs = EDT.winfo_screenheight() #screen height

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	EDT.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')
	textbox = st.ScrolledText(EDT,width=38,heigh=10,font=(None,30))
	textbox.pack(expand=True, fill='x')
	textbox.insert(INSERT,MTEXT.get())
	Bsave = ttk.Button(EDT,text='Save Text')
	Bsave.pack(ipadx=20,ipady=10)
	EDT.mainloop()


GUI.bind('<F1>', MoveText)
GUI.bind('<F2>',ResetText)
GUI.bind('<F3>',GUI2)
GUI.bind('<F12>',lambda x:GUI.destroy())
GUI.mainloop()
