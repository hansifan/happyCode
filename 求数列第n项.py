""""
斐波那契数列

米兔从兔米那里了解到有一个无限长的数字序列 1,  2，3，3，4，4，4,  5，5，5，5，5 ...,(已知此数列有一定规律
，现将这些数字按不同数值堆叠，相同值的数字在同一层)。米兔想知道这个数字序列的第n个数所在的那一层之前的所有层
里共有多少个数。


"""




n = int(input())
ans = 0    #前一层总数
cnt = 1    #每一层有多少个数
a = 0      #前一层有多少个数
while ans+cnt < n:
    # if ans+cnt>=n:
    #     break
    ans += cnt
    cnt += a        #下一层的数为本层与前一层相加
    a = cnt-a       #a换为本层cnt,即本层数，随即跳到下一个循环
print(ans)



""""" 斐波那契数列输出"""
def Fibonacci(self, n):     
        res=[0,1,1,2]
        while len(res)<=n:
            res.append(res[-1]+res[-2])
        return res[n]


