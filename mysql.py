'''
mysql.py
pymysql  操作数据库
'''


import pymysql

# 连接数据库
db = pymysql.connect(
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
# 获取游标（操作数据库，执行sql语句，得到执行结果）
cur = db.cursor()

# 执行语句
sql = "insert into class values(6,'七哥',17,'w',123456789,78,0);"
cur.execute(sql)

# 提交到数据库
db.commit()

# 关闭游标
cur.close()

# 关闭数据库
db.close()