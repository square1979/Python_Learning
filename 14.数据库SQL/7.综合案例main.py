"""
使用《面向对象》章节中的数据集，完成使用python语言读取数据并将数据写入MySQL的功能
"""

from pymysql import Connection
from data_define import Record
from file_define import TextFileReader, JsonFileReader

textFileReader = TextFileReader("2011年1月销售数据.txt")
jsonFileReader = JsonFileReader("2011年2月销售数据JSON.txt")

jan_data: list[Record] = textFileReader.read_data()
feb_data: list[Record] = jsonFileReader.read_data()

# 将两个月份的数据合并成一个list来存储
all_data: list[Record] = jan_data + feb_data

# 构建MySQL链接对象
conn = Connection(host="localhost", port=3306, user="root", password="123456", autocommit=True)

# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('py_sql')
# 组织SQL语句
for record in all_data:
    sql = f"insert into orders(order_date,order_id,money,province) " \
          f"values('{record.date}','{record.order_id}',{record.money},'{record.province}')"
    cursor.execute(sql)

conn.close()
