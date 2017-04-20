from threading import Thread as thread
from threading import Lock
import time,random  
dish = 0 #需要放在安全区的变量
lock = Lock()
def producerFunction() :
    '''如果投的筛子比0.2大，则向盘子中增加一个苹果'''
    global lock, dish
    while True:
        if ( random.random() > 0.1 ):
            lock.acquire() # 从这里进入线程安全区
            if dish < 100:
                dish += 1
                msg = '生产者增加了一个苹果，现在有 %d 个苹果' % (dish)
                print ( msg.decode ('utf-8') )
            lock.release() # 从这里离开线程安全区
        time.sleep (random.random()*3)

def consumerFunction() :
    '''如果投的筛子比0.5大，则从盘子中取一个苹果'''  
    global lock, dish  
    while True:  
        if ( random.random() > 0.9 ):
            lock.acquire() # 从这里进入线程安全区
            if dish > 0:
                dish -= 1
                msg = '消费者拿走一个苹果现，在有%d个苹果' % (dish)
                print (msg.decode('utf-8'))
            lock.release() # 从这里离开线程安全区
            time.sleep (random.random()*3)  
  
def begin_test_lock():
    ident1 = thread.start_new_thread ( producerFunction, () )
    ident2 = thread.start_new_thread ( consumerFunction, () )
    time.sleep(60)
def main ():
    begin_test_lock ()
if __name__ == '__main__' :
    main ()