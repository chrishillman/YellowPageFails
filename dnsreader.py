import sqlite3

conn = sqlite3.connect("dnsDB.db")
c = conn.cursor()
c.execute("CREATE TABLE dnsDB (datedns TEXT, timedns TEXT, ampm TEXT, protocol TEXT, direction TEXT, address TEXT, dnsname TEXT)")
readlist = list()
with open("dnstextsample.txt") as file:
	for line in file:
		line = line.replace("\n", "")
		line = line.replace("\r", "")
		linearr = line.split(" ")
		for i in range(0, linearr.count('')):
			linearr.remove('')
		for i in range(0, len(linearr)):
			print str(i) + "  " + linearr[i]
		print"      "
		readlist.append((linearr[0],linearr[1],linearr[2],linearr[6],linearr[7],linearr[8],linearr[-1]))
c.executemany("INSERT INTO dnsDB VALUES (?,?,?,?,?,?,?)", readlist)
for row in c.execute("SELECT * FROM dnsDB"):
	print row
