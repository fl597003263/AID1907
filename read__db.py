'''
read_db.py
'''
'''
mysql.py
pymysql  操作数据库
'''

import pymysql

# 连接数据库
db = pymysql.connect(user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
# 获取游标（操作数据库，执行sql语句，得到执行结果）
cur = db.cursor()

# 获取数据
sql = "select * from class where age = '57';"
cur.execute(sql)

# #可以直接遍历游标:第一种方法
# for i in cur:
#     print(i)

# # 第二种方法：
# all_row = cur.fetchall()
# print(all_row)

# # 获取多个查询结果
# many_row = cur.fetchmany(2)
# print(many_row)

# 获取一个查询结果
one_row = cur.fetchone()
print(one_row)

# 关闭游标
cur.close()

# 关闭数据库
db.close()
