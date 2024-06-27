#创建类对象
'''
创建一个名为 Restaurant 的类,为其 __init__() 方法设置
两个属性：restaurant_name 和 cuisine_type。创建一个名为
describe_restaurant() 的方法和一个名为 open_restaurant() 的方法,
其中前者打印前述两项信息,而后者打印一条消息,指出餐馆正在营业。
根据这个类创建一个名为 restaurant 的实例,分别打印其两个属性,再调用前
述两个方法。
'''
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self) :
        print("{} is beautiful!".format(self.restaurant_name))
    
    def open_restaurant(self) :
        print("{}  {} !".format(self.restaurant_name,self.cuisine_type))

restaurant = Restaurant('好吃店','开业了')
print(restaurant.restaurant_name + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()