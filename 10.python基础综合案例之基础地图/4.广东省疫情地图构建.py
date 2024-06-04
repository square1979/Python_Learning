"""
    演示广东省疫情地图可视化的构建
"""
# 导入软件包
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取疫情的JSON文件，并关闭文件减少内存占用
f = open("疫情.txt", "r", encoding="UTF-8")
str1 = f.read()
f.close()

# 将JSON文件转成python文件,并得出可用元组
dict1 = json.loads(str1)
dict1_data = dict1["areaTree"][0]["children"][7]["children"]
dict2_list = []

for province in dict1_data:
    province_name = province["name"]
    province_name = "{}市".format(province_name)
    province_mount = province["total"]["confirm"]
    dict2_list.append([province_name, province_mount])

# 构建图像
# print(dict2_list)
map1 = Map()
map1.add("广东省各地级市疫情确诊人数", dict2_list, "广东")
map1.set_global_opts(
    title_opts=TitleOpts(title="广东省各地级市疫情确诊人数"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 50, "label": "1 - 50 ", "color": "#00FF00"},
            {"min": 51, "max": 100, "label": "51 - 100 ", "color": "#00FF FF"},
            {"min": 101, "max": 200, "label": "101 - 200 ", "color": "#0000FF"},
            {"min": 201, "max": 300, "label": "201 - 300", "color": "#A52A2A"},
            {"min": 301, "max": 400, "label": "301 - 400 ", "color": "#FFA500"},
            {"min": 401, "max": 500, "label": "401 - 500 ", "color": "#FF4500"},
            {"min": 501, "max": 600, "label": "501 - 600 ", "color": "#800000"},
            {"min": 601, "label": "600+ ", "color": "#000000"}

        ]
    )
)
map1.render("广东省疫情地图.html")
