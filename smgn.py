n=int(input("no."))
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)
    n= n//10
print("sum is :",sum)