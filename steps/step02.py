# coding = <utf-8> 

""" 버튼 위젯 
(ref) https://youtu.be/bKPIcoou9N8?t=526
"""
import os
import os.path as osp 

from tkinter import Tk, Button, PhotoImage


root = Tk()
root.title("My GUI")

btn1 = Button(root, text="버튼1") # 버튼 객체 초기화 
btn1.pack() # mainloop() 에 버튼이 표출되도록 함 

btn2 = Button(root, padx=5, pady=10, text='버튼2')  # 디폴트 버튼 박스 크기에서 패딩(padding)
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text='버튼3')
btn3.pack()

btn4 = Button(root, width=10, height=3, text='버튼4') # 고정 박스 크기를 직접 설정 
btn4.pack()

btn5 = Button(root, fg='red', bg="yellow", text='버튼5') # foreground, background 색상
btn5.pack()


img_path = osp.join(os.getcwd(), 'steps', 'images', 'button.png')  # 이미지로 버튼 만들기
photo = PhotoImage(file=img_path)
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭되었습니다.")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop()