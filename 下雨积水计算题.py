""""
特殊的单调递增
序列a按照最高值划分为两个数组b、c，后半部分翻转
对每一个数组，遍历数组，
若当前最大值t_max小于x，则更新t_max = x；
若大于，则计数 t_max - x
"""
 
def count(a):
    ret, t_max = 0, 0
    for x in a:
        if x > t_max:
            t_max = x
        else:
            ret += t_max - x    #遍历到坑则计数
    return ret
 
if __name__ == "__main__":
    a = list(map(int, input().strip().split(',')))
    b = a[a.index(max(a)):][::-1]                 #[::-1]取列表的逆序   https://blog.csdn.net/love20165104027/article/details/82750523
    c = a[:a.index(max(a)) + 1]
    ans = 0
    ans += count(b)
    ans += count(c)
    print(ans)