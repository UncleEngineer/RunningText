# https://github.com/UncleEngineer/RunningText/
# Follow Uncle: http://facebook.com/UncleEngineer/

from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as st


GUI = Tk()
w = 650
h = 700

ws = GUI.winfo_screenwidth() #screen width
hs = GUI.winfo_screenheight() #screen height


x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')
GUI.title('โปรแกรมไว้อ่านข่าวของลุง v.0.0.1')
#GUI.state('zoomed')
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

MAINTEXT = '''กด F1 รัน
กด P เพื่อหยุดชั่วคราว
กด R เพื่อรันต่อ
กด F2 หยุด+รีเซ็ต
กด F3 แก้ไขข้อความ
กด F5 เต็มจอ/ย่อ
กด F12 ปิดโปรแกรม
สวัสดีจ้าา
ลุงเองจ้าาาาา
ไม่มีอะไรทำ
เลยเขียนโปรแกรมเล่น
โปรแกรมสำหรับอ่านข่าว
สไลด์ข้อความขึ้น
อ่านเรื่อยๆ
ใช้ร้องเพลง
คาราโอเกะ
เราจะทำตามสัญญาได้
555
'''

def readtext():
	global MAINTEXT
	with open('runningtext.txt') as rt:
		settext = rt.read()
		MAINTEXT = settext

try:
	readtext()
except:
	with open('runningtext.txt','w') as rt:
		rt.writelines(MAINTEXT)
	readtext()



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

	def SaveText():
		data = textbox.get('1.0', END)
		MTEXT.set(data)
		with open('runningtext.txt','w') as rt:
			rt.writelines(MTEXT.get())
		readtext()
		MTEXT.set(MAINTEXT)
		EDT.destroy()

	Bsave = ttk.Button(EDT,text='Save Text',command=SaveText)
	Bsave.pack(ipadx=20,ipady=10)
	EDT.mainloop()

def Pause(event):
	MT.after_cancel(runafter)

def Resume(event):
	MoveText()


GUI.bind('<p>',Pause)
GUI.bind('<r>',Resume)
GUI.bind('<F1>', MoveText)
GUI.bind('<F2>',ResetText)
GUI.bind('<F3>',GUI2)
GUI.bind('<F12>',lambda x:GUI.destroy())
GUI.mainloop()
