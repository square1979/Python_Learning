"""
    需求：计算每日的销售额
    1.设计一个类，可以完成数据的封装
    2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
        由于两个文件的格式不同，逻辑不同，所以构建一个抽象类，通过具体的子类实现具体数据的具体读取方法
    3.读取文件，生产数据对象
    4.进行数据需求的逻辑计算（计算每一天的销售额）
    5.pyecharts进行图形绘制
"""
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import *

from data_define import Record
from file_define import FileReader, TextFileReader, JsonFileReader

textFileReader = TextFileReader("2011年1月销售数据.txt")
jsonFileReader = JsonFileReader("2011年2月销售数据JSON.txt")

jan_data: list[Record] = textFileReader.read_data()
feb_data: list[Record] = jsonFileReader.read_data()

# 将两个月份的数据合并成一个list来存储
all_data: list[Record] = jan_data + feb_data

# 进行数据计算
# {"2011-01-01": 1234,"2011-01-02": 2234,"2011-01-03": 3234}
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 有记录所以做累加即可
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.DARK))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render()
