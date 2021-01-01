# coding = <utf-8> 

""" 레이블  
(ref) https://youtu.be/bKPIcoou9N8?t=1050

글자나 이미지를 보여주는 용도. 기능은 없음 
"""
import os
import os.path as osp 

from tkinter import Tk, Label, PhotoImage, Button


root = Tk()
root.title("My GUI")
root.geometry("640x480") 


label1 = Label(root, text="안녕하세요") # 레이블 객체 초기화 
label1.pack() # mainloop() 에 버튼이 표출되도록 함 


img_path = osp.join(os.getcwd(), 'steps', 'images', 'button.png')  # 이미지로 버튼 만들기
photo = PhotoImage(file = img_path)
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또 만나요")  # "안녕하세요" -> "또 만나요"  로 label1 의 값이 바뀜 


    global photo2  # 함수가 반환 되어도 값을 유지시키기 위해서
    img_path = osp.join(os.getcwd(), 'steps', 'images', 'like.png')  # 이미지로 버튼 만들기
    photo2 = PhotoImage(file = img_path)
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change) # 버튼을 클릭했을 때 레이블의 값을 프로그램 실행중에 바꾸기 
btn.pack()


root.mainloop()