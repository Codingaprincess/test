import tkinter
import tkinter.font
import pygame as pg

def click_btn():
    button["text"] = "생성되었습니다"


root = tkinter.Tk()
root.title("오프닝화면")
root.resizable(False, False)

cvs = tkinter.Canvas(root, width=1300, height=700)
cvs.pack()
gazou = tkinter.PhotoImage(file="village.png.png")    #이미지 불러오기
cvs.create_image(650, 350, image = gazou)           #이미지 위치 조정


label = tkinter.Label(root, text="이름을 입력해주세요", font=("System", 40))
label.place(x=425, y=300)

label = tkinter.Label(root, text="A story hidden in a village", font=("System", 100))
label.place(x=200, y=100)

button = tkinter.Button(root, text="눌러주세요", font=("System", 24), command=click_btn)
button.place(x=555, y=600)

entry = tkinter.Entry(width=50)
entry.place(x=475, y=400)




root.mainloop()