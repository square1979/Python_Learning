def append_to_file(flier, data):
    c = open(flier, 'a', encoding='utf-8')
    c.write(data)
    c.close()


append_to_file("E:/project/file.txt", "外卖即将送到\n")
