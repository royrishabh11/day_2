n=int(input("enter number: "))

#prime
if n >1:
    for i in range(2,n):
        if(n%i)==0:
            print(n," is not prime.")
            break
    else:
            print(n,"is prime.")
else:
    print(n,"is not prime")

#odd/even

if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")

#palindrome

t=n
r=0
while t>0:
    d=t%10
    r=r*10+d
    t=t//10
if(n==r):
    print(n,"is palindrome")
else:
    print(n,"is not palindrome")

#armstrong

temp=n
sum=0

while temp>0:
    d=temp%10
    sum=sum+d**3
    temp=temp//10

if n==sum:
    print(n,"is armstrong")
else:
    print(n,"is not armstrong")
