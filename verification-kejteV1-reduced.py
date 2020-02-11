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
#ketje padding  
state=[[] for i in range(25)]

for i in range(25):
        for j in range(dd):
                state[i].append(Keccak(0))
keylane=[1,2,3,4,5,6,7,8,9]
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
        state[10][i]=tianchong2[i]
for i in range(2):
        state[24][i+6]=tianchong3[i]

#32 cube
for i in range(8):
        state[11][i]=v(2*i)
        state[16][i]=v(2*i+1)
        state[21][i]=v(2*i)+v(2*i+1)


state[18][0]=v(16)
state[23][0]=v(16)

state[18][7]=v(17)
state[23][7]=v(17)

for i in range(6):
        state[14][i]=v(18+2*i)
        state[19][i]=v(18+2*i+1)
        state[24][i]=v(18+2*i)+v(18+2*i+1)

state[14][6]=v(30)
state[19][6]=v(30)

state[14][7]=v(31)
state[19][7]=v(31)


#29 auxiliary variables

for i in range(8):
        state[11][i]=v(2*i)+k(0+i)+k(40+i)
for i in range(3,8):
        state[12][i]=k(8+i)+k(48+i)
for i in range(8):
        state[23][i]=k(16+i)+k(56+i)

state[23][0]=v(16)+k(16)+k(56)
state[23][7]=v(17)+k(23)+k(63)

for i in range(7):
        state[14][i]=v(18+2*i)+k(24+i)+k(64+i)
state[14][7]=v(31)+k(31)+k(71)
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
cc=list(set4)
cc.sort()
for i in range(len(cc)):
        print(cc[i])
