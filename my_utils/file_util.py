"""
    file_util.py(文件处理相关工具，内含:)
        函数:print_file_info(file name)，接收传入文件的路径，打印文件的全部内
            容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
        函数:append_to_file(file name，data)，接收文件路径以及传入数据，将数据追加写入到文件中
"""


def print_file_info(file_name):
    """
    功能说明：读取文件并给出捕获异常信息
    :param file_name: 读取文件名
    :return: 返回异常原因
    """
    f = None
    try:
        f = open(file_name, 'r', encoding='utf-8')
        f1 = f.read()
        print(f1)
    except Exception as e:
        print(e)
    finally:
        if f:  # 如果变量是none 表示false 如果有任何内容及时True
            f.close()


def append_to_file(file_name, data):
    """
    功能说明：在文件中补充内容
    :param file_name:文件名
    :param data: 补充的内容
    :return: 不返回
    """
    c = open(file_name, 'a', encoding='utf-8')
    c.write(data)
    c.close()


if __name__ == '__main__':
    append_to_file('E:/project/abcd.txt', 'remember\n')
    print_file_info('E:/project/abcd.txt')
