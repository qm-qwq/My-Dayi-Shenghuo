# class Dog :
#     pass
# dog =  Dog()
# print(type(dog))
#
# class Dog :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(f"{self.name} 汪汪！")
#
#     def bark2(self):
#         print(f"{self.name}现在{self.age}岁了")
# dog1 = Dog("Bob",18)
# dog2 = Dog("jio",8)
# print(dog1.age)
# print(dog2.name)
#
# dog1.bark()
# dog2.bark2()





# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"{self.name} 汪汪叫")
#     def display2(self):
#         print(f"{self.name} is {self.age} years old")
# d1 = Dog("旺财",8)
# d1.display()
# d1.display2()
# d2 = Dog("小黑",7)
# d2.display()
# d2.display2()
#
#
#
#
#
# class Student:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     school = "圣芙蕾雅学院"
# s1 = Student("张三",14)
# s2 = Student("里斯",13)
# print(s1.age)
# print(s2.age)
# print(s1.school)
# print(s2.school)
# Student.school = "qit"
# print(s1.school)
# print(s2.school)


# class MyClass:
#     class_var = 0
#     def __init__(self,value):
#         self.instance_var = value
#     def display(self):
#         print(self.instance_var)
#     @classmethod
#     def display2(cls):
#         print(cls.class_var)
#     @staticmethod
#     def display3():
#         print("jingtai")
#
# obj = MyClass(5)
# obj.display()
# MyClass.display2()
# obj.display2()
# MyClass.display3()
#
#
#
# class Dog:
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         Dog.count += 1
# d1 = Dog("旺财")
# d2 = Dog("小黑")
# print(Dog.count)






class Person:
    population = 0
    def __init__(self,name):
        self.name=name
        Person.population += 1
    @classmethod
    def get_population(cls):
        print(f"当前人口数：{Person.population}")

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True

per = Person("13")
per2 = Person("13")
per3 = Person("13")
Person.get_population()
print(Person.is_adult(20))



















