"""
    演示可视化需求1 ： 折线图开发

"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, ToolboxOpts

# 打开文件，选择读取模式
f_US = open("E:/BaiduNetdiskDownload/资料/可视化案例数据/折线图数据/美国.txt", "r", encoding="utf-8")
US_data = f_US.read()
f_jp = open("E:/BaiduNetdiskDownload/资料/可视化案例数据/折线图数据/日本.txt", "r", encoding="utf-8")
jp_data = f_jp.read()
f_in = open("E:/BaiduNetdiskDownload/资料/可视化案例数据/折线图数据/印度.txt", "r", encoding="utf-8")
in_data = f_in.read()

# 去掉不合乎json规范的开头
US_data = US_data.replace("jsonp_1629344292311_69436(", " ")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", " ")
in_data = in_data.replace("jsonp_1629350745930_63180(", " ")

# 去掉不合乎json规范的结尾,但是为防止去掉多了，所以切片选择【开头 到 倒数第二个前】的数据
US_data = US_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# 将json字符串 转python列表/字典
US_dict = json.loads(US_data)
jp_dict = json.loads(jp_data)
in_data = json.loads(in_data)

# 获取trend key
US_trend_data = US_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_data['data'][0]['trend']

# 获取日期数据，用于x轴 取到2020年（到314下标结束）
US_x_data = US_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取确切数据，用于y轴 取到2020年（到314下标结束）
US_y_data = US_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
line = Line()  # 构建折线图对象
# 添加x轴数据
line.add_xaxis(US_x_data)
line.add_yaxis("美国的确诊人数", US_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本的确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度的确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图",
                         pos_left="center", pos_bottom="1%"),
    toolbox_opts=ToolboxOpts(is_show=True)
)

# 调用render生成图表
line.render()

# 关闭文件
f_US.close()
f_jp.close()
f_in.close()
