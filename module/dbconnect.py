import sqlite3


class DBConnect(object):
    """using context manager to connect database
    """
    def __init__(self, path):
        """connect to database when initalize 
        """
        self.conn = sqlite3.connect(path)

    def __enter__(self):
        """create the cursor when in the with statement
        """
        cursor = self.conn.cursor()
        return cursor

    def __exit__(self, *args):
        """disconnect database when leave with statement
        """
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    with DBConnect('forum.db') as session:
        pid = session.execute(f'SELECT title FROM post').fetchall()
        print(pid)
        
