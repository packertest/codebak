import sqlite3

conn = sqlite3.connect('file_database.db')
conn.execute('''CREATE TABLE files
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             file_name TEXT NOT NULL,
             file_path TEXT NOT NULL,
             file_content TEXT NOT NULL);''')

data = [
    ('example1.txt', '/home/user/documents/', 'This is an example file 1.'),
    ('example2.txt', '/home/user/documents/', 'This is an example file 2.'),
    ('example3.txt', '/home/user/documents/', 'This is an example file 3.')
]

conn.executemany("INSERT INTO files (file_name, file_path, file_content) VALUES (?, ?, ?)", data)


cursor = conn.execute("SELECT * FROM files WHERE file_path='/home/user/documents/'")

for row in cursor:
    print("ID = ", row[0])
    print("File name = ", row[1])
    print("File path = ", row[2])
    print("File content = ", row[3], "\n")

conn.commit()
conn.close()


import sqlite3
import os


conn = sqlite3.connect('file_database.db')


# conn.execute('''CREATE TABLE files
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#              file_name TEXT NOT NULL,
#              file_path TEXT NOT NULL,
#              file_extension TEXT NOT NULL,
#              file_size INTEGER NOT NULL,
#              file_content BLOB NOT NULL);''')


path = r'/home/user/documents/'
files = os.listdir(path)
for file in files:
    file_path = os.path.join(path, file)
    file_name, file_extension = os.path.splitext(file)
    file_size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        file_content = f.read()
    conn.execute("INSERT INTO files (file_name, file_path, file_extension, file_size, file_content) \
                  VALUES (?, ?, ?, ?, ?)", (file_name, path, file_extension, file_size, file_content))


cursor = conn.execute("SELECT * FROM files WHERE file_path='/home/user/documents/'")
for row in cursor:
    print("ID = ", row[0])
    print("File name = ", row[1])
    print("File path = ", row[2])
    print("File content = ", row[3], "\n")

conn.commit()
conn.close()

#############################################################################

import email
from email import policy
from email.parser import BytesParser
import re

from bs4 import BeautifulSoup

# 打开 .eml 文件并读取内容
eml_path = r"/home/user/documents/0.eml"
with open(eml_path, 'rb') as eml_file:
    eml_content = eml_file.read()

# 解析 .eml 文件内容并获取文本内容
msg = BytesParser(policy=policy.default).parsebytes(eml_content)
text_content = ''

if msg.is_multipart():
    # 如果消息是多部分的，则迭代所有部分来获取文本内容
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            # 获取纯文本部分的内容
            text_content += part.get_payload()
        elif part.get_content_type() == 'text/html':
            # 获取HTML部分的内容，并将其转换为纯文本
            html_content = part.get_payload()
            soup = BeautifulSoup(html_content, 'html.parser')
            text_content += soup.get_text(separator='\n')
else:
    # 如果消息不是多部分的，则直接获取文本内容
    text_content = msg.get_payload()

    # 移除HTML标记和样式
    text_content = re.sub(r'<.*?>', '', text_content)

    # 替换特殊字符
    text_content = re.sub(r'=20', ' ', text_content)
    text_content = re.sub(r'&nbsp;', ' ', text_content)
    text_content = re.sub(r'&amp;', '&', text_content)

    # 清理文本
    text_content = re.sub(r'(\n\s*)+', '\n', text_content)
    text_content = re.sub(r'(\s*\n)+', '\n', text_content)
    text_content = re.sub(r'\s+', ' ', text_content)

print(text_content)
