
"""
import pyodbc

conn = pyodbc.connect(
    "DRIVER={odbc driver 18 for SQL Server};"
    "SERVER=localhost\sqlexpress;"
    "DATABASE=ShohinKanri;"
    "UID=sa;"
    "PWD=sa;"
    "TrustServerCertificate=yes;"   ##証明書検証スキップ
)

cursor = conn.cursor()
"""


from SQLServerManagerClass import SQLServerManager

db = SQLServerManager('config.json')

try:
    db.connect()
    print("データベースに接続しました。")
    
    #rows = db.execute_query("SELECT * FROM M_Shohin")

    sql = "SELECT * FROM M_Shohin"
    rows = db.execute_query(sql)
    
    for row in rows:
        print(row)

except Exception as e:
    print("エラーが発生しました:", e)
finally:
    db.close() 
    print("データベース接続を閉じました。")