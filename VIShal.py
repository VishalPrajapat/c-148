from tkinter import *
import random

root=Tk()
root.title("list")
root.geometry("400x400")
no_list=Label(root)
sort_list=Label(root)
def randomlist():
    randlist=random.sample(range(1,1000),10)
    no_list["text"]="Random List: " + str(randlist)
    randlist.sort()
    sort_list["text"]="Sorted list: " + str(randlist)
btn=Button(root,text="show Random list",command=randomlist)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
no_list.place(relx=0.5,rely=0.6,anchor=CENTER)
sort_list.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()