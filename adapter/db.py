import mysql.connector
from settings import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

config = {
  'user': DB_USER,
  'password': DB_PASSWORD,
  'host': DB_HOST,
  'database': DB_NAME
}

class DataBase:

  def insDB(query, values): 
    db = mysql.connector.connect(**config)
    cursor = db.cursor(dictionary=True)
    cursor.execute(query, values)
    db.commit()
    last_inserted_id = cursor.lastrowid
    cursor.close()
    db.close()
    return last_inserted_id

  def selDB(query, values=None):
    db = mysql.connector.connect(**config)
    cursor = db.cursor(dictionary=True)
    result = cursor.execute(query, values)
    rows = cursor.fetchall()
    db.close()
    return rows