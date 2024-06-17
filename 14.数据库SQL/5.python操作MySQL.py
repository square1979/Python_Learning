# 使用第三方库：pymysql模块，创建到 MySQL的数据库连接
from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host='localhost',  # 主机（IP）
    port=3306, user="root", password="123456"
)
# print(conn.get_server_info())
# 执行非查询性质的SQL
cursor = conn.cursor()  # 获取游标对象
conn.select_db('world')  # 选择数据库
# cursor.execute("create table test_pymysql2(id int);")  # 新建表格
# 执行查询性质SQL
cursor.execute("select * from student;")
result = cursor.fetchall()  # 元组中嵌套元组
for row in result:
    print(row)
# 关闭连接
conn.close()
