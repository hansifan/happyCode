
# d-xf      100-15=85
# d-xf >= x*reminder+p*reminder  

# 85>=13 * 6

x,f,d,p = map(int,input().split())

day = 0
if d-x*f<=0:
    day = d // x
else: 
    day = f + (d-x*f) // (x+p)

print(day)

