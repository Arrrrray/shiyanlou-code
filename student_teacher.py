"""
改写 我们在 类 这个实验中 继承 部分的 student_teacher.py 脚本，实现以下功能：

在 Person() 类中增添函数 get_grade()
对于教师类，get_grade() 函数可以自动统计出老师班上学生的得分情况并按照频率的高低以 A: X, B: X, C: X, D: X 的形式打印出来
对于学生类，get_grade() 函数则可以以 Pass: X, Fail: X 来统计自己的成绩情况（A,B,C 为 Pass, 如果得了 D 就认为是 Fail）。
student_teacher.py 文件可以通过在 Xfce 终端中输入如下代码来获取

$ cd /home/shiyanlou/Code
$ wget http://labfile.oss.aliyuncs.com/courses/790/student_teacher.py

要求:
1.请把最终的student_teacher.py 代码文件放在 /home/shiyanlou/Code/ 路径下
2.根据命令行中的第一个参数 teacher 或者 student 来判断最终输出的格式。
3.命令行中第二个输入的参数是需要统计的字符串
"""
#!/usr/bin/env python3
import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def getgrade(self):
      return 0


class Student(Person):
    """
    返回 Student 对象，采用 name ， branch ， year , grade 4个参数
    """

    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
      # 获取用户输入
      common = Counter(self.grade).most_common(4)
      n1 = 0
      n2 = 0
      for item in common:
        if item[0] != 'D':
          n1 += item[1]
        else:
          n2 += item[1]
      print("Pass: {}, Fail: {}".format(n1,n2))

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers, grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))
      
    def get_grade(self):
      s = []
      # 获取用户输入
      common = Counter(self.grade).most_common(4)
      for i,j in common:
        s.append("{}: {}".format(i,j))
      print(", ".join(s))


person1 = Person('Sachin')
if sys.argv[1] == "student":
  student1 = Student('Kushal', 'CSE', 2005,sys.argv[2])
  student1.get_grade()
else:
  teacher1 = Teacher('Prashad', ['C', 'C++'],sys.argv[2])
  teacher1.get_grade()

# print(person1.get_details())
# print(student1.get_details())
# print(teacher1.get_details())