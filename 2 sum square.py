n=int(input("enter the elements"))
l = [ ]
odd=0
even=0
for i in range(0,n):
    ele=int(input("enter n values"))
    l . append (ele)
print(l)
for i in l:
    if i%2==0:
        even=even+i**2
    else:
        odd=odd+i**2
l=[odd,even]
print(l)
