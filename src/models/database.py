import sqlite3
from pathlib import Path


class DatabaseConnection:
    """
    Usage:
    ```
    db_file = pathlib.Path.cwd().parent.joinpath('database', 'features.db')
    db = DatabaseConnection(db_file)

    with db:
        # do db ops
        # db.cur.<operation>
        pass
    ```
    """

    def __init__(self, file_name: Path):
        self.file_name = file_name

    def __enter__(self):
        self.conn = sqlite3.connect(str(self.file_name))
        self.cur = self.conn.cursor()

    def __exit__(self, exType, exValue, exTraceback):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur
