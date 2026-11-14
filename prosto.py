#/usr/bin/python3
def simnumbers(n):
    numbers=[]
    a=2 
    while n > 1:
        while n%a==0:
            numbers.append(a)
            n //= a 
        a+=1
    return numbers
n=int(input())
result=simnumbers(n)
print(result)

