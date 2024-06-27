# 学生
from people import People

class Student(People):
    identity = '学生'
    grade = ''
    __weight = 0
    # def __init__(self, name, age, __weight,grade):报错私有属性不能被继承
    def __init__(self, name, age,__weight,grade):
        self.__weight = __weight
        super().__init__(name, age, self.set_weight(__weight))
        self.grade = grade
    
    # 重写父类方法
    def description(self):
        str = f'我叫{self.name},今年{self.age}岁,我的体重为{self.__weight}kg,我的身份是{self.identity},我今年上{self.grade}年级'
        print(str)
    
    # 测试
def test():
    if __name__ == '__main__':
        people = Student('mike',15,120,9)
        people.description()
    else:
        return
test()