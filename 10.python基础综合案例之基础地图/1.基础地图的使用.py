# 基础地图的演示
# https://www.ab173.com/gongju/ui/rgb.php
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map1 = Map()
# 准备数据
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499),
    ("天津市", 599)
]
# 添加地图
map1.add("测试地图", data)
# 设置全局选项
map1.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1 - 9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10 - 99", "color": "#FF6666"},
            {"min": 100, "max": 999, "label": " 100 - 999", "color": "#990033"},
        ]

    ),
)

# 绘图
map1.render()
