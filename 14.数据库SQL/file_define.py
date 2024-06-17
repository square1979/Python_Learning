# 定义一个抽象类作为顶层设计，确定有哪些功能需要实现
# 导入JSON处理的模块,为JsonFileReader类的实现提供支持。
import json
# 从另一个模块中导入Record类,这个类用于表示每条销售数据的记录
from data_define import Record


# 定义了一个抽象基类FileReader,它包含一个抽象方法read_data()。
# 这个方法的作用是读取数据并将其转换为Record对象列表
class FileReader:

    def read_data(self) -> list[Record]:
        """读取的每一条数据都转换为Record对象,将它们都封装到list内返回即可"""
        pass


# 这是FileReader抽象类的一个具体实现,用于读取文本格式的销售数据文件。
# 在__init__方法中,接受文件路径作为参数,并将其存储为成员变量self.path。
# 实现了read_data()方法,打开文件,逐行读取数据,将每行数据转换为Record对象,并将这些对象添加到一个列表中,最后返回这个列表
class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量，记录文件的路径

    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")
        record_list: list[Record] = []

        for line in f.readlines():
            line = line.strip()  # 消除读取每一行数据中的换行符
            data_list = line.split(",")
            # 创建一个Record对象
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        f.close()
        return record_list


# 这是FileReader抽象类的另一个具体实现,用于读取JSON格式的销售数据文件。
# 与TextFileReader类似,在__init__方法中接受文件路径作为参数,并将其存储为成员变量self.path。
# 实现了read_data()方法,打开文件,逐行读取数据,将每行JSON数据转换为Record对象,并将这些对象添加到一个列表中,最后返回这个列表
class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量，记录文件的路径

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"],
                            int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    # for i in list1:
    #     print(i)
    for i in list2:
        print(i)
