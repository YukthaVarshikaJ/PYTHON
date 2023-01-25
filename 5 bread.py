a=float(input("enter the number of fresh loaves purchased"))
b=float(input("enter the number of old loaves purchased"))
new=185*a
c=b*(185*60)/100
old=b*185-c
total=new+old
print("regular price=185.00")
print("amount of new loaves",new)
print("amount of old loaves",old)
print("total amount",total)
