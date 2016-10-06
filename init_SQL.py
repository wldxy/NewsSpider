import MySQLdb

con = MySQLdb.connect('localhost', 'root', '163613', 'user')
with con:
    con = con.cursor()
    con.execute("CREATE TABLE IF NOTE EXIST \
                ")