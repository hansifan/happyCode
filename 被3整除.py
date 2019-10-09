l,r = map(int,input().split())    #同时输入两个整数
# split()函数   通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串 https://www.runoob.com/python/att-string-split.html

# map() 会根据提供的函数对指定序列做映射。 https://www.runoob.com/python/python-func-map.html
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

# l,r = input().split()  #同时输入两个字符串

# l,r = eval(input())   2,5


def test(x,y):
    res=[]
    for i in range(x,y+1):
        val=''
        for j in range(1,i+1):
            val+=str(j)
        res.append(val)
    return res
  
t_list = test(l,r)
count = 0

for i in t_list:
  i = int(i)
  if i%3==0:
    count = count+1
print(count)

#超时