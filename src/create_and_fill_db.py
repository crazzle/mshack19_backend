import pathlib
import sqlite3

"""
delete db and recreate it
"""

db_file = pathlib.Path.cwd().parent.joinpath('database', 'features.db')
pathlib.Path.unlink(db_file)  # THIS DELETES THE DB

conn = sqlite3.connect(db_file)
cur = conn.cursor()

# bevoelkerungsindikatoren_haushalte
cur.execute("""
    create table standard_heat(
            long,
            lat,
            busstops,
            nightlife,
            supermarket,
            university
        )
""")
# data = [
#     ('foo', '123'),
#     ('bar', '456'),
#     ('baz', '789'),
# ]
cur.executemany('INSERT INTO standard_heat VALUES (?,?)', data)
conn.commit()

# kita_ms
# ...

conn.commit()
cur.close()
conn.close()
