with open(r'D:\Codes\test\eml\test doc.eml', 'rb') as f:
    msg = email.message_from_binary_file(f)
    
# 提取附件并保存到指定文件夹
if msg.is_multipart():
    for part in msg.walk():
        content_type = part.get_content_type()
        disposition = str(part.get("Content-Disposition"))
        if content_type != 'text/plain' and 'attachment' in disposition:
            filename = part.get_filename()
            if filename:
                # 解码文件名
                decoded_filename = decode_header(filename)[0][0]
                if isinstance(decoded_filename, bytes):
                    # 如果文件名是bytes类型，则解码为字符串
                    decoded_filename = decoded_filename.decode()
                # 拼接文件路径并保存文件
                filepath = os.path.join(r'/home/test', decoded_filename)
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))
