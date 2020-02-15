from brial import *
import copy
import pdb
import xdrlib ,sys
import random
import time
import math


Keccak=declare_ring([Block('v',1472),Block('k',128)],globals())

dd=8

def theta(state):
        tempstate=[[] for i in range(25)]
        for i in range(25):
                for j in range(dd):
                        tempstate[i].append(state[i][j])
                        for k in range(5):
                                tempstate[i][j]+=state[(i%5+5-1)%5+5*k][j]+state[(i%5+1+5)%5+5*k][(j-1+8)%dd]

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
#ketje padding
state=[[] for i in range(25)]

for i in range(25):
        for j in range(dd):
                state[i].append(Keccak(0))
keylane=[6,12,18,24,3,9,10,16,22,1,7,13]
for i in range(len(keylane)):
        for j in range(dd):
                state[keylane[i]][j]=k(i*8+j)# key padding
#padding
tianchong1=[0,1,0,0,1,0,0,0]
tianchong2=[1,0,0,0,0,0,0,0]
tianchong3=[1,1]

for i in range(8):
        state[0][i]=tianchong1[i]
for i in range(8):
        state[19][i]=tianchong2[i]
for i in range(2):
        state[21][i+6]=tianchong3[i]

#16 cube
for i in range(6):
        state[5][i]=v(2*i)
        state[15][i]=v(2*i+1)
        state[20][i]=v(2*i)+v(2*i+1)
for i in range(2):
        state[15][6+i]=v(12+i)
        state[20][6+i]=v(12+i)

state[11][0]=v(14)
state[4][7]=v(15)


#26 auxiliary variables

state[15][0]=k(48)+v(1)
state[15][2]=k(50)+v(5)
state[15][5]=k(53)+v(11)
state[20][1]=k(49)+v(2)+v(3)
state[20][3]=k(51)+v(6)+v(7)
state[20][4]=k(52)+v(8)+v(9)


for i in range(2):
        state[20][6+i]=k(54+i)+v(12+i)

state[11][0]=k(0)+k(56)+k(72)+v(14)

for i in range(4):
        state[2][2+i]=k(10+i)+k(66+i)+k(82+i)

for i in range(2):
        state[17][i]=k(8+i)+k(64+i)+k(80+i)
for i in range(2):
        state[17][6+i]=k(14+i)+k(70+i)+k(86+i)

for i in range(2):
        state[8][2+i]=k(18+i)+k(34+i)+k(90+i)

for i in range(2):
        state[8][6+i]=k(22+i)+k(38+i)+k(94+i)
state[23][0]=k(16)+k(32)+k(88)

for i in range(2):
        state[23][4+i]=k(20+i)+k(36+i)+k(92+i)


state[4][7]=k(31)+k(47)+v(15)
state[14][1]=k(25)+k(41)
set2=set()

aa=[0]
aa1=[]


# one round
theta(state)
rio(state)
pi(state)
chi(state)

#after one round


set1=set()
set3=set()
set4=set()

state3=[]
state2=[0]
tt=0
for i in range(25):
        for j in range(8):
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

#output the number of involved key bits and  involved key bits
print(len(set4))

cc=list(set4)
cc.sort()

for i in range(len(cc)):
        print(cc[i])     
