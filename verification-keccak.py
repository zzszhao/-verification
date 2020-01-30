from brial import *
import copy
import pdb
import xdrlib ,sys
import random
import time
import math


Keccak=declare_ring([Block('v',1472),Block('k',128)],globals())

dd=64


def theta(state):
        tempstate=[[] for i in range(25)]
        for i in range(25):
                for j in range(dd):
                        tempstate[i].append(state[i][j])
                        for k in range(5):
                                tempstate[i][j]+=state[(i%5+5-1)%5+5*k][j]+state[(i%5+1+5)%5+5*k][(j-1+64)%dd]

        for i in range(25):
                for j in range(dd):
                        state[i][j]=tempstate[i][j]



def rio(state):
        rot=[0,1,62,28,27,36,44,6,55,20,3,10,43,25,39,41,45,15,21,8,18,2,61,56,14]
        tempstate=[[] for i in range(25)]
        for i in range(25):
                for j in range(dd):
                        tempstate[i].append(state[i][(j-rot[i]+dd)%dd])

        for i in range(25):
                for j in range(dd):
                        state[i][j]=tempstate[i][j]

def pi(state):
        tempstate=[[] for i in range(25)]
        for i in range(25):
             y=int(math.floor(i/5))
                x=i%5
                x1=y
                y1=(2*x+3*y)%5
                temp=5*y1+x1
                for j in range(dd):
                        tempstate[temp].append(state[i][j])
        for i in range(25):
                for j in range(dd):
                        state[i][j]=tempstate[i][j]
def chi(state):
        tempstate=[[] for i in range(25)]
        for i in range(5):
                for j in range(5):
                        for k in range(dd):
                                tempstate[5*i+j].append(state[5*i+j][k]+(state[5*i+(j+1)%5][k]+1)*state[5*i+(j+2)%5][k])

        for i in range(25):
                for j in range(dd):
                        state[i][j]=tempstate[i][j]


#keccak填充                                                                                                                                                             state=[[] for i in range(25)]

for i in range(25):
        for j in range(dd):
                state[i].append(Keccak(0))
keylane=[0,1]
for i in range(len(keylane)):
        for j in range(dd):
                state[keylane[i]][j]=k(i*64+j)#填充密钥

#64个立方变量


state[2][0]=state[7][0]=v(0)
state[2][1]=state[7][1]=v(1)
state[2][2]=state[7][2]=v(2)
state[2][4]=state[7][4]=v(3)
state[2][5]=state[7][5]=v(4)

state[2][6]=state[7][6]=v(5)
state[2][11]=state[7][11]=v(6)
state[2][14]=state[7][14]=v(7)
state[2][15]=state[7][15]=v(8)
state[2][16]=state[7][16]=v(9)

state[2][17]=state[7][17]=v(10)
state[2][18]=state[7][18]=v(11)
state[2][20]=state[7][20]=v(12)
state[2][26]=state[7][26]=v(13)
state[2][27]=state[7][27]=v(14)

state[2][28]=state[7][28]=v(15)
state[2][30]=state[7][30]=v(16)
state[2][39]=state[7][39]=v(17)
state[2][40]=state[7][40]=v(18)
state[2][42]=state[7][42]=v(19)

state[2][43]=state[7][43]=v(20)
state[2][46]=state[7][46]=v(21)
state[2][49]=state[7][49]=v(22)
state[2][52]=state[7][52]=v(23)
state[2][53]=state[7][53]=v(24)

state[2][54]=state[7][54]=v(25)
state[2][55]=state[7][55]=v(26)
state[2][56]=state[7][56]=v(27)
state[2][57]=state[7][57]=v(28)
state[2][58]=state[7][58]=v(29)

state[3][2]=state[8][2]=v(30)
state[3][4]=state[8][4]=v(31)
state[3][5]=state[8][5]=v(32)
state[3][6]=state[8][6]=v(33)
state[3][14]=state[8][14]=v(34)

state[3][16]=state[8][16]=v(35)
state[3][17]=state[8][17]=v(36)
state[3][26]=state[8][26]=v(37)
state[3][29]=state[8][29]=v(38)
state[3][30]=state[8][30]=v(39)

state[3][32]=state[8][32]=v(40)
state[3][38]=state[8][38]=v(41)
state[3][39]=state[8][39]=v(42)
state[3][40]=state[8][40]=v(43)
state[3][42]=state[8][42]=v(44)

state[3][43]=state[8][43]=v(45)
state[3][44]=state[8][44]=v(46)
state[3][52]=state[8][52]=v(47)
state[3][51]=state[8][51]=v(48)
state[3][54]=state[8][54]=v(49)

state[3][55]=state[8][55]=v(50)
state[3][58]=state[8][58]=v(51)

state[4][15]=v(52)
state[4][16]=v(53)
state[4][28]=v(54)
state[4][31]=v(55)
state[4][41]=v(56)

state[4][54]=v(57)
state[6][4]=v(58)
state[6][15]=v(59)
state[6][17]=v(60)
state[6][30]=v(61)
state[6][43]=v(62)
state[6][53]=v(63)


#44个辅助变量
state[5][0]=k(0)
state[5][1]=k(1)
state[5][2]=k(2)
state[5][3]=k(3)
state[5][5]=k(5)

state[5][9]=k(9)
state[5][11]=k(11)
state[5][12]=k(12)
state[5][13]=k(13)
state[5][14]=k(14)

state[5][16]=k(16)
state[5][17]=k(17)
state[5][20]=k(20)
state[5][21]=k(21)
state[5][24]=k(24)

state[5][25]=k(25)
state[5][26]=k(26)
state[5][27]=k(27)
state[5][29]=k(29)
state[5][31]=k(31)

state[5][35]=k(35)
state[5][36]=k(36)
state[5][37]=k(37)
state[5][38]=k(38)
state[5][39]=k(39)

state[5][40]=k(40)
state[5][41]=k(41)
state[5][42]=k(42)
state[5][44]=k(44)
state[5][46]=k(46)

state[5][47]=k(47)
state[5][49]=k(49)
state[5][50]=k(50)
state[5][51]=k(51)
state[5][52]=k(52)

state[5][53]=k(53)
state[5][54]=k(54)
state[5][55]=k(55)
state[5][57]=k(57)
state[5][58]=k(58)

state[5][60]=k(60)
state[5][62]=k(62)
state[5][63]=k(63)

state[6][18]=k(82)





set2=set()





aa=[0]
aa1=[]


#一轮
theta(state)
rio(state)
pi(state)
chi(state)

#看一轮之后，与立方变量相乘的密钥比特
set1=set()
set3=set()
set4=set()

state3=[]
state2=[0]
tt=0
for i in range(25):
        for j in range(64):
                state2[0]=(state[i][j].monomials())
        #       print state2[0]
        #       print(time.ctime())
                for h in range(64):
#                       print m
                        bb=[]
                        cc=''
                        dd=''
                        for m in state2[0]:
                                if(str(m/Keccak(v(h))).count('v')==1):
                                        print('error')
                                if(((m/Keccak(v(h)))!=0) and ((m/Keccak(v(h)))!=1) and str(m/Keccak(v(h))).count('v')==0):
                                        bb.append(m/Keccak(v(h)))
                        if len(bb)!=0:
                                cc=str(bb[0])
                                for n in range(1,len(bb)):
                                        cc=cc+'+'+str(bb[n])
                                set4.add(cc)

#输出依然相关密钥比特的个数和值
print(len(set4))
cc=list(set4)

cc.sort()
for i in range(len(cc)):
        print(cc[i])
