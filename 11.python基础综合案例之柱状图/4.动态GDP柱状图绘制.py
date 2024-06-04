"""
    需求分析：
    1.GDP 数据处理为亿级
    2.有时间轴，按照年份为时间轴的点
    3.X轴 Y轴反转 同事每一年的数据只要前8名国家
    4.有标题，标题的年份会动态更改
    5.设置了主题为light
"""
# 1.导入软件包
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
# from pyecharts.globals import *

# 2.读取数据json转python，得出能用于画图的列表
f = open("E:/BaiduNetdiskDownload/资料/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv",
         "r", encoding="GB2312")
data_lines = f.readlines()
f.close()
# 删除第一条数据
data_lines.pop(0)

"""
    将数据转换为字典存储.格式为：{年份1：[  [国家，GDP],[国家，GDP],[国家，GDP]  ],
    年份2：[  [国家，GDP],[国家，GDP],[国家，GDP]  ] ,  年份3：[  [国家，GDP],[国家，GDP],[国家，GDP]  ] }
"""
# 先定义一个字典对象【字典内部嵌套列表】
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])

    # 如何判断字典里面是否有指定KEY
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict)
# 时间线对象
timeline = Timeline()
# timeline = Timeline({"theme": ThemeType.LIGHT})

# 3.使用Bar构建图像并排序
# 3.1先取出全部的key,再根据key排序
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)

# 3.2 因为最后结果只要GDP前八的国家，所以应在同一年中对所有国家GDP进行排序
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份里前八名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # X轴添加国家
        y_data.append(country_gdp[1] / 100000000)  # Y轴添加GDP

    # 构建柱状图,柱状图由小到大，反转后从大到小
    bar1 = Bar()
    x_data.reverse()
    y_data.reverse()
    bar1.add_xaxis(x_data)
    bar1.add_yaxis("GDP(亿)", y_data,
                   label_opts=LabelOpts(position="right"))

    # 反转X轴 Y轴
    bar1.reversal_axis()
    # 设置每一年的图表标题
    bar1.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前八国家GDP数据")
    )
    timeline.add(bar1, str(year))


timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_loop_play=True,
    is_auto_play=True
)
# 5.设置图像年份标题option
timeline.render("1960-2019年全球GDP前八国家.html")
