# coding:utf-8;

import time
import _thread


# 协程写法实现原理

gen = None # 全局生成器，供long_io使用

def gen_coroutine(fun):
    def wrapper(*args, **kwargs):
        global gen
        gen = fun()
        gen.__next__()  # 开启生成器req_a的执行
    return wrapper


def long_io( ):
    """模拟耗时IO操作"""
    def fun():
        print( "开始执行IO操作")
        global gen
        time.sleep(5)
        try:
            print( "完成IO操作，并send结果唤醒挂起程序继续执行")
            gen.send("io result")  # 使用send返回结果并唤醒程序继续执行
        except StopIteration: # 捕获生成器完成迭代，防止程序退出
            pass
    _thread.start_new_thread(fun, ())


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