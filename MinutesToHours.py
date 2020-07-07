# 在 MinutesToHours.py 文件中实现一个函数 Hours()，将用户输入的 分钟数 转化为 小时数和分钟数，并要求小时数尽量大。将结果以 XX H, XX M 的形式打印出来。
# 要求：
#用户能够通过命令行参数输入分钟数，不要使用 input，命令行参数可以使用 sys.argv 来提取。例如程序执行为 python3 MinutesToHours.py 80，传入的参数 80 就是分钟数，程序需要打印出相应的小时数和分钟数，输出为 1 H, 20 M。
#如果用户输入的是一个负值，程序需要 raise 来抛出 ValueError 异常。
#Hours() 函数调用的时候，需要使用 try...except 处理异常。获取异常后，在屏幕上打印出 Parameter Error 提示用户输入的值有误。

import sys

# 时间转换函数
def Hours(minute):
  # 如果输入的值为负数，raise异常
  if minute < 0:
    raise ValueError('请输入正整数')
  else:
    print('{} H, {} M'.format(int(minute / 60), minute % 60))
    
# 函数调用及异常处理
try:
  Hours(int(sys.argv[1]))
except:
  print("输入参数错误")