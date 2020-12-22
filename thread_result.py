import threading
import time

"""重新定义带返回值的线程类"""
class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
"""测试函数，计算两个数之和"""
def fun():
    time.sleep(1)
    return 12

if __name__ == '__main__':
    t = MyThread(fun)
    t.start()
    t.join()
    print(t.get_result())