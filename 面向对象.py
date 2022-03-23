class Aniaml(object):
    type_name = '动物类1'
    def __init__(self,name,sex,age):
            self.name = name
            self.age = age
            self.sex = sex
    def eat(self):
        print(self)
        print('吃东西')
class Person(Aniaml):
    pass
class Cat(Aniaml):
    pass
class Dog(Aniaml):
    pass
# 类名：
# print(Person.type_name)  # 可以调用父类的属性，方法。
# print(Person.__dict__)
# Person.eat(111)
# print(Person.type_name)
# 对象：
# 实例化对象
p1 = Person('春哥','男',18)
# # print(p1.__dict__)
# # 对象执行类的父类的属性，方法。
# print(p1.type_name)
# p1.type_name = '666'
print(p1.type_name)
print(p1)
p1.eat()


