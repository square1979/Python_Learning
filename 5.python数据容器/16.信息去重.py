"""
    有如下列表对象：my_list = ['黑马程序员', '传智播客','黑马程序员', '传智播客', 'itheima','itcast','itheima','itcast','best']
    请： 1.定义一个空集合
        2.通过for循环遍历列表
        3.在for循环中将列表元素添加至集合
        4.最终得到元素去重后的集合对象，并打印输出
"""
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客',
           'itheima', 'itcast', 'itheima', 'itcast', 'best']
print(f"有列表为：{my_list}")
set1 = set()
for i in my_list:
    set1.add(i)
print(f"存入集合后结果为：{set1}")
