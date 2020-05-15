n=int(input("Enter No.: "))

for i in range(n):
    print("* "*(n-i)+"    "*i+" *"*(n-i))
for i in range(1,n+1):
    print("* "*i+"    "*(n-i)+" *"*i)