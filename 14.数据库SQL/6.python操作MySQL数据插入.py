# 演示使用pymysql库进行数据插入的操作
# pymysql库在执行对数据库有修改操作的行为时，需要通过链接对象的commit成员方法进行确认
# 自动提交设置在连接中设置 autocommit = True

from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host='localhost',  # 主机（IP）
    port=3306, user="root", password="123456",
    autocommit=True
)
# print(conn.get_server_info())
# 执行非查询性质的SQL
cursor = conn.cursor()  # 获取游标对象
conn.select_db('world')  # 选择数据库
# cursor.execute("create table test_pymysql2(id int);")  # 新建表格
# 执行查询性质SQL
cursor.execute("insert into student values (10002,'林俊杰',32,'男')")
# 关闭连接
conn.close()
