num=int(input("Enter any number"))
c=0
rev=0
while (num>0):
    num=num//10
    c+=1
print(c)
a=num
while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
if(a==rev):
    print("The number is palind1rome")
else:
    print("Number is not palindome")



