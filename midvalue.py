# printing mid value among three values
a=int(input("enter value"));
b=int(input("enter value"));
c=int(input("enter value"));
if b>a or a<c :
    print(b);
elif a>c or a<b :
 print(a);
elif c>a or c<b :
 print(c); 
else:
  print("no values");
  
