"""
    出现bug：1.整个程序因为一个bug停止运行
            2.对bug进行提醒，整个程序继续运行
    语法： try：
                可能发生错误的代码
        except：
                如果出现异常执行的代码
"""
# 基本捕获语法
try:
    open('E:/project/abcd.txt', 'r', encoding='utf-8')
except IndentationError:
    print("出现异常，我将模式换位 w 模式打开")
    f = open('E:/project/abcd.txt', 'w', encoding='utf-8')

# 捕获
# 通过将异常信息赋值给as，保存异常信息
try:
    print(name)
    # 1 / 0
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常，将要捕获的异常类型的名字放到except后,并使用元组的方式进行书写
try:
    print(k)
except (NameError, ZeroDivisionError) as e:
    print("ZeroDivisionError错误")
    print(e)

# 捕获所有异常
try:
    1 / 0
except Exception as e:
    print(e)

# 异常的else 表示如果没有异常要执行的代码 【可选】 except Exception能捕获全部异常
try:
    f = open('E:/project/abc.txt', 'r', encoding='utf-8')
except Exception as e:
    print(e)
else:
    print("good good good ")

# finally 表示无论是否异常都要执行的代码 例如，关闭文件
try:
    f = open('E:/project/abc.txt', 'r', encoding='utf-8')
except FileNotFoundError as e:
    f = open('E:/project/abc.txt', 'w', encoding='utf-8')
    print(e)
else:
    print("这次没有异常")
finally:
    print("hello finally")
    f.close()
