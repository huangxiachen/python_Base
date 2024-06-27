#定义一个人类
class People:
    name = ''
    age = 0
    # 私有属性
    __weight = 0

    def __init__(self,name,age,__weight):
        self.name = name
        self.age = age
        self.__weight = __weight
    
    # description
    def description(self):
        str = f'我叫{self.name},今年{self.age}岁,我的体重为{self.__weight}kg.'
        print(str)
    
    # 私有属性不能被子类直接访问,所以父类提供访问和修改私有属性的方法
    def get_weight(self):
        return self.__weight
    
    def set_weight(self,weight):
        self.__weight = weight


def test():
    if __name__ == '__main__':
        people = People('maike',15,120)
        # print(people.__weight)直接访问报错
        people.name = 'mike'
        people.__weight = 40 #不报错但修改不了私有属性,被认为是给实例添加了一个属性
        print(people.__weight)
        people.description()
    else:
        return
test()

