import sqlite3

# create a connection
conn = sqlite3.connect('test.db')

c = conn.cursor()  # cursor

# create a table
#
c.execute("""CREATE TABLE riddaren (
            attribut TEXT,
            value INTEGER )""")

all_attribut = [
    ('Initiativ', 5),
    ('Tålighet', 9),
    ('Attack', 6),
    ('Smidighet', 4)
]
c.executemany("INSERT INTO riddaren VALUES (?, ?)", all_attribut)

# select data
c.execute("SELECT * FROM riddaren")
print(c.fetchall())

# commit
conn.commit()

# close the connection
conn.close()