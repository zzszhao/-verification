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
#ketje 填充
state=[[] for i in range(25)]

for i in range(25):
        for j in range(dd):
                state[i].append(Keccak(0))
keylane=[6,12,18,24,3,9,10,16,22,1]
for i in range(len(keylane)):
        for j in range(dd):
                state[keylane[i]][j]=k(i*8+j)#填充密钥
#填充比特
tianchong1=[0,1,0,0,1,0,0,0]
tianchong2=[1,0,0,0,0,0,0,0]
tianchong3=[1,1]

for i in range(8):
        state[0][i]=tianchong1[i]
for i in range(8):
        state[19][i]=tianchong2[i]
for i in range(2):
        state[21][i+6]=tianchong3[i]

#32个立方变量
for i in range(8):
        state[5][i]=v(2*i)
        state[15][i]=v(2*i+1)
        state[20][i]=v(2*i)+v(2*i+1)

        state[8][i]=v(2*i+16)
        state[13][i]=v(2*i+17)
        state[23][i]=v(2*i+16)+v(2*i+17)


#14个辅助变量
for i in range(8):
        state[4][i]=state[14][i]=state[19][i]=k(32+i)+k(16+i)+k(47+i)

state[4][0]=k(32)+k(16)+k(55)
state[14][0]=k(32)+k(16)+k(55)
state[19][0]=k(32)+k(16)+k(55)

for i in range(6):
        state[11][i]=k(48+i)+k(7+i)+k(63+i)
        state[21][i]=k(48+i)+k(7+i)+k(63+i)
state[11][0]=k(48)+k(15)+k(71)
state[21][0]=k(48)+k(15)+k(71)

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

#输出依然相关密钥比特数量和值
print(len(set4))

for bbb in set4:
        print(bbb)
