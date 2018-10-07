import cx_Oracle
import sys

host_name = '192.168.237.131'
port = '1521'
ora_sid = 'orcl'
usr_id = 'system'
paswd = 'Kamemiya007'

args = sys.argv
if len(args) != 2:
    print("実行するSQLファイルを引数に１つ設定してください。")
    sys.exit(1)

file_path = args[1]

f = open(file_path, 'r')

for sqlfile in f:
    sql_load = sqlfile

    tns = cx_Oracle.makedsn(host_name, port, ora_sid)
    conn = cx_Oracle.connect(usr_id, paswd, tns)

    cur = conn.cursor()

    cur.execute(sql_load)

    rows = cur.fetchall()

    for r in rows:
        print(r)

f.close()