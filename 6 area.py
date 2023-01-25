ef maxArea(A, Len) :
    area = 0
    for i in range(Len) :
        for j in range(i + 1, Len):
            area = max(area, min(A[j], A[i]) * (j - i))
    return area
n=int(input("enter number of elements in array1"))
m=int(input("enter number of elements in array2"))
l1=[]
l2=[]
for i in range(0,n,1):
    ele=int(input("enter number"))
    l1.append(ele)
for j in range(0,m,1):
    el=int(input("enter number"))
    l2.append(el)
print(l1)
print(l2)
 
len1 = len(l1)
print(maxArea(l1, len1))
 
len2 = len(l2)
print(maxArea(l2, len2))
