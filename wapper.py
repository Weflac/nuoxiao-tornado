# coding:utf-8;

from time import ctime, sleep

# 装饰器
def w1(func):
    def inner():
        # 验证1
        # 验证2
        print("---正在验证权限----")
        func()
    return inner

# f1 = w1(f1)(装饰器原理) 等价于@w1
@w1
def f1():
    print('test wapper 1')

@w1
def f2():
    print('test wapper 2')

@w1
def f3():
    print('test wapper 3')

@w1
def f4():
    print('test wapper 4')



# f1()

#定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        print("- - -1- - -")
        return "<b>" + fn() + "</b>"
    return wrapped

#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        print("- - -2- - -")
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

@makeBold
@makeItalic
def test3():
    print("- - -3- - -")
    return "hello world-3"

# print(test1())
# print(test2())
# print(test3())

def timefun(func):
    def wrappedfunc():
        print("%s called at %s"%(func.__name__, ctime()))
        f = func()
        return f
    return wrappedfunc

@timefun
def foo():
    print("I am foo")

@timefun
def getInfo():
    return '----hahah---'

# foo()
# sleep(2)
# foo()
#
# print(getInfo())

# 装饰器带参数,在原有装饰器的基础上，设置外部变量
def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            if pre == 'python':
                print(pre)
            print("%s called at %s %s"%(func.__name__, ctime(), pre))
            return func()
        return wrappedfunc
    return timefun

@timefun_arg("itcast")
def foo():
    print("I am foo")

@timefun_arg("python")
def too():
    print("I am too")

# foo()
# sleep(2)
# too()


#定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        print("----1---")
        return "<b>" + fn() + "</b>"
    return wrapped

#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        print("----2---")
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
@makeItalic
def test3():
    print("----3---")
    return "hello world-3"

# ret = test3()
# print(ret)

# 通用装饰器
def func(functionName):
    def func_in(*args, **kwargs):
        print("-----记录日志-----")
        ret = functionName(*args, **kwargs)
        return ret

    return func_in

@func
def test():
    print("----test----")
    return "haha"

@func
def test2():
    print("----test2---")

@func
def test3(a):
    print("-----test3--a=%d--"%a)

ret = test()
print("test return value is %s"%ret)

a = test2()
print("test2 return value is %s"%a)


test3(11)
