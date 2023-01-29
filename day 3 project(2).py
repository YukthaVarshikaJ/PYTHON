n=int(input("enter number of elements in list"))
l1=[]
for i in range(1,n+1,1):
    ele=int(input("enter"))
    l1.append(ele)
print(l1)
comb = permutations(l1,3)
for i in comb:
    print(i)
