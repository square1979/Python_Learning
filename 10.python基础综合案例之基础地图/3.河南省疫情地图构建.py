"""
    演示河南省疫情可视化地图的开发
"""
# 导入所需软件包
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取文件
f = open("E:/BaiduNetdiskDownload/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="utf-8")
data = f.read()
f.close()

# 取到河南省中各个城市的数据
# 将字符串json转化为python的字典
f_dict = json.loads(data)
# 从字典中获取河南省中各个城市的数据
# print(f_dict)
# print(type(f_dict))
f_province_data = f_dict["areaTree"][0]["children"][3]["children"]

# print(f_province_data)

data_list = []
for province in f_province_data:
    province_name = province["name"]  # 城市的名字
    # 城市的名字 加上“市”
    if province_name in "济源示范区市":
        province_name = "济源市"
    else:
        province_name = "{}市".format(province_name)
    province_confirm = province["total"]["confirm"]  # 确诊人数
    data_list.append([province_name, province_confirm])

print(data_list)
map2 = Map()
map2.add("河南省内城市确诊人数", data_list, "河南")
map2.set_global_opts(

    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 50, "label": "1 - 50 ", "color": "#ef252e"},
            {"min": 51, "max": 100, "label": "51 - 100 ", "color": "#ee814f"},
            {"min": 101, "max": 150, "label": "101 - 150 ", "color": "#f4e057"},
            {"min": 151, "max": 200, "label": "151 - 200 ", "color": "#4fe70d"},
            {"min": 201, "max": 250, "label": "201 - 250 ", "color": "#0dd4e7"},
            {"min": 251, "max": 300, "label": "251 - 300 ", "color": "#720de7"},
            {"min": 301, "label": "300+ ", "color": "#000000"}

        ]
    )

)
map2.render("河南省疫情地图.html")
