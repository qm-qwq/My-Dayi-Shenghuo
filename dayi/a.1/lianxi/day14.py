# class Bank:
#     def __init__(self, balance):
#         self.balance = balance
#         self._deposit = 0
#         self.__withdraw = "666"
# account = Bank(100)
# print(account.balance)
# print(account._deposit)
# print(account._Bank__withdraw)
## print(account.__withdraw)


# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#     def area(self):
#






#
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         return self.__balance
#     def qu(self,value):
#         if value > self.__balance:
#             return "余额不足"
#         else:
#             self.__balance -= value
#             return f"取款成功，当前余额：{self.__balance}"
#     def cun(self,value):
#         self.__balance += value
#
# a = BankAccount(0)
# print(a.balance)
# a.cun(100)
# print(a.balance)
# print(a.qu(99))
# print(a.qu(100))




# class Person:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print(f"{self.name}正在吃东西")
# class Child(Person):
#     def bark(self):
#         print(f"{self.name}哇哇叫")
# pr = Child("aad")
# pr.eat()
# pr.bark()
# class Cat(Person):
#     pass
#     # def eat(self):
#     #     print(f"{self.name}优雅的chi")
# cat = Cat("MIMI")
# cat.eat()
#
# class Dog(Person):
#     def __init__(self, name,br):
#         super().__init__(name)
#         self.br = br
#
#     def eat(self):
#         super().eat()
#         print(f"{self.name}吃完天天子")
# dog = Dog("2哈","3哈")
# dog.eat()
# dog.eat()




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我是{self.name} 今年 {self.age} years old")

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def introduce(self):
        print(f"是{self.grade}年级")

p = Person("Z3",18)
p.introduce()
s = Student("l4",15,3)
s.introduce()










