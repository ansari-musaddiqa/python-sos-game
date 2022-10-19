from random import random
import random
import time
from tkinter import *
from tkinter import messagebox

type = "n"
class App:
    def __init__(self):
        self.ai_dec_val = 0
        self.r = 0
        self.c = 0
        self.val = 0
        self.user_point = 0
        self.ai_point = 0
        self.original_board = [
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
                              ]
        self.temp_board   =  [
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
                            ]
        self.b=[[None for x in range(10)] for x in range(10)]
        root = Tk()
        root.title("SOS BOARD")

        btns = Button(root, text="S", font=("Helvetica", 20), height=1, width=2, bg="#0059b3",command=lambda: self.b_click(btns, "ss"))
        btno = Button(root, text="O", font=("Helvetica", 20), height=1, width=2, bg="#0059b3",command=lambda: self.b_click(btno, "oo"))

        self.label_user=Label(root,text="USER  POINTS:",bg="#6FC9E7")
        self.label_ai=Label(root,text="AGENT POINTS:",bg="#FECCAB")

        self.b_score_ai =Label(root,text="0",bg="#FECCAB")
        self.b_score_user=Label(root,text="0",bg="#6FC9E7")



        self.b[0][0] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[0][0], "00"))
        self.b[0][1] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[0][1], "01"))
        self.b[0][2] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[0][2], "02"))
        self.b[0][3] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[0][3], "03"))
        self.b[0][4] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[0][4], "04"))
        self.b[0][5] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[0][5], "05"))
        self.b[0][6] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[0][6], "06"))
        self.b[0][7] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[0][7], "07"))
        self.b[0][8] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[0][8], "08"))
        self.b[0][9] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[0][9], "09"))

        self.b[1][0] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[1][0],"10"))
        self.b[1][1] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[1][1],"11"))
        self.b[1][2] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[1][2],"12"))
        self.b[1][3] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[1][3],"13"))
        self.b[1][4] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[1][4],"14"))
        self.b[1][5] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[1][5],"15"))
        self.b[1][6] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[1][6],"16"))
        self.b[1][7] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[1][7],"17"))
        self.b[1][8] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[1][8],"18"))
        self.b[1][9] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[1][9],"19"))

        self.b[2][0] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[2][0],"20"))
        self.b[2][1] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[2][1],"21"))
        self.b[2][2] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[2][2],"22"))
        self.b[2][3] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[2][3],"23"))
        self.b[2][4] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[2][4],"24"))
        self.b[2][5] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[2][5],"25"))
        self.b[2][6] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[2][6],"26"))
        self.b[2][7] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[2][7],"27"))
        self.b[2][8] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[2][8],"28"))
        self.b[2][9] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[2][9],"29"))

        self.b[3][0] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[3][0],"30"))
        self.b[3][1] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[3][1],"31"))
        self.b[3][2] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[3][2],"32"))
        self.b[3][3] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[3][3],"33"))
        self.b[3][4] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[3][4],"34"))
        self.b[3][5] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[3][5],"35"))
        self.b[3][6] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[3][6],"36"))
        self.b[3][7] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[3][7],"37"))
        self.b[3][8] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[3][8],"38"))
        self.b[3][9] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[3][9],"39"))

        self.b[4][0] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[4][0],"40"))
        self.b[4][1] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[4][1],"41"))
        self.b[4][2] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[4][2],"42"))
        self.b[4][3] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[4][3],"43"))
        self.b[4][4] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[4][4],"44"))
        self.b[4][5] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[4][5],"45"))
        self.b[4][6] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[4][6],"46"))
        self.b[4][7] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[4][7],"47"))
        self.b[4][8] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[4][8],"48"))
        self.b[4][9] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[4][9],"49"))

        self.b[5][0] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[5][0],"50"))
        self.b[5][1] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[5][1],"51"))
        self.b[5][2] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[5][2],"52"))
        self.b[5][3] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[5][3],"53"))
        self.b[5][4] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[5][4],"54"))
        self.b[5][5] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[5][5],"55"))
        self.b[5][6] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[5][6],"56"))
        self.b[5][7] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[5][7],"57"))
        self.b[5][8] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[5][8],"58"))
        self.b[5][9] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[5][9],"59"))

        self.b[6][0] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[6][0],"60"))
        self.b[6][1] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[6][1],"61"))
        self.b[6][2] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[6][2],"62"))
        self.b[6][3] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[6][3],"63"))
        self.b[6][4] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[6][4],"64"))
        self.b[6][5] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[6][5],"65"))
        self.b[6][6] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[6][6],"66"))
        self.b[6][7] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[6][7],"67"))
        self.b[6][8] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[6][8],"68"))
        self.b[6][9] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[6][9],"69"))

        self.b[7][0] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[7][0],"70"))
        self.b[7][1] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[7][1],"71"))
        self.b[7][2] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[7][2],"72"))
        self.b[7][3] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[7][3],"73"))
        self.b[7][4] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[7][4],"74"))
        self.b[7][5] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[7][5],"75"))
        self.b[7][6] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[7][6],"76"))
        self.b[7][7] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[7][7],"77"))
        self.b[7][8] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[7][8],"78"))
        self.b[7][9] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[7][9],"79"))

        self.b[8][0] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[8][0],"80"))
        self.b[8][1] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[8][1],"81"))
        self.b[8][2] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[8][2],"82"))
        self.b[8][3] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[8][3],"83"))
        self.b[8][4] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[8][4],"84"))
        self.b[8][5] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[8][5],"85"))
        self.b[8][6] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[8][6],"86"))
        self.b[8][7] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[8][7],"87"))
        self.b[8][8] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[8][8],"88"))
        self.b[8][9] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[8][9],"89"))

        self.b[9][0] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[9][0],"90"))
        self.b[9][1] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[9][1],"91"))
        self.b[9][2] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[9][2],"92"))
        self.b[9][3] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[9][3],"93"))
        self.b[9][4] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[9][4],"94"))
        self.b[9][5] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[9][5],"95"))
        self.b[9][6] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[9][6],"96"))
        self.b[9][7] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[9][7],"97"))
        self.b[9][8] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[9][8],"98"))
        self.b[9][9] = Button(root, text=" ", font=("Helvetica", 20), height=1, width=2, bg="SystemButtonFace",command=lambda: self.b_click(self.b[9][9],"99"))

        self.b[0][0].grid(row=0, column=0)
        self.b[0][1].grid(row=0, column=1)
        self.b[0][2].grid(row=0, column=2)
        self.b[0][3].grid(row=0, column=3)
        self.b[0][4].grid(row=0, column=4)
        self.b[0][5].grid(row=0, column=5)
        self.b[0][6].grid(row=0, column=6)
        self.b[0][7].grid(row=0, column=7)
        self.b[0][8].grid(row=0, column=8)
        self.b[0][9].grid(row=0, column=9)

        self.b[1][0].grid(row=1, column=0)
        self.b[1][1].grid(row=1, column=1)
        self.b[1][2].grid(row=1, column=2)
        self.b[1][3].grid(row=1, column=3)
        self.b[1][4].grid(row=1, column=4)
        self.b[1][5].grid(row=1, column=5)
        self.b[1][6].grid(row=1, column=6)
        self.b[1][7].grid(row=1, column=7)
        self.b[1][8].grid(row=1, column=8)
        self.b[1][9].grid(row=1, column=9)

        self.b[2][0].grid(row=2, column=0)
        self.b[2][1].grid(row=2, column=1)
        self.b[2][2].grid(row=2, column=2)
        self.b[2][3].grid(row=2, column=3)
        self.b[2][4].grid(row=2, column=4)
        self.b[2][5].grid(row=2, column=5)
        self.b[2][6].grid(row=2, column=6)
        self.b[2][7].grid(row=2, column=7)
        self.b[2][8].grid(row=2, column=8)
        self.b[2][9].grid(row=2, column=9)

        self.b[3][0].grid(row=3, column=0)
        self.b[3][1].grid(row=3, column=1)
        self.b[3][2].grid(row=3, column=2)
        self.b[3][3].grid(row=3, column=3)
        self.b[3][4].grid(row=3, column=4)
        self.b[3][5].grid(row=3, column=5)
        self.b[3][6].grid(row=3, column=6)
        self.b[3][7].grid(row=3, column=7)
        self.b[3][8].grid(row=3, column=8)
        self.b[3][9].grid(row=3, column=9)

        self.b[4][0].grid(row=4, column=0)
        self.b[4][1].grid(row=4, column=1)
        self.b[4][2].grid(row=4, column=2)
        self.b[4][3].grid(row=4, column=3)
        self.b[4][4].grid(row=4, column=4)
        self.b[4][5].grid(row=4, column=5)
        self.b[4][6].grid(row=4, column=6)
        self.b[4][7].grid(row=4, column=7)
        self.b[4][8].grid(row=4, column=8)
        self.b[4][9].grid(row=4, column=9)

        self.b[5][0].grid(row=5, column=0)
        self.b[5][1].grid(row=5, column=1)
        self.b[5][2].grid(row=5, column=2)
        self.b[5][3].grid(row=5, column=3)
        self.b[5][4].grid(row=5, column=4)
        self.b[5][5].grid(row=5, column=5)
        self.b[5][6].grid(row=5, column=6)
        self.b[5][7].grid(row=5, column=7)
        self.b[5][8].grid(row=5, column=8)
        self.b[5][9].grid(row=5, column=9)

        self.b[6][0].grid(row=6, column=0)
        self.b[6][1].grid(row=6, column=1)
        self.b[6][2].grid(row=6, column=2)
        self.b[6][3].grid(row=6, column=3)
        self.b[6][4].grid(row=6, column=4)
        self.b[6][5].grid(row=6, column=5)
        self.b[6][6].grid(row=6, column=6)
        self.b[6][7].grid(row=6, column=7)
        self.b[6][8].grid(row=6, column=8)
        self.b[6][9].grid(row=6, column=9)

        self.b[7][0].grid(row=7, column=0)
        self.b[7][1].grid(row=7, column=1)
        self.b[7][2].grid(row=7, column=2)
        self.b[7][3].grid(row=7, column=3)
        self.b[7][4].grid(row=7, column=4)
        self.b[7][5].grid(row=7, column=5)
        self.b[7][6].grid(row=7, column=6)
        self.b[7][7].grid(row=7, column=7)
        self.b[7][8].grid(row=7, column=8)
        self.b[7][9].grid(row=7, column=9)

        self.b[8][0].grid(row=8, column=0)
        self.b[8][1].grid(row=8, column=1)
        self.b[8][2].grid(row=8, column=2)
        self.b[8][3].grid(row=8, column=3)
        self.b[8][4].grid(row=8, column=4)
        self.b[8][5].grid(row=8, column=5)
        self.b[8][6].grid(row=8, column=6)
        self.b[8][7].grid(row=8, column=7)
        self.b[8][8].grid(row=8, column=8)
        self.b[8][9].grid(row=8, column=9)

        self.b[9][0].grid(row=9, column=0)
        self.b[9][1].grid(row=9, column=1)
        self.b[9][2].grid(row=9, column=2)
        self.b[9][3].grid(row=9, column=3)
        self.b[9][4].grid(row=9, column=4)
        self.b[9][5].grid(row=9, column=5)
        self.b[9][6].grid(row=9, column=6)
        self.b[9][7].grid(row=9, column=7)
        self.b[9][8].grid(row=9, column=8)
        self.b[9][9].grid(row=9, column=9)

        btns.grid(row=1, column=10)
        btno.grid(row=1, column=12)

        self.label_ai.grid(row=2, column=10)
        self.b_score_ai.grid(row=2,column=11)

        self.label_user.grid(row=3,column=10)
        self.b_score_user.grid(row=3,column=11)



        root.mainloop()

    #function call at user take action as his moves or click any cell of board
    def b_click(self,b, index):
        global type
        if b["text"] == "S":
            type = "s"
            return
        if b["text"] == "O":
            type = "o"
            return

        if type == "n":
            messagebox.showerror("SOS BOARD", "Please choose a move")
        else:
            if b["text"]==" ":
                b["text"] = type
                b["bg"] = "#6FC9E7"
                self.user1(int(index[0]),int(index[1]),type)
                self.b_score_user["text"]=self.user_point
                self.check_winner()
                type = "n"
            else:
                messagebox.showerror("SOS BOARD", "Please choose a correct move its already occupied")

    #changing in board by user
    def user1(self,row,col,val):
        temp=self.user_point
        if val == 'S' or val == 's':
            val = 1
        elif val == 'O' or val == 'o':
            val = 0

        self.original_board[row][col] = val
        self.temp_board[row][col] = val

        print()
        print("after user move board is:")
        self.display_board(self.original_board)
        self.user_point = self.point(row, col, self.user_point, self.original_board)
        print("user current points:" + str(self.user_point))
        print()
        if temp==self.user_point:
            self.play1()

    #ai starts its play
    def play1(self):
            temp1=self.ai_point
            if self.isspace():
                self.ai1()
                self.b_score_ai["text"]=self.ai_point
                self.check_winner()

            while temp1<self.ai_point and self.isspace():
                temp1 = self.ai_point
                self.ai1()
                self.b_score_ai["text"]=self.ai_point
                self.check_winner()

            self.temp_board=self.original_board.copy()


    def ai1(self):
        self.greed_algo()
        if self.ai_dec_val <= 0:
            c = 0
            self.val = random.randint(0, 1)
            self.r = random.randint(0, len(self.original_board) - 1)
            self.c = random.randint(0, len(self.original_board) - 1)
            while self.original_board[self.r][self.c] != 2:
                self.val = random.randint(0, 1)
                self.r = random.randint(0, len(self.original_board) - 1)
                self.c = random.randint(0, len(self.original_board) - 1)

            self.temp_board[self.r][self.c] = self.val
            while self.ai_move(self.r, self.c, self.val):
                self.val = random.randint(0, 1)
                self.r = random.randint(0, len(self.original_board) - 1)
                self.c = random.randint(0, len(self.original_board) - 1)
                while self.original_board[self.r][self.c] != 2:
                    self.val = random.randint(0, 1)
                    self.r = random.randint(0, len(self.original_board) - 1)
                    self.c = random.randint(0, len(self.original_board) - 1)
                self.temp_board[self.r][self.c] = self.val
                c = c + 1
                if c == 10:
                    break

            self.original_board[self.r][self.c] = self.val
            self.insert_at_design(self.r,self.c,self.val)
            self.temp_board = self.original_board.copy()
            self.ai_point = self.point(self.r, self.c, self.ai_point, self.original_board)

        elif self.ai_dec_val > 0:
            self.original_board[self.r][self.c] = self.val
            self.insert_at_design(self.r,self.c,self.val)
            self.temp_board = self.original_board.copy()
            self.ai_point = self.point(self.r, self.c, self.ai_point, self.original_board)

        print("after ai move:")
        self.display_board(self.original_board)
        print("ai current points:" + str(self.ai_point))
        print()
        print()

    def insert_at_design(self,r,c,v):
        if v == 1:
            self.b[self.r][self.c]["text"]="s"
            self.b[self.r][self.c]["bg"]="#FECCAB"
        if v == 0:
            self.b[self.r][self.c]["text"]="o"
            self.b[self.r][self.c]["bg"] = "#FECCAB"

    def isspace(self):
        for i in range(len(self.original_board)):
            for j in range(len(self.original_board)):
                if self.original_board[i][j] == 2:
                    return 1
        return 0

    # displaying the board on consol
    def display_board(self, board):
        print("--------------------------------------")
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 2:
                    if board[i][j]==1:
                        print("S", end=" ")
                    else:
                        print("O", end=" ")
                else:
                    print("-", end=" ")
            print()
        print("------------------------------------------")


    # incrementing the points
    def point(self, posi, posj, point, board):
        if board[posi][posj] == 0:
            if posj - 1 >= 0 and posj + 1 <= len(board) - 1:
                if board[posi][posj - 1] == 1 and board[posi][posj + 1] == 1:
                    point += 1

            if posi - 1 >= 0 and posi + 1 <= len(board) - 1:
                if board[posi - 1][posj] == 1 and board[posi + 1][posj] == 1:
                    point += 1

            if posi - 1 >= 0 and posj + 1 <= len(board) - 1 and posi + 1 <= len(board) - 1 and posj - 1 >= 0:
                if board[posi - 1][posj + 1] == 1 and board[posi + 1][posj - 1] == 1:
                    point += 1

            if posi - 1 >= 0 and posj - 1 >= 0 and posi + 1 <= len(board) - 1 and posj + 1 <= len(board) - 1:
                if board[posi - 1][posj - 1] == 1 and board[posi + 1][posj + 1] == 1:
                    point += 1

        if board[posi][posj] == 1:
            if posj + 1 <= len(board) - 1 and posj + 2 <= len(board) - 1:
                if board[posi][posj + 1] == 0 and board[posi][posj + 2] == 1:
                    point += 1

            if posj - 1 >= 0 and posj - 2 >= 0:
                if board[posi][posj - 1] == 0 and board[posi][posj - 2] == 1:
                    point += 1

            if posi + 1 <= len(board) - 1 and posi + 2 <= len(board) - 1:
                if board[posi + 1][posj] == 0 and board[posi + 2][posj] == 1:
                    point += 1

            if posi - 1 >= 0 and posi - 2 >= 0:
                if board[posi - 1][posj] == 0 and board[posi - 2][posj] == 1:
                    point += 1

            if posi + 1 <= len(board) - 1 and posj + 1 <= len(board) - 1 and posi + 2 <= len(
                    board) - 1 and posj + 2 <= len(
                    board) - 1:
                if board[posi + 1][posj + 1] == 0 and board[posi + 2][posj + 2] == 1:
                    point += 1

            if posi - 1 >= 0 and posj - 1 >= 0 and posi - 2 >= 0 and posj - 2 >= 0:
                if board[posi - 1][posj - 1] == 0 and board[posi - 2][posj - 2] == 1:
                    point += 1

            if posi - 1 >= 0 and posj + 1 <= len(board) - 1 and posi - 2 >= 0 and posj + 2 <= len(board) - 1:
                if board[posi - 1][posj + 1] == 0 and board[posi - 2][posj + 2] == 1:
                    point += 1

            if posi + 1 <= len(board) - 1 and posj - 1 >= 0  and posi + 2 <= len(board) - 1 and posj - 2 >= 0:
                if board[posi + 1][posj - 1] == 0 and board[posi + 2][posj - 2] == 1:
                    point += 1
        return point


    #check if user has a point after ai or not
    def ai_move(self,row,col,val):
        bad=0
        for i in range(len(self.temp_board)):
            for j in range(len(self.temp_board)):
                if self.temp_board[i][j] == 2:
                    if self.max0(i, j) != 0:
                        bad=1
                    if self.max1(i, j)!=0:
                        bad=1

                    self.temp_board[i][j]=2
        self.temp_board[row][col] = 2
        return bad


    # greed_algo
    def greed_algo(self):
        temp=0
        self.ai_dec_val=0
        for i in range(len(self.temp_board)):
            for j in range(len(self.temp_board)):
                if self.temp_board[i][j] == 2:
                    if self.max0(i, j) > self.max1(i, j):
                        if temp < self.max0(i, j):
                            temp = self.max0(i, j)
                            self.temp_board[i][j]=2
                            self.val = 0
                            self.r = i
                            self.c = j
                            self.ai_dec_val=1
                    elif self.max0(i, j) <= self.max1(i, j):
                        if temp < self.max1(i, j):
                            temp = self.max1(i, j)
                            self.temp_board[i][j] = 2
                            self.val = 1
                            self.r = i
                            self.c = j
                            self.ai_dec_val = 1
                    self.temp_board[i][j]=2


    def max0(self, posi, posj):
        self.temp_board[posi][posj] = 0
        pre_ai_point = self.ai_point
        new_ai_point = self.point(posi, posj, self.ai_point, self.temp_board)
        if pre_ai_point < new_ai_point:
            temp_dec_val = new_ai_point-pre_ai_point
        else:
            temp_dec_val = 0
        return temp_dec_val

    def max1(self, posi, posj):
        self.temp_board[posi][posj] = 1
        pre_ai_point = self.ai_point
        new_ai_point = self.point(posi, posj, self.ai_point, self.temp_board)

        if pre_ai_point < new_ai_point:
            temp_dec_val = new_ai_point-pre_ai_point
        else:
            temp_dec_val = 0
        return temp_dec_val

    def check_winner(self):
      if self.isspace()==0:
        print()
        print("user  point  : "+str(self.user_point))
        print("Agent point  : "+str(self.ai_point))
        print()
        if self.ai_point>self.user_point:
            print("winner is AGENT")
            messagebox.showerror("SOS BOARD", "AGENT is a winner with maximum point :"+str(self.ai_point))
            exit()
        elif self.ai_point<self.user_point:
            print("Congratulation, you are the winner")
            messagebox.showerror("SOS BOARD", "Congratulations, You are the winner with maximum point :"+str(self.user_point))
            exit()
        else:
            print("Tie")
            messagebox.showerror("SOS BOARD", "Its a TIE between you and agent with a point :"+str(self.user_point))
            exit()