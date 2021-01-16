import pymysql


db=pymysql.Connect(host="localhost",port=3306,user="test",passwd="123321",db="spider",charset="utf8")
cursor=db.cursor()

sql="insert into tel(name,phone) values('单位','000')"

cursor.execute(sql)
db.commit()
db.close()
