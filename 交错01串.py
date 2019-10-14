s = str(input())

#字符串切片
list_test = []
for i in range(0,len(s)):
    list_test.append(s[i:i+1])

count = 1          #最少为1
count_max = 1       #防止count重新变回1
count_list = []   #存放count记录
for index,item in enumerate(list_test):   
    #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    #https://www.runoob.com/python/python-func-enumerate.html
    if index < len(s)-1:
        if item == list_test[index+1]:
            count = 1
        else:
            count += 1
            # if count>1:
            #     count_list.append(count)
    if count>count_max:
        count_max = count
# print(max(count_list))
print(count_max)