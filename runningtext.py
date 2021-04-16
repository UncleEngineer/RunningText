# -*- coding: utf-8 -*-

# https://github.com/UncleEngineer/UncleNews/
# Follow Uncle: http://facebook.com/UncleEngineer/

from tkinter import *
from tkinter import ttk, messagebox
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

HELP = '''กด F1 รัน/เพิ่มความเร็ว
กด P เพื่อหยุดชั่วคราว
กด R เพื่อรันต่อ
กด F2 หยุด+รีเซ็ต/ลดความเร็ว
กด F3 แก้ไขข้อความ
กด F5 เต็มจอ/ย่อ
กด F10 วิธีใช้งาน
กด F12 ปิดโปรแกรม
กดลูกศรซ้าย/ขวา ปรับตำแหน่ง
กดลูกศรขึ้น/ลง ปรับขนาดฟอนต์
สวัสดีจ้าา
ลุงเองจ้าาาาา
ไม่มีอะไรทำ
เลยเขียนโปรแกรมเล่น
โปรแกรมสำหรับอ่านข่าว
สไลด์ข้อความขึ้น
อ่านเรื่อยๆ
ใช้ร้องเพลง
คาราโอเกะ
เราจะทำตามสัญญา
ขอเวลาอีกไม่นาน
...
...
ฮัมวี่มารับลุงแล้ว!
555

พัฒนาโดย: ลุงวิศวกร สอนคำนวณ
FB: https://www.facebook.com/UncleEngineer
YouTube: https://www.youtube.com/UncleEngineer
'''


MAINTEXT = '''กด F1 รัน/เพิ่มความเร็ว
กด P เพื่อหยุดชั่วคราว
กด R เพื่อรันต่อ
กด F2 หยุด+รีเซ็ต/ลดความเร็ว
กด F3 แก้ไขข้อความ
กด F5 เต็มจอ/ย่อ
กด F10 วิธีใช้งาน
กด F12 ปิดโปรแกรม
กดลูกศรซ้าย/ขวา ปรับตำแหน่ง
กดลูกศรขึ้น/ลง ปรับขนาดฟอนต์
สวัสดีจ้าา
ลุงเองจ้าาาาา
ไม่มีอะไรทำ
เลยเขียนโปรแกรมเล่น
โปรแกรมสำหรับอ่านข่าว
สไลด์ข้อความขึ้น
อ่านเรื่อยๆ
ใช้ร้องเพลง
คาราโอเกะ
เราจะทำตามสัญญา
ขอเวลาอีกไม่นาน
...
...
ฮัมวี่มารับลุงแล้ว!
555

พัฒนาโดย: ลุงวิศวกร สอนคำนวณ
'''


xpos = 80

fontsize = 80
FONT1 = (None,fontsize)

def readx():
	global xpos
	with open('xpos.txt') as rt:
		settext = rt.read()
		xpos = int(settext.strip())

def writex():
	with open('xpos.txt','w') as rt:
		rt.write(str(xpos))

try:
	readx()
except:
	writex()


def readfont():
	global fontsize
	with open('fontsize.txt') as rt:
		settext = rt.read()
		fontsize = int(fontsize.strip())

def writefont():
	with open('fontsize.txt','w') as rt:
		rt.write(str(fontsize))

try:
	readfont()
except:
	writefont()


def readtext():
	global MAINTEXT
	with open('runningtext.txt',encoding='utf-8') as rt:
		settext = rt.read()
		MAINTEXT = settext

try:
	readtext()
except:
	with open('runningtext.txt','w',encoding='utf-8') as rt:
		rt.writelines(MAINTEXT)
	readtext()



MTEXT = StringVar()
MTEXT.set(MAINTEXT)


MT = Label(GUI,textvariable=MTEXT,font=FONT1, foreground = green, background='black')
MT.place(x=xpos,y=0)
global ypos
global runafter

runafter = None

ypos = 0

def MoveText(event=None):
	global ypos
	global runafter
	MT.place(x=xpos,y=ypos)
	ypos -= 5
	runafter = MT.after(60,MoveText)
	
def ResetText(event=None):
	try:
		global ypos
		global runafter
		MT.place(x=50,y=0)
		ypos = 0
		MT.after_cancel(runafter)
	except:
		pass

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
		with open('runningtext.txt','w',encoding='utf-8') as rt:
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


def Right(event):
	global xpos
	xpos += 10
	writex()
	readx()
	MT.place(x=xpos,y=ypos)


def Left(event):
	global xpos
	xpos -= 10
	writex()
	readx()
	MT.place(x=xpos,y=ypos)


def FontInc(event):
	global FONT1
	global fontsize
	fontsize += 5
	FONT1 = (None,fontsize)
	MT.configure(font=FONT1)

def FontDec(event):
	global FONT1
	global fontsize
	fontsize -= 5
	FONT1 = (None,fontsize)
	MT.configure(font=FONT1)


GUI.bind('<Up>',FontInc)
GUI.bind('<Down>',FontDec)
GUI.bind('<Right>',Right)
GUI.bind('<Left>',Left)
GUI.bind('<p>',Pause)
GUI.bind('<r>',Resume)
GUI.bind('<F1>', MoveText)
GUI.bind('<F2>',ResetText)
GUI.bind('<F3>',GUI2)
GUI.bind('<F12>',lambda x:GUI.destroy())
GUI.bind('<F10>',lambda x:messagebox.showinfo('Help',HELP))
GUI.mainloop()
