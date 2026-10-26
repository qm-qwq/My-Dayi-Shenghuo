


# class Person:
#     def sound(self):
#         pass
# class Student(Person):
#     def sound(self):
#         print("哦哦哦")
# class Stuntss(Person):
#     def sound(self):
#         print("影月月")
#
# person = [Student(), Stuntss()]
# for p in person:
#     p.sound()
# def speak(person):
#     person.sound()
# ss = Stuntss()
# st = Student()
# speak(ss)
# speak(st)



# class Shape:
#     def area(self):
#         return 0
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
# xingzhuang = [Rectangle(4,5),Circle(3)]
# for x in xingzhuang:
#     print(x.area())





# class Book:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def __str__(self):
#         return f"《{self.name}》by {self.price}"
#     def __repr__(self):
#         return f"book('{self.name}', '{self.price}')"
#
# b = Book("python", 18)
# print(b)
# print(repr(b))

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages

b = Book("mingz","zuoze",300)
print(b)
print(len(b))






