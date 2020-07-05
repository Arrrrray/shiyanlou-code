# CircleArea.py
# 本挑战中，我们将实现一个程序用来计算半径为 2 的圆的面积并打印输出。
# CircleArea.py 能够计算出一个半径为2的圆的面积，并且把面积打印出来，保留小数点后10位。
import math
CircleArea = math.pi * 2 * 2
print('半径为2的圆的面积为：{:.10f}'.format(CircleArea))