"""
    图表会动态变化
    创建时间线timeline() ———— 时间线 charts
"""
# 导入软件包
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
# from pyecharts.globals import ThemeType

# 使用Bar构建基础柱状图bar1
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10],
               label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

# 使用Bar构建基础柱状图bar2
bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 25, 20],
               label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

# 使用Bar构建基础柱状图bar3
bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [70, 20, 40],
               label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 构建时间线对象 timeline()
timeline = Timeline()
# 在时间线内添加柱状图对象
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")

# 设置时间线主题 timeline = Timeline({"theme": ThemeType.ROMA})

# 设置自动播放 time.add.schema
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

# 绘图是用时间线对象绘图
timeline.render("基础时间线柱状图.html")
