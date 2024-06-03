"""
    演示全国疫情可视化地图的开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 添加用到的软件包

# 读取文件
f = open("E:/BaiduNetdiskDownload/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="utf-8")
data = f.read()
f.close()

# 取到各省的数据
# 将字符串json转化为python的字典
f_dict = json.loads(data)
# 从字典中获取省份的数据
# print(f_dict)
# print(type(f_dict))
f_province_data = f_dict["areaTree"][0]["children"]
# <class 'list'> print(type(f_province_data))
data_list = []
for f_province in f_province_data:
    province_name = f_province["name"]  # 省份名称
    if province_name in "天津北京重庆上海":
        province_name = "{}市".format(province_name)
    elif province_name in "内蒙古西藏":
        province_name = "{}自治区".format(province_name)
    elif province_name in "宁夏":
        province_name = "{}回族自治区".format(province_name)
    elif province_name in "广西":
        province_name = "{}壮族自治区".format(province_name)
    elif province_name in "新疆":
        province_name = "{}维吾尔自治区".format(province_name)
    elif province_name in "香港澳门":
        province_name = "{}特别行政区".format(province_name)
    else:
        province_name = "{}省".format(province_name)
    province_confirm = f_province["total"]["confirm"]  # 确诊人数
    data_list.append([province_name, province_confirm])

# print(data_list)
map1 = Map()
map1.add("各省份确诊人数", data_list, "china")
map1.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1 - 99 ", "color": "#ef252e"},
            {"min": 100, "max": 999, "label": "10 - 999 ", "color": "#ee814f"},
            {"min": 1000, "max": 9999, "label": "1000 - 9999 ", "color": "#f4e057"},
            {"min": 10000, "max": 99999, "label": "10000 - 99999 ", "color": "#4fe70d"},
            {"min": 100000, "max": 999999, "label": "100000 - 999999 ", "color": "#0dd4e7"},
            {"min": 1000000, "label": "1000000+ ", "color": "#720de7"}

        ]
    )
)
map1.render("全国疫情地图.html")
