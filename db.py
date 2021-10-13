import connect, mysql.connector
print("import done - establishing connection")
conn = mysql.connector.connect(user=connect.dbuser, \
     password=connect.dbpass, host=connect.dbhost, database=connect.dbname, autocommit=True)
print(f"connection done - {conn}")
with conn:
    cur = conn.cursor()
    cur.execute("select * from Fixtures limit 1;")
    select_Fixtures = cur.fetchall()
    print(select_Fixtures[0])
    
    


