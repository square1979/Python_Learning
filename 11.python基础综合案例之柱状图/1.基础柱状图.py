"""
 柱状图构建：通过Bar构建基础柱状图
"""
# 导入软件包
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 使用Bar构建基础柱状图
bar = Bar()

# 添加x轴数据
bar.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))

# 反转X轴与Y轴
bar.reversal_axis()
bar.render("基础柱状图.html")
