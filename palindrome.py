
"""
def reverse(n):
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev    



n=int(input())
print(n==reverse(n))

"""
"""
n=int(input())
print(n==int(str(n)[::-1]))
"""

"""
def reverse(n):
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev    



n=int(input())
if n==reverse(n):
    print(n)
else:
    i=1
    while True:
        if n+i==reverse(n+i):
            print(n+i)
            break
        i+=1
"""
"""
def reverse(n):
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev    



n=int(input())
if n==reverse(n):
    print(n)
else:
    i=1
    while True:
        if n-i==reverse(n-i):
            print(n-i)
            break
        i+=1
"""
"""

def reverse(n):
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev    



n=int(input())
if n==reverse(n):
    print(n)
else:
    i=1
    while True:
        if n-i==reverse(n-i):
            r=n-i
            print(r)
            break
        i+=1
    i=1
    while True:
        if n+i==reverse(n+i):
            t=n+i
            print(t)
            break
        i+=1
    if abs(n-r)<=abs(t-n):
        print(r)
    else:
        print(t)
"""


def reverse(n):
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev    



n=int(input())
m=int(input())
c=0
i=1
while True:
    
    if n+i==reverse(n+i):
        c+=1
    
    if c==m:
        print(n+i)
        break
    i+=1






























