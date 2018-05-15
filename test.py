# coding:utf-8;

import time
import _thread

def long_io(callback):
    """模拟耗时IO操作"""
    def fun(cb):
        print("开始执行IO操作")
        time.sleep(5)
        print("完成IO操作")
        cb("io result")  # 执行回调函数

    _thread.start_new_thread(fun, (callback,))  # 开启线程执行耗时操作


def on_finish(ret):
    """回调函数"""
    print ("开始执行回调函数on_finish")
    print ("ret: %s" % ret)
    print ("完成执行回调函数on_finish")

def req_a():
    """模拟请求a"""
    print('开始处理请求req_a')
    long_io(on_finish)
    print( '完成处理请求req_a')

def req_b():
    """模拟请求b"""
    print ('开始处理请求req_b')
    print( '完成处理请求req_b')

def main():
    """模拟tornado框架，处理两个请求"""
    req_a()
    req_b()
    while 1:  # 添加此句防止程序退出，保证线程可以执行完
        pass

if __name__ == "__main__":
    main()