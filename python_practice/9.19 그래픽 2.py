from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

main = Tk()

def btnclick():
    name = tkinter.simpledialog.askstring("질문", "이름을 입력하시오")
    age = tkinter.simpledialog.askinteger("질문", "나이를 입력하시오")
    if name and age:
        tkinter.messagebox.showwarning("환영", str(age) + "세" + name + "님 반갑습니다.")

btn = Button(main, text = "클릭", foreground="Blue", command = btnclick)
btn.pack()

def btnclick2():
    if tkinter.messagebox.askokcancel("시스템종료", "정말 종료하시겠습니까?"):
        tkinter.messagebox.showwarning("bye", "안녕히가십시오.")
btn2 = Button(main, text = "종료", foreground="Black", command = btnclick2)
btn2.pack()

main.mainloop()
