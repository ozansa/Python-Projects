#importing sqlite3 module
import sqlite3

# list of files
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# connecting to the database
conn = sqlite3.connect('db_162.db')

with conn:
    cur = conn.cursor()

    # create the database table if it does not already exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tbl_txtFiles (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            col_fileName TEXT
        )
    """)

    # for loop to add all .txt files to the database
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_txtFiles (col_fileName) VALUES (?)", (file,))
            print(file)

    # commit the transaction
    conn.commit()

# close the database connection
conn.close()
