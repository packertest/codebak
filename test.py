import sqlite3
import os


conn = sqlite3.connect('files.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS files
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    filetype TEXT,
    filepath TEXT,
    filesize INTEGER,
    filecontent BLOB)
    ''')

def insert_file(filename, filetype, filepath, filesize, filecontent):
    cursor.execute('''
        INSERT INTO files (filename, filetype, filepath, filesize, filecontent)
        VALUES (?, ?, ?, ?, ?)''', (filename, filetype, filepath, filesize, filecontent))
    conn.commit()
    print('insert ok')


def select_file(filename):
    obj = cursor.execute("SELECT * FROM files WHERE filename=?", (filename,))
    # result = cursor.fetchone()
    for result in obj:
        if result:
            print(f"ID：{result[0]}")
            print(f"File Name：{result[1]}")
            print(f"File Type：{result[2]}")
            print(f"File Path：{result[3]}")
            print(f"File Size：{result[4]}")
            print(f"File Content：{result[5]}")
        else:
            print("record does not exist")


def update_file(filename, new_filepath):
    cursor.execute("UPDATE files SET filepath=? WHERE filename=?", (new_filepath, filename))
    conn.commit()
    print('updated ok')


def delete_file(filename):
    cursor.execute("DELETE FROM files WHERE filename=?", (filename,))
    conn.commit()
    print('delete ok')


with open('test.txt', 'rb') as f:
    content = f.read()
insert_file('test.txt', 'txt', os.path.abspath('test.txt'), os.path.getsize('test.txt'), content)


select_file('test.txt')


update_file('test.txt', os.path.abspath('test/test.txt'))


# delete_file('test.txt')

cursor.close()
conn.close()
