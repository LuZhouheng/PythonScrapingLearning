import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='mysql123', db='mysql')

cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
