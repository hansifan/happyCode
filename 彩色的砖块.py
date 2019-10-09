string = str(input(''))

#字符串切片
list_test = []
for i in range(1,len(string)+1):
  list_test.append(string[i-1:i])

#字符串去重
new_list = []
for i in list_test:
    if i not in new_list:
        new_list.append(i)


# 这个题千万不要被这个全排列蒙蔽了，然后傻乎乎的去字母计算全排列，笔试时间有限，肯定有简单的方法。
# 分析一下：如果只有一种大写字母，肯定只有一种情况；
# 如果有两种大写字母，全排列出来有6中，符合题意的肯定只有两种；
# 如果有三种字母（或者>3种），不同字母紧靠且符合题意的肯定没有；
# 所以，显而易见，三种情况考虑就OK了。
size = 0
size = len(new_list)
if size == 2:
    print(2)
elif size == 1:
    print(1)
else:
    print(0)
