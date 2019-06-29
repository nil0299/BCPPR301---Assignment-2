import sqlite3


class DbWriter:
    """Structure by Sarah, Jin implemented it"""

    def __init__(self):
        self.my_db = 'temp.db'

    def start_db(self):
        try:
            my_conn = sqlite3.connect(self.my_db)
            print(f"Opened {self.my_db} successfully")
            return my_conn
        except Exception as e:
            print(e)
        finally:
            print("Connection complete")

    def write_db(self, new_module):
        my_conn = self.start_db()
        c = my_conn.cursor()
        try:
            c.execute('''CREATE TABLE IF NOT EXISTS module (
                        classname text PRIMARY KEY, 
                        class_attributes text,
                        class_methods text)''')
            for a_class in new_module.all_my_classbuilders:
                c.execute(f'''UPDATE module set classname = {a_class.name}''')
                for an_a in a_class.all_my_attributes:
                    c.execute(f'''UPDATE module set class_attributes = '{an_a.name}' 
                              WHERE classname = '{a_class.name}''''')
                for an_m in a_class.all_my_methods:
                    c.execute(f'''UPDATE module set class_methods = '{an_m.name}'
                              WHERE classname = '{a_class.name}''''')
        except Exception as e:
            print(e)

    def read_db(self):
        my_conn = self.start_db()
        c = my_conn.cursor()
        for row in c.execute('SELECT * from classes'):
            print(row)
