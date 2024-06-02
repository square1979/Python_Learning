# 文件追加写入‘a'，文件不存在会创建，文件存在会在原有内容后续继续写入
f = open("E:/project/test.txt", "a", encoding="utf-8")
f.write("\n黑马程序员，学python最佳选择,月薪过万")
f.close()
