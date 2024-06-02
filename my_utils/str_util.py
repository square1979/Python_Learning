"""
    str_util.py(字符串相关工具，内含:)
        函数:str_reverse(s)，接受传入字符串，将字符串反转返回
        函数:substr(s，x，y)，按照下标x和y，对字符串进行切片
"""


def str_reverse(s):
    """
    功能说明:将字符串倒序输出
    :param s:输入的字符串
    :return: 倒序输出的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    功能说明：将字符串切片输出
    :param s: 输入的字符串
    :param x: 切片起始下标
    :param y: 切片终止下标
    :return: 返回切片后的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse('abandon'))
    print(substr('abandon', 1, 4))
