l,r = map(int,input().split())    #同时输入两个整数
# split()函数   通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串 https://www.runoob.com/python/att-string-split.html

# map() 会根据提供的函数对指定序列做映射。 https://www.runoob.com/python/python-func-map.html
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

# l,r = input().split()  #同时输入两个字符串

# l,r = eval(input())   2,5



#超时算法

# def test(x,y):
#     res=[]
#     for i in range(x,y+1):
#         val=''
#         for j in range(1,i+1):
#             val+=str(j)
#         res.append(val)
#     return res
  
# t_list = test(l,r)
# count = 0

# for i in t_list:
#   i = int(i)
#   if i%3==0:
#     count = count+1
# print(count)

#找规律，第1个数不能被3整除，第2、3个可以；第4个数不能被3整除，第5、6个可以。。。。。。。。。。。。。。

# count_1 = 0
# count_2 = 0
# count_3 = 0
# y = 0
# z = 0
# count_1 = (r // 3)*2

# y = r%3

# if y==2:
#     count_2 = 1
# else:
#     count_2 = 0



# print(count_1+count_2-count_3)

# test_1
def calcCount(x):
    count_1 = (x//3)*2
    if x%3==2:
        count_1 += 1
    return count_1

print(calcCount(r)-calcCount(l-1))
# if l%3==1:
#     print(calcCount(r)-calcCount(l))
# else:
#     print(calcCount(r)-calcCount(l)+1)

#text_2  超时
# count = 0
# for i in range(l,r+1):
#     if i%3==2 or i%3==0:
#         count+=1
# print(count)