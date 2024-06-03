"""
    json 是一种轻量级的数据交换格式，可以按照JSON指定格式取组织和封装数据
    JSON本质是一个带有特定格式的字符串
    注意：1.1 json.dumps() 是将 Python 对象转换为 JSON 字符串的函数。
                它接受一个 Python 对象作为参数，并返回一个包含 JSON 字符串的结果。
                这个函数通常用于将数据序列化为 JSON 字符串，以便在网络传输或存储时使用。
         1.2 json.dump() 是将 Python 对象转换为 JSON 格式并写入文件的函数。
                它接受两个参数：一个 Python 对象和一个文件对象。
                它将 Python 对象转换为 JSON 格式，并将结果写入文件对象中。
                这个函数通常用于将数据以 JSON 格式保存到文件中。
         2.1 json.loads() 是将 JSON 字符串解析为 Python 对象的函数。
                它接受一个包含 JSON 字符串的参数，并返回一个对应的 Python 对象。
                这个函数通常用于从网络传输或存储中获取 JSON 字符串，并将其反序列化为 Python 对象。
         2.2 json.load() 是从文件中读取 JSON 数据并解析为 Python 对象的函数。
                它接受一个文件对象作为参数，并从文件中读取 JSON 数据并解析为对应的 Python 对象。
                这个函数通常用于从 JSON 文件中读取数据并将其转换为 Python 对象。
"""
# Python数据【列表，字典】和JSON数据【字符串】的相互转化
import json

# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [{'name': '邢伟', 'age': 18, 'money': 5000},
        {'name': '何文', 'age': 19, 'money': 6000},
        {'name': '黄龙', 'age': 20, 'money': 7000}]

# 带上【ensure_ascii=False】中文不会乱码
json_str1 = json.dumps(data, ensure_ascii=False)
print(f"json_str1的结果为:{json_str1},json_str1的类型为:{type(json_str1)}")

# 准备字典，将字典转换为json字符串
data_dict = {'name': 'jack', 'length': 145, 'school': 'university', 'grade': 'S+'}
json_str2 = json.dumps(data_dict)
print(f"json_str2的结果为:{json_str2},json_str2的类型为:{type(json_str2)}")

# 准备一份字符串转换为Python数据类型 [{},{}]
str1 = json.loads(json_str1)
print(f"str1的结果为:{str1},str1的类型为:{type(str1)}")

# 准备一份字符串转换为Python数据类型 {}
str2 = json.loads(json_str2)
print(f"str2的结果为:{str2},str2的类型为:{type(str2)}")

# 将json字符串转换为Python数据类型 {  }
json_str3 = '{"name": "jack", "length": 145, "school": "university", "grade": "S+"}'
str3 = json.loads(json_str3)
print(f"str3的结果为:{str3},str3的类型为:{type(str3)}")
