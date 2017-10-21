def gettime(msg):
    return msg[14:16]

time=0
count = 1
temp=0
f = open("钱小佳2.txt", 'r')
i=f.readline()
t = open("tempword.txt", 'w')
t.close()
while i:
    if i != 'Other message received\n':
        t = open("tempword.txt", 'a')
        t.write(i)
        print(i)
        t.close()
    i = f.readline()
f.close()

t = open("qxj_result.txt", 'w')
t.close()
f = open("tempword.txt",'r')
i=f.readline()
while i:
    temp=gettime(i)
    i = f.readline()
    if gettime(i)==temp:
        count+=1
    else:
        t = open("qxj_result.txt", 'a')
        t.write(str(time) +" "+ str(count)+'\n')
        t.close()
        time+=1
        count=1
    print (i)