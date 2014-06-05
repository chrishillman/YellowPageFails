import sqlite3

conn = sqlite3.connect("dnsDB.db")
c = conn.cursor()
for row in c.execute("SELECT datedns, timedns, address, dnsname, count(dnsname) AS namecount FROM dnsDB group by dnsname order by namecount DESC"):
	print row
