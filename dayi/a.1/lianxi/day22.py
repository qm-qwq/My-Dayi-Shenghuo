# import numpy as np
# a = np.array([1, 2, 3])        # 一维数组：[1 2 3]
# b = np.array([[1,2],[3,4]])     # 二维数组：2行2列俩中括号
# c = np.arange(5)           # 生成 [0 1 2 3 4]
# d = np.arange(1, 10, 2)    # 生成 [1 3 5 7 9]
# e = np.linspace(0,1,5) # 生成 [0.  0.25 0.5 0.75 1. ]
#
# zeros = np.zeros((2, 3))   # 生成2行3列、全是0的数组
# ones = np.ones((3, 2))     # 生成3行2列、全是1的数组
# rand_arr = np.random.rand(2, 3)    # 生成2x3的数组，数值在[0,1)之间
# rand_int = np.random.randint(1,10,size=(3,4))  # 生成3x4的数组，数值是[1,10)的随机整数
#
#
# a1 = np.array([[1,2,3],[4,5,6]])
# print(a1.shape) #(2,3)维度
# print(a1.ndim) #2 轴数
# print(a1.size) # 6 元素个数
# print(a1.dtype) # int64 数据类型
#
# a2 = np.array([10,20,30,40,50])
# print(a2[0])
# print(a2[1:4])
# print(a2[-1])
#
# b2 = np.array([[1,2,3],
#                 [4,5,6],
#                [7,8,9]])
# print(b2[1,2]) #第二行第三列 索引从0开始
# print(b2[0]) #整行
# print(b2[:,1]) #整列
# print(b2[:,2,1:3]) #行和列 打印都是横着打印
# print(b2[::1,::2])



# import numpy as np
# q = np.random.randint(1,100,size=(3,4))
# print(q)
# print(q.shape)
# print(q.ndim)
# print(q[0])
# print(q[:,0])
# print(q[1,2])




import numpy as np

arr = np.array([1,2,3,4])
print(arr * 2)
print(arr + 10)
print(arr ** 2)
print(np.sqrt(arr))

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(a * b)
print(a + b)

arr = np.array([5,2,1])
print(arr > 3) #判断的（大于小于号）

# axis=0：沿着行方向（跨行），对每列操作
# axis=1：沿着列方向（跨列），对每行操作
arr2d = np.array([[1,2,3,]
                  ,[4,5,6,]])
print(np.sum(arr2d,axis=0)) #每列和
print(np.mean(arr2d,axis=1)) #每行均值

arr = np.array([1,2,3])
print(arr + 10) #广播 就是把一个10变成【10，10，10】再相加

arr1 = np.array(([1,2,3],
                 [4,5,6])) #两行三列
row = np.array([10,20,30])
print(row + arr1)

col = np.array([[10],[20]]) #列  一列两行
print(col + arr1)

# 该知识点4了 明天加油











