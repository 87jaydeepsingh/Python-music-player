from tkinter import filedialog
from tkinter import *
import vlc
window=Tk()
frame=Frame(window)
frame1=Frame(window)
frame2=Frame(window)
l1=Label(window)
l2=Label(window)
list1=[]
i=0
j=0
global player1
def ofile():
    global filename
    global j
    filename=filedialog.askopenfilename()
    list1.append(filename)
    li1.insert(j,list1[j])
    j+=1
def play():
    global player1
    player1=vlc.MediaPlayer(str(list1[i]))
    player1.play()
    l1['text']="Currently-Playing:"+list1[i]
def next1():
    global player1
    player1.stop()
    global i
    i+=1
    player1=vlc.MediaPlayer(str(list1[i]))
    player1.play()
    l1['text']="Currently-Playing:"+list1[i]
def prev():
    global player1
    player1.stop()
    global i
    i-=1
    player1=vlc.MediaPlayer(str(list1[i]))
    player1.play()
    l1['text']="Currently-Playing:"+list1[i]
def pause():
    player1.pause()
    l1['text']="Currently-Playing:paused"
def stop():
    global i
    player1.stop()
    i=0
    l1['text']="Currently-Playing:Stoped"
b2=Button(frame,text="Add Songs",command=ofile,width=12,bd=1)
b3=Button(frame,text="Play",command=play,width=12,bd=1)
b4=Button(frame,text="Next",command=next1,width=12,bd=1)
b7=Button(frame,text="Previous",command=prev,width=12,bd=1)
b5=Button(frame,text="Stop",command=stop,width=12,bd=1)
b6=Button(frame,text="Pause",command=pause,width=12,bd=1)
l1=Label(frame1,text="Currently-Playing:no song")
li1=Listbox(frame2,width=92,height=10,bd=1,fg="White",bg="Black")
frame1.pack(side=TOP)
l1.pack()
frame.pack(side=BOTTOM)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b6.pack(side=LEFT)
b5.pack(side=LEFT)
b4.pack(side=LEFT)
b7.pack(side=LEFT)
frame2.pack()
li1.pack(side=LEFT)
window.mainloop()
