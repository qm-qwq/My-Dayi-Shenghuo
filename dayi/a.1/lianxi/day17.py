# def divide(a,b):
#     print(f"a = {a} , b = {b}")
#     return a / b
# result = divide(10,0)

# def divide(a,b):
#     assert b != 0
#     return a/b

# print(divide(10,5))
# print(divide(10,0))


# import pdb
#
# def buggy_function(x):
#     y = x * 2
#     pdb.set_trace()
#     z = y / 0
#     return z
#
# buggy_function(1)




# Python 3.7+ 简化写法：直接使用 breakpoint() 替代 pdb.set_trace()。
# def buggu_function(x):
#     y = x * 2
#     breakpoint()
#     z = y / 0
#     return z





def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    breakpoint()
    # 假设这里有个 bug：当 numbers 为空时，count 为 0
    average = total / count
    return average
try:
    result = calculate_average([])
    print(result)
except ZeroDivisionError:
    print("请重新输入")
















