# coding:utf-8;

import time
import _thread


# 协程写法实现原理

def gen_coroutine(f):
    def wrapper(*args, **kwargs):
        gen_f = f() # gen_f为生成器req_a
        r = gen_f.__next__()  # r为生成器long_io
        print("r为生成器long_io")
        def fun(g):
            ret = g.__next__()  # 执行生成器long_io
            try:
                print("将结果返回给req_a并使其继续执行")
                gen_f.send(ret)  # 将结果返回给req_a并使其继续执行
            except StopIteration:
                pass
        _thread.start_new_thread(fun, (r,)) # 相当于tornado.ioloop.IOLoop
    return wrapper


def long_io( ):
    print ("开始执行IO操作")
    time.sleep(5)
    print ("完成IO操作，yield回操作结果")
    yield "io result"


@gen_coroutine
def req_a():
    """模拟请求a"""
    print('开始处理请求req_a')
    ret = yield long_io()
    print("ret: %s" % ret)
    print( '完成处理请求req_a')

def req_b():
    """模拟请求b"""
    print ('开始处理请求req_b')
    time.sleep(2)
    print( '完成处理请求req_b')

def main():
    """模拟tornado框架，处理两个请求"""
    req_a()
    req_b()
    while 1:  # 添加此句防止程序退出，保证线程可以执行完
        pass

if __name__ == "__main__":
    main()