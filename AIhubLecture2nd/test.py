from ast import Load
from tkinter import *
from tkinter import filedialog



root = Tk()
root.geometry("300x400")

menuBar = Menu(root)    #처음 메뉴바 initializing
"""
file open
"""
def Load(): #파일 열기 선언
    filename = filedialog.askopenfilename(title="열기",filetypes=(("text files","*.txt"),("all files","*.*")))  #열기에서 파일 type을 보여주는거
    print(filename)

    #text 창에 메모장 내용 load
    if(filename):
        file = open(filename,"rt", encoding="UTF8") #한글 출력을 위해 ENCODING을 UTF8을 이용한다.
        txt.delete("1.0",END)
        txt.insert(END, file.read())
            

fileMenu = Menu(menuBar)    #메뉴바에 붙일 fileMenu 선언
menuBar.add_cascade(label="File", menu = fileMenu)   #메뉴바에 file메뉴 붙이기

fileMenu.add_command(label="Open", command=Load)


"""
file save
"""
def Save():
    filename = filedialog.asksaveasfilename(title="다른 이름으로 저장",filetypes=(("text files","*.txt"),("all files","*.*")))  #다른 이름으로 저장
    print(filename)
    if filename:
        file = open(filename,"wt",encoding="UTF8")
        file.write(txt.get("1.0",END))

fileMenu.add_command(label="Save", command=Save)


fileMenu.add_separator()    # file메뉴 안에 줄 긋기
"""
exit
"""
def funcExit():
    root.destroy()

fileMenu.add_command(label="Exit",command=funcExit)


"""
text
"""
# 스크롤바
scrollBar = Scrollbar(root)
scrollBar.pack(side="right", fill="y") #오른쪽에 붙이기

#텍스트창
txt = Text(root,yscrollcommand=scrollBar.set)
txt.pack(side="left", fill="both",expand=True)

#연동
scrollBar.config(command=txt.yview)


root.config(menu=menuBar) # config를 해주어야 메뉴바가 나타난다.

root.mainloop()