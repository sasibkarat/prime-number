def prime(start,end):
 p=[]
 for val in range (start,end+1):
   flag=0;
   for n in range(2,val):
     if (val % n)==0:
         flag=1;
   if flag==0:
     p.append(val)
 return p
start=int(input("enter first num"))
end=int(input("enter last num"))
pr=prime(start,end)
print(pr)
