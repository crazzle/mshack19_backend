import pathlib

from models.database import DatabaseConnection

"""
delete db and recreate it
"""

db_file = pathlib.Path.cwd().parent.joinpath('database', 'features.db')
pathlib.Path.unlink(db_file)  # THIS DELETES THE DB

db = DatabaseConnection(db_file)

with db:
    db.cursor.execute("""
        create table standard_heat(
                long,
                lat,
                public_transport,
                nightlife,
                shops,
                near_university,
                avg_cost
            )
    """)
    data = [
        (7.389923121825148, 51.82050029844267, 1, 22, 4, 1, 0),
        (7.389923121825148, 51.82050029844267, 10, 15, 18, 13, 0),
        (7.389923121825148, 51.82050029844267, 12, 13, 10, 14, 0),
        (7.389923121825148, 51.82050029844267, 19, 9, 14, 20, 0),
        (7.389923121825148, 51.82050029844267, 4, 7, 6, 23, 0),
        (7.389923121825148, 51.82050029844267, 6, 3, 15, 20, 0),
    ]
    db.cursor.executemany('INSERT INTO standard_heat VALUES (?,?,?,?,?,?,?)', data)
    db.connection.commit()
