# 表示函数返回了空的意思 return none = 不写return语句
# 返回值为none = false
def say():
    print("hello world")
    return None


# 不返回任何值
result = say()
print(result, type(result))


# none用于if判断
def check_age(age):
    if age > 18:
        return "success"
    else:
        return None


# 在if判断中，none等于false
num = int(input("Enter a number: "))
result = check_age(num)
if not result:
    print("未成年人禁止入内！")

# none用于声明无初始内容的变量
name = None
