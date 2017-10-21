import time, sys

from danmu import DanMuClient

def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
        decode(sys.stdin.encoding))
    f = open("S7比赛1021.txt", 'a')
    f.write(msg+'\n')
    f.close()
dmc = DanMuClient('http://www.douyu.com/288016')
if not dmc.isValid(): print('Url not valid')

@dmc.danmu
def danmu_fn(msg):
    pp('%s:  [%s] %s ' % (time.ctime(time.time()),msg['NickName'], msg['Content']))
#@dmc.gift
#def gift_fn(msg):
    #pp('[%s] sent a gift!' % msg['NickName'])

@dmc.other
def other_fn(msg):
    pp('Other message received')



dmc.start(blockThread = True)
