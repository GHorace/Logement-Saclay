import core.db as db

conn = db.get_connection()

print(conn.execute("SHOW DATABASES").fetchall())