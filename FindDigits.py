# FindDigits.py 中，我们需要完成以下任务：
# 使用 open 打开文件 /tmp/String.txt 并读取其中的字符串
# 提取字符串中的所有数字，并组合成一个新的字符串，然后打印输出

# 打开文件，读取文件中字符串
with open("/tmp/String.txt") as file:
  str = file.read()
res = ""

# 循环字符串中的每个字符，判断其是否为数字
for char in str:
  if char.isdigit():
    res += char
print(res)    

