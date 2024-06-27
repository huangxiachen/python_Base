#创建Dog类
class Dog:
    # 构造方法
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(self)
        print(self.__class__)
    
    # 其他行为
    def sit(self):
        print(f'{self.name} is now setting.')
    
    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")
    
    def to_string(self):
        print('{},{}'.format(self.name,self.age))

# 测试
my_dog = Dog('HuiHui',3)
my_dog.sit()
# python是动态语言,支持在实例上动态添加自定义属性
my_dog.color = 'red'
print(my_dog.color)