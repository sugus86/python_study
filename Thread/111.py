import threading
def doubler(number):
    """
    可以被线程使用的一个函数
    """
    print(threading.currentThread().getName())
    print(number * 2)
    #print()
if __name__ == '__main__':
    for i in range(5):
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()