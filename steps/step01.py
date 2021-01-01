# coding=<utf-8>
""" 기본 프레임 
(ref) https://youtu.be/bKPIcoou9N8?t=245
"""
from tkinter import Tk


root = Tk()
root.title("My first GUI")
root.geometry("640x480") # 가로 * 세로 (윈도우 창)

#root.resizable(False, False)  # width, height 값 변경 불가 (= 창 크기 변경 불가)
root.resizable(True, True)   # width, height 값 변경 가능 (= 창 크기 변경 가능)


root.mainloop()  # 창이 닫히지 않도록 계속 루프를 돌림 