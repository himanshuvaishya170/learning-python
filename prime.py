n=int(input("enter a number"))
count=0
i=1
while n>=i :
    if n%i==0:
        count=count+1
    i=i+1 
if count==2 :
    print("it is prime number")
else :
    print("it is composite number")        