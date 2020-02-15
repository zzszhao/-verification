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
keylane=[6,12,18,24,3,9,10,16,22,1]
for i in range(len(keylane)):
        for j in range(dd):
                state[keylane[i]][j]=k(i*8+j)# padding key
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

#32 cube
for i in range(8):
        state[5][i]=v(2*i)
        state[15][i]=v(2*i+1)
        state[20][i]=v(2*i)+v(2*i+1)

        state[8][i]=v(2*i+16)
        state[13][i]=v(2*i+17)
        state[23][i]=v(2*i+16)+v(2*i+17)


#22 auxiliary variables
state[5][1]=k(49)+v(2)
state[5][3]=k(51)+v(6)
state[5][6]=k(54)+v(12)

state[20][0]=k(48)+v(0)+v(1)
state[20][4]=k(52)+v(8)+v(9)
state[20][5]=k(53)+v(10)+v(11)

state[15][2]=k(50)+v(5)
state[15][7]=k(55)+v(15)


for i in range(3):
        state[11][i]=k(0+i)+k(56+i)+k(72+i)

for i in range(2):
        state[11][6+i]=k(6+i)+k(62+i)+k(78+i)
state[21][4]=k(4)+k(60)+k(76)
state[8][0]=k(16)+k(32)+v(16)
state[8][4]=k(20)+k(36)+v(24)
state[8][7]=k(23)+k(39)+v(30)


state[13][1]=k(17)+k(33)+v(19)
state[13][2]=k(18)+k(34)+v(21)

state[13][5]=k(21)+k(37)+v(27)
state[23][3]=k(19)+k(35)+v(22)+v(23)
state[17][5]=k(13)+k(69)




set2=set()

aa=[0]
aa1=[]


#one round
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

#output and compute
print(len(set4))

for bbb in set4:
        print(bbb)
