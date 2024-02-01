n=int(input("enter a number"))
rev=0
org=n
while n>0 :
    rev=(rev*10)+n%10
    n=n//10
print(rev) 
if rev==org :
    print("it is pallindrome")
else :
    print("not pallindrome")