from tkinter import*
import tkinter.messagebox

main = Tk()
main.title("Tk Test")
main.geometry("800x600")

menubar = Menu(main)
main.config(menu = menubar)

popup = Menu(menubar)
menubar.add_cascade(label = "파일", menu = popup)

def about():
    tkinter.messagebox.showinfo("소개", "메뉴사용예제입니다.")

popup.add_command(label = "소개", command = about)
popup.add_command(label = "종료", command = quit)

main.mainloop()
