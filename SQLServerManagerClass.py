import json
import pyodbc

class SQLServerManager:
    def __init__(self, config_path='config.json'):
        #with open(config_path, 'r') as f:
        with open(r'C:\vbcode\python\config.json', 'r') as f:
            self.config = json.load(f)
        self.conn=None
        self.cursor=None
        
    def connect(self):
        conn_str = (
            f'DRIVER={self.config["driver"]};'
            f'SERVER={self.config["server"]};'
            f'DATABASE={self.config["database"]};'
            f'UID={self.config["username"]};'
            f'PWD={self.config["password"]};'
            f"TrustServerCertificate=yes;"
        )
        self.conn=pyodbc.connect(conn_str)
        self.cursor=self.conn.cursor()

    def execute_query(self, sql, params=()):
        self.cursor.execute(sql, params)
        if sql.strip().lower().startswith("select"):
            return self.cursor.fetchall()
        else:
            self.conn.commit()
            return None
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        