from tkinter import Tk
from tkinter import Button
from tkinter import Text
from tkinter import Frame

# test2String.py
# a program to convert text a into formatted string 
#
# Gary Davenport
# garydavenport73@gmail.com
# 4/29/2021

def paste():
    print("paste pressed")
    try:
        text1.insert("insert",root.clipboard_get())
        print(root.clipboard_get())
    except:
        print("no clipboard contents")

def clear():
    print("clear pressed")
    text1.delete("1.0","end")
    text2.delete("1.0","end")
    
def convert():
    print("convert pressed ")
    rawString=repr(text1.get("1.0","end"))
    #rawString=rawString.replace("\'" , chr(92)+chr(39))
    rawString=rawString.replace("\"" , chr(92)+chr(34))
    rawString=rawString[1:-1]
    text2.delete("1.0","end")
    #text2.insert("insert",rawString[:-2])
    text2.insert("insert",rawString)
    print("\nHere's your string:\n\n"+rawString+"\n")
    
def copy():
    print("copy pressed")
    root.clipboard_clear()
    root.clipboard_append(text2.get("1.0","end")[:-1])
    print(text2.get("1.0","end")+"\ncopied to clipboard.")
    
def close():
    root.destroy()

root=Tk()
root.title("Text2String")

topframe=Frame(root)
bottomframe=Frame(root)

topframe.pack(fill="both",expand=1)
bottomframe.pack(fill="x")

topframe.columnconfigure(0, weight=1)
topframe.columnconfigure(1, weight=1)
topframe.rowconfigure(0, weight=1)

text1=Text(topframe, width=34)
text2=Text(topframe, width=34)

text1.grid(column=0, row=0, sticky='nsew')
text2.grid(column=1, row=0, sticky='nsew')

btnPaste=Button(bottomframe,text="Paste", width=14, command=paste)
btnClear=Button(bottomframe,text="Clear", width=14, command=clear)
btnConvert=Button(bottomframe,text="Convert", width=14, command=convert)
btnCopy=Button(bottomframe,text="Copy String", width=14, command=copy)
btnClose=Button(bottomframe,text="Close", width=14, command=close)

btnPaste.pack(padx=5,pady=4, side="left", fill="x",expand=1)
btnClear.pack(padx=5,pady=4,side="left", fill="x",expand=1)
btnConvert.pack(padx=5,pady=4,side="left", fill="x",expand=1)
btnCopy.pack(padx=5,pady=4,side="left", fill="x",expand=1)
btnClose.pack(padx=5,pady=4,side="left", fill="x",expand=1)

root.mainloop()