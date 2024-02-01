n=int(input("enter a number"))
p1=1
while n>0 :
    p1=p1*(n%10)*(n%10)
    n=n//10
print(p1)