n= int(input("Enter the number: "))
a=0
b=1
print("the fibonacci series is: ")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c