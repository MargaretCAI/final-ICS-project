import tkinter as tk
import tkinter.messagebox
import hit_the_plane
import pygame


window = tk.Tk()
window.title('Super 6+1')
window.geometry('1000x900')

#创建右方frame
frame_r = tk.Frame(window)
frame_r.pack(side='right', anchor='ne')

#创建右上方第一个frame
frame_1 = tk.Frame(frame_r) #frame_left的上方frame
frame_1.pack(side='top', anchor='ne')

#创建画布，放logo
canvas_1 = tk.Canvas(frame_1, bg='light blue', height = 130, width= 530)
image_file_1 = tk.PhotoImage(file='pic.gif')
image = canvas_1.create_image(250, 0, anchor='n', image=image_file_1)
canvas_1.pack(side='top')
#创建标题
l = tk.Label(frame_1, text='Welcome to Super 6+1', bg='orange', font=('Arial', 20), width=45, height=5)
l.pack(side='top')

#创建右方第二个frame,插入两个玩家的头像
frame_2 = tk.Frame(frame_r)
frame_2.pack(side='top')
canvas_2 = tk.Canvas(frame_2, bg='#FFD700', height=100,width=200)
image_file_2 = tk.PhotoImage(file='player1.gif')
image = canvas_2.create_image(100,0,anchor='n', image=image_file_2)
canvas_2.pack(side='right', padx=5, pady=50)


frame_3 = tk.Frame(frame_r)
frame_3.pack(side='top')
canvas_3 = tk.Canvas(frame_2, bg='#6495ED', height=100, width=200)
image_file_3 = tk.PhotoImage(file='player2.gif')
image = canvas_3.create_image(100,0,anchor='n',image=image_file_3)
canvas_3.pack(side='right', padx=30,pady=50)

#创建记分板
frame_4 = tk.Frame(frame_r)
frame_4.pack(side='top')
l = tk.Label(frame_4, text='这是记分板', bg='#F0FFF0', font=('楷体', 20), width=40, height=5)
l.pack(side='top', padx=10, pady=10)

#主持人头像
frame_5 = tk.Frame(frame_r)
frame_5.pack(side='bottom', anchor='se')
canvas_4 = tk.Canvas(frame_5, bg='#D2B48C', height=200, width=110)
image_file_4 = tk.PhotoImage(file='host.gif')
image = canvas_4.create_image(100, 60, anchor='e',image=image_file_4)
canvas_4.pack(side='right', padx=30, pady=30)

#创建九宫格
#创建左方frame
frame_l = tk.Frame(window)
frame_l.pack(side='left', anchor='nw')

#创建title;一个frame
frame_a = tk.Frame(frame_l)
frame_a.pack(side='top', anchor='nw')
l1 = tk.Label(frame_a, text='You are always charmed by gamble', bg='#DEB887', font=("Times", "27", "bold italic"), width=45, height=5)
l1.pack(side='top')

frame_e = tk.Frame(frame_l)
frame_e.pack(side='top', anchor='nw')
l2 = tk.Label(frame_e, text='Choose one button that charms you most', bg='#FFA07A', font=("Times", "20" ), width=45, height=5)
l2.pack(side='top')

#9个游戏的函数
STATE_1 = 1
STATE_2 = 1
STATE_3 = 1
STATE_4 = 1
STATE_5 = 1
STATE_6 = 1
STATE_7 = 1
STATE_8 = 1
STATE_9 = 1

def game1():
    global STATE_1
    if STATE_1 == 1:
        a = tkinter.messagebox.askyesno(title='Hi, Warrior', message='If you win, you will get a point; lose, get nothing.')
        if a == True:
            hit_the_plane.main()
            result = hit_the_plane.win
            if result == True:#游戏胜利
                tkinter.messagebox.askyesno(title='Game over', message='You win')
                STATE_1 = 0
            else:
                tkinter.messagebox.askyesno(title='Game over', message='You lose ')
    elif STATE_1 == 0:
            print('This game has been tried. Please click another number')

#第一个游戏的测试函数
def game2():
    a = tkinter.messagebox.askyesno(title='Hi, Warrior', message='If you win, you will get a point; lose, get nothing.')
    if a == True:
        hit_the_plane.main()
        result = hit_the_plane.win
        if result == True:  # 游戏胜利
            tkinter.messagebox.askyesno(title='Game over', message='You win')

        else:
            tkinter.messagebox.askyesno(title='Game over', message='You lose ')




#打开游戏的class
class play_game():
    def __init__(self, state, number, game):#game 是导入的module
        self.state = state
        self.message = 'If you win, you will get ' + str(number) + ' point; otherwise, get nothing'
        self.game = game

    def check(self):
        global STATE_1
        if STATE_1 == 1:
            a = tkinter.messagebox.askyesno(title='Hi, Warrior', message='If you win, you will get a point; lose, get nothing.')
            if a == True:
                hit_the_plane.main()
                result = hit_the_plane.win
                if result == True:  # 游戏胜利
                    tkinter.messagebox.askyesno(title='Congratulations', message='You win')
                    STATE_1 = 0
                else:
                    tkinter.messagebox.askyesno(title='Game over', message='You lose ')
        elif STATE_1 == 0:
            print('This game has been tried. Please click another number')


def hit_me():
    pass





#创建第一行的三个按钮
frame_b = tk.Frame(frame_l)
frame_b.pack(side='top')

a1 = tk.Button(frame_b, text='1', font=("Times", "20", "bold italic"), width=5, height=2,command=play_game(STATE_1, 1, hit_the_plane).check)#这里的函数不能有括号
a1.pack(side='left', anchor='w',padx=30, pady=30)

# a2 = tk.Button(frame_b, text='2', font=("Times", "20", "bold italic"), width=5, height=2,command=play_game(STATE_2, 2, f2).check)
# a2.pack(side='left', padx= 30, pady=30)
#
# a3 = tk.Button(frame_b, text='3', font=("Times", "20", "bold italic"), width=5, height=2,command=play_game(STATE_3, 3, f3).check)
# a3.pack(side='left', padx=30, pady=30)
#
# #创建第二行的三个按钮
# frame_c = tk.Frame(frame_l)
# frame_c.pack(side='top')
#
# a4 = tk.Button(frame_c, text='4', font=("Times", "20", "bold italic"), width=5, height=2,command=play_game(STATE_4, 4, f4).check)
# a4.pack(side='left', anchor='w',padx=30, pady=30)
#
# a5 = tk.Button(frame_c, text='5', font=("Times", "20", "bold italic"), width=5, height=2,command=play_game(STATE_5, 5, f5).check)
# a5.pack(side='left', anchor='w',padx=30, pady=30)
#
# a6 = tk.Button(frame_c, text='6', font=("Times", "20", "bold italic"), width=5, height=2,command=play_game(STATE_6, 6, f6).check)
# a6.pack(side='left', anchor='w',padx=30, pady=30)
#
# #创建第三行的三个按钮
# frame_d = tk.Frame(frame_l)
# frame_d.pack(side='top')
#
# a7 = tk.Button(frame_d, text='7', font=("Times", "20", "bold italic"), width=5, height=2,command=play_game(STATE_7, 7, f7).check)
# a7.pack(side='left', anchor='w',padx=30, pady=30)
#
# a8 = tk.Button(frame_d, text='8', font=("Times", "20", "bold italic"), width=5, height=2,command=play_game(STATE_8, 8, f8).check)
# a8.pack(side='left', anchor='w',padx=30, pady=30)
#
# a9 = tk.Button(frame_d, text='9', font=("Times", "20", "bold italic"), width=5, height=2,command=play_game(STATE_9, 9, f9).check)
# a9.pack(side='left', anchor='w',padx=30, pady=30)





window.mainloop()






