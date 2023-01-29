class Solve():
   def Anagrams( self, li ):
       dictionary = {}
       for word in li:
           sortedWord = ''.join(sorted(word))
           if sortedWord not in dictionary:
               dictionary[sortedWord] = [word]
           else:
               dictionary[sortedWord] += [word]
       return [dictionary[i] for i in dictionary]

if __name__ == '__main__':
    li=[]
    n=int(input("enter number of words"))
    for i in range(1,n+1,1):
        ele=input("enter")
        li.append(ele)
    print(li)
print(Solve().Anagrams(li))
Footer
