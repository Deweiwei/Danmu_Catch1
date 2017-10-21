import numpy as np
import pylab as pl
def gethead(msg):
    pos=msg.index(" ")
    return msg[0:pos]

def gettail(msg):
    pos=msg.index(" ")
    return msg[pos+1:-1]

ftm_x=[]
ftm_y=[]
f = open("ftm_result.txt","r")
i=f.readline()
while i:
    ftm_x.append(int(gethead(i)))
    ftm_y.append(int(gettail(i)))
    print (ftm_x)
    print (ftm_y)
    i = f.readline()
f.close()
#print(ftm[0:40][2][1])
mn_x=[]
mn_y=[]
f = open("mn_result.txt","r")
i=f.readline()
while i:
    mn_x.append(int(gethead(i)))
    mn_y.append(int(gettail(i)))
    i = f.readline()
f.close()

mk_x=[]
mk_y=[]
f = open("mk_result.txt","r")
i=f.readline()
while i:
    mk_x.append(int(gethead(i)))
    mk_y.append(int(gettail(i)))
    i = f.readline()
f.close()

qxj_x=[]
qxj_y=[]
f = open("qxj_result.txt","r")
i=f.readline()
while i:
    qxj_x.append(int(gethead(i)))
    qxj_y.append(int(gettail(i)))
    i = f.readline()
f.close()

plotlist=[]
#plotlist.append(pl.plot(range(0, 40),mn[0:40]))

#pl.ylim(0,1000)
pl.plot(mn_x,mn_y,label=u'y=x^3曲线图')
pl.plot(mk_x,mk_y)
pl.plot(qxj_x,qxj_y)
pl.plot(ftm_x,ftm_y)
pl.show()
