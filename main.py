# Muhim mavzular
# List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]
# Description: Python dasturlash tilida o'rganish

# Dictionary comprehension
squares = {number: number ** 2 for number in numbers}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Data types ["int", "float", "complex", "list", "tuple", "range", "str", "dict", "set", "frozenset", "bool", "bytes", "bytearray", "memoryview", "NoneType"] O'rganish kerak bo'lgan data types

# Set comprehension
odd_numbers = {number for number in numbers if number % 2 != 0}
print(odd_numbers)  # {1, 3, 5}
text = 'SalomPython'
# print(text[0]) # textdan birinchi elementni chiqaradi 
# print(text[0:5]) # textdan 0 dan 5 gacha elementlarni chiqaradi
# print(text[::-1]) # textni teskari chiqaradi
# print(text[0:5:2]) # textdan 0 dan 5 gacha elementlarni 2 ta 2 ta chiqaradi
# print(text.upper()) # textni katta harflar bilan chiqaradi
# print(text.lower()) # textni kichkina harflar bilan chiqaradi
# print(text.split()) # textni bo'sh joylar bilan ajratadi
# print(text.split('o')) # textni o bilan ajratadi
# print(text.replace('o', 'a')) # textni o larini a ga almashtiradi
# print(text.find('P')) # textda harflarning index larini topadi
# print(text.count('o')) # textda harflarning nechta borligini topadi
# print(text.strip()) # textni bo'sh joylarni olib tashlaydi
# print(text.lstrip()) # textni chapdagi bo'sh joylarni olib tashlaydi
# print(text.rstrip()) # textni o'ngdagi bo'sh joylarni olib tashlaydi
# print(text.split(' ')) # textni listga aylantiradi
# print(text.join(' ')) # textni so'zlar orasiga qo'shadi
# print(text.startswith('S')) # text S bilan boshlanadimi
# print(text.endswith('n')) # text n bilan tugaydimi
# print(text.capitalize()) # textni bosh harfini katta qiladi # faqat birinchi so'zning bosh harfini katta qiladi
# print(text.title()) # textni so'zlarning bosh harfini katta qiladi # barcha so'zlarning bosh harfini katta qiladi
# print(text.swapcase()) # textni katta harflarini kichik kichiklarini katta qiladi
# print(text.isalpha()) # textda faqat harflar bor yoki yo'q bosh space harfga kirmaydi
# print(text.isdigit()) # textda faqat raqamlar bor yoki yo'q
# print(text.isalnum()) # textda faqat harflar va raqamlar bor yoki yo'q
# print(text.islower()) # text kichkina harflar bilan yozilganmi
# String data type tugadi 

# Generator expression
numbers = (number for number in range(6))
for number in numbers:
    print(number)  # 0, 1, 2, 3, 4, 5
# List data type
list = ['Python', 'Java', 'C++', 'C#', 'JavaScript', 12, 3.12]
# print(list[0]) # listdan birinchi elementni chiqaradi
# print(list[0:3]) # listdan 0 dan 3 gacha elementlarni chiqaradi
# print(list[::-1]) # listni teskari chiqaradi
# print(list[0:3:2]) # listdan 0 dan 3 gacha elementlarni 2 ta 2 ta chiqaradi
# print(list.append('Dunyo')) # listga element qo'shadi
# print(list.pop()) # listdan birinchi elementni olib tashlaydi
# print(list.remove('Python')) # listdan elementni olib tashlaydi
# print(list.clear()) # listni tozalaydi
# print(list.count('Python')) # listda elementning nechta borligini topadi
# print(list.copy()) # listni nusxasini olish
# print(list.reverse()) # listni teskari chiqaradi
# print(list.sort()) # listni tartiblaydi
# print(list.index('Python')) # listda elementning indexini topadi
# print(list.extend(['Django', 'Flask'])) # listga boshqa listni qo'shadi
# print(list.insert(1, 'Django')) # listga boshqa listni qo'shadi # indexni belgilash kerak bo'ladi. index 1 ga qo'shadi
# List data type tugadi

# Map, filter, reduce
from functools import reduce
# Tuple data type
tuple = ('Python', 'Java', 'C++', 'C#', 'JavaScript', 12, 3.12)
# print(tuple[0]) # tupledan birinchi elementni chiqaradi
# print(tuple[0:3]) # tupledan 0 dan 3 gacha elementlarni chiqaradi
# print(tuple[::-1]) # tupleni teskari chiqaradi
# print(tuple[0:3:2]) # tupledan 0 dan 3 gacha elementlarni 2 ta 2 ta chiqaradi
# print(tuple.count('Python')) # tupleda elementning nechta borligini topadi
# print(tuple.index('Python')) # tupleda elementning indexini topadi
# print(tuple.__sizeof__()) # tuple ning hajmi
# print(tuple.__len__()) # tuple ning uzunligi
# print(tuple.__hash__()) # tuple ning hash
# print(tuple.__class__) # tuple ning class
# print(tuple.__dir__()) # tuple ning dir
# print(tuple.__doc__) # tuple ning doc
# print(tuple.__format__()) # tuple ning format
# print(tuple.__getattribute__()) # tuple ning getattribut
# Tuple data type tugadi

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
# Set data type
set = {'Python', 'Java', 'C++', 'C#', 'JavaScript', 12, 3.12}
# print(set[0]) # setdan birinchi elementni chiqaradi
# print(set[0:3]) # setdan 0 dan 3 gacha elementlarni chiqaradi
# print(set[::-1]) # setni teskari chiqaradi
# print(set[0:3:2]) # setdan 0 dan 3 gacha elementlarni 2 ta 2 ta chiqaradi
# print(set.add('Django')) # setga element qo'shadi
# print(set.remove('Python')) # setdan elementni olib tashlaydi
# print(set.clear()) # setni tozalaydi
# print(set.copy()) # setni nusxasini olish
# print(set.discard('Python')) # setdan elementni olib tashlaydi
# print(set.pop()) # setdan birinchi elementni olib tashlaydi
# print(set.update(['Django', 'Flask'])) # setga boshqa setni qo'shadi
# Set data type tugadi

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
# Dictionary data type
#dict = {
 #   'name': 'John',
  # 'city': 'New York',
    #'country': 'USA'
#}
# print(dict['name']) # dictdan birinchi elementni chiqaradi
# print(dict.get('name')) # dictdan birinchi elementni chiqaradi
# print(dict['name']) # dictdan birinchi elementni chiqaradi
# print(dict.keys()) # dictning keylarini chiqaradi
# print(dict.values()) # dictning valuelarini chiqaradi
# print(dict.items()) # dictning itemlarini chiqaradi
# print(dict.pop('name')) # dictdan birinchi elementni olib tashlaydi
# print(dict.popitem()) # dictdan birinchi elementni olib tashlaydi
# print(dict.clear()) # dictni tozalaydi
# print(dict.copy()) # dictni nusxasini olish
# print(dict.setdefault('name', 'John')) # dictdan birinchi elementni chiqaradi
# print(dict.update({'name': 'John'})) # dictga boshqa dictni qo'shadi
# print(dict.__sizeof__()) # dict ning hajmi
# Dictionary data type tugadi

product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24
# Boolean data type
# bool = True
# bool = False
# print(bool) # True
# print(bool.__class__) # <class 'bool'>
# Boolean data type tugadi

# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
# NoneType data type
# none = None
# print(none) # None
# NoneType data type tugadi

@my_decorator
def say_hello():
    print("Hello!")
# # If else statement
# son = 10
# if son > 5:
#     print("Son 5 dan katta")
# else:
#     print("Son 5 dan kichik")

say_hello()
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
# # If elif else statement
# son = 10
# if son > 5:
#     print("Son 5 dan katta")
# elif son < 5:
#     print("Son 5 dan kichik")
# else:
#     print("Son 5 ga teng")

# Generators
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
# # Nested if statement
# son = 10
# if son > 5:
#     print("Son 5 dan katta")
#     if son < 10:
#         print("Son 10 dan kichik")    
# else:
#     print("Son 5 ga teng")

# Itertools
import itertools
# Shartli operatorlar tugadi

numbers = [1, 2, 3]
permutations = list(itertools.permutations(numbers))
print(permutations)  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# # For loop
# Ko'proq malumot 
# for i in range(10):
#     print(i)  # 0 dan 9 gacha chiqaradi
# for i in range(1, 10):
#     print(i)  # 1 dan 9 gacha chiqaradi
# for i in range(1, 10, 2):
#     print(i)  # 1 dan 9 gacha 2 ta 2 ta chiqaradi 
# for i in range(10, 1, -1):
#     print(i)  # 10 dan 1 gacha teskari chiqaradi
# for i in range(10, 1, -2):
#     print(i)  # 10 dan 1 gacha 2 ta 2 ta teskari chiqaradi
# for i in range(10, 1, -3):
#     print(i)  # 10 dan 1 gacha 3 ta 3 ta teskari chiqaradi    
# # For loop tugadi

# Context manager
with open("data.txt", "w") as file:
    file.write("Hello world")
# # While loop
# son = 0
# while son < 10:
#     print(son)
#     son += 1 # 0 dan 9 gacha chiqaradi
# # While loop tugadi

# # Break statement
# son = 0
# while son < 10:
#     print(son)
#     son += 1
#     if son == 5:
#         break # 0 dan 4 gacha chiqaradi
# # Break statement tugadi

# # Continue statement
# son = 0
# while son < 10:
#     son += 1
#     if son == 5:
#         continue # 0 dan 4 gacha chiqaradi
#     print(son)
# # Continue statement tugadi

# # Pass statement
# son = 0
# while son < 10:
#     son += 1
#     if son == 5:
#         pass # 0 dan 4 gacha chiqaradi
#     print(son)
# # Pass statement tugadi

# # Function
# def salom():
#     print("Assalomu alaykum")
# salom() # Assalomu alaykum

# def salom(ism):
#     print(f"Assalomu alaykum {ism}")
# salom("John") # Assalomu alaykum John

# def salom(ism, familiya):
#     print(f"Assalomu alaykum {ism} {familiya}")
# salom("John", "Doe") # Assalomu alaykum John Doe

# def salom(ism, familiya):
#     return f"Assalomu alaykum {ism} {familiya}"
# print(salom("John", "Doe")) # Assalomu alaykum John Doe

# # Function tugadi

# # Lambda function
# salom = lambda ism, familiya: f"Assalomu alaykum {ism} {familiya}"
# print(salom("John", "Doe")) # Assalomu alaykum John Doe
# # Lambda function tugadi

# # Class
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# user = User("John", 25)
# print(user.name) # John
# print(user.age) # 25

# # Class tugadi
# try: 
#     son = int(input("Enter a number: "))
#     print(10 / son)
    
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Zero division error")

# Try tugadi

# # File handling
# file = open("data.txt", "w")
# file.write("Hello world")
# file.close()
# file = open("data.txt", "r")
# print(file.read())
# file.close()
# # File handling tugadi

# # Modules
# import math
# print(math.sqrt(16)) # 4.0 ildiz hisoblaydi
# print(math.pow(2, 3)) # 8.0 darajaga ko'taradi
# print(math.pi) # 3.141592653589793 pi soni
# print(math.e) # 2.718281828459045 e soni
# print(math.factorial(5)) # 120 faktorial hisoblaydi
# print(math.ceil(3.2)) # 4.0 yuqoriga yaxlitlaydi
# print(math.floor(3.2)) # 3.0 yuqoridan yaxlitlaydi
# print(math.trunc(3.2)) # 3.0 butun qismni qaytaradi
# print(math.log(10)) # 2.302585092994046 logarifm hisoblaydi
# print(math.log10(10)) # 1.0 logarifm hisoblaydi
# print(math.log2(10)) # 3.321928094887362 logarifm hisoblaydi
# print(math.sin(90)) # 0.8939966636005579 sin hisoblaydi
# print(math.cos(90)) # -0.4480736161291701 cos hisoblaydi
# print(math.tan(90)) # -1.995200412208242 tan hisoblaydi
# print(math.degrees(1.5707963267948966)) # 90.0 radianni darajaga aylantiradi
# print(math.radians(90)) # 1.5707963267948966 darajani radianga aylantiradi
# print(math.sinh(90)) # 6.102016471589204 sinh hisoblaydi
# print(math.cosh(90)) # 6.102016471589204 cosh hisoblaydi
# print(math.tanh(90)) # 1.0 tanh hisoblaydi
# print(math.asin(1)) # 1.5707963267948966 asin hisoblaydi

# # Modules tugadi

# # Packages
# from math import sqrt
# print(sqrt(16)) # 4.0 ildiz hisoblaydi
# # Packages tugadi
