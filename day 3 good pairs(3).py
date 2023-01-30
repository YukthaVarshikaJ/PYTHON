def solve(nums):
   count=0
   n=len(nums)
   for i in range(n):
      for j in range(i+1,n):
         if nums[i] == nums[j]:
            count+=1
   return count
n=int(input("enter no of elements"))
nums=[]
for i in range (1,n+1,1):
    ele=int(input("enter"))
    nums.append(ele)
print(nums)
print(solve(nums))
