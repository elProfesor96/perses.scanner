import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('perses.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS perses
             (id INTEGER PRIMARY KEY, filehash TEXT, filename TEXT, clamav TEXT, comodo TEXT, avg TEXT, defender TEXT, analyzed TEXT)''')
        self.conn.commit()
        self.conn.close()

    def insert(self, filehash, filename, clamav, comodo, avg, defender, timestamp):
        self.conn = sqlite3.connect('perses.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO perses VALUES (NULL, '" + filehash + "', '" + filename + "', '" + clamav + "', '" + comodo + "', '" + avg + "', '" + defender + "', '" + timestamp + "')")
        self.conn.commit()
        self.conn.close()

    def search(self, filehash):
        self.conn = sqlite3.connect('perses.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM perses WHERE filehash=?", (filehash,))
        result = self.c.fetchall()
        self.conn.close()
        return result

    def wipe(self):
        self.conn = sqlite3.connect('perses.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute("DELETE FROM perses")
        self.conn.commit()
        self.conn.close()

#db = Database()
#db.insert("hashed", "filename", "clam_status", "comodo_status", "avg_status", "defender_status", "first_scanned")
#result = db.search("hashed")
#print(result)



