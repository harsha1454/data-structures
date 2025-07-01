'''#Array operations
#program to consider a list arr=[0,20,20,40] and perform inset opeaions
and deletion opertion with 50 and 25 respectively and trverse
the aray to fetch a number 25 is present or not'''
arr=[10,20,30,40]
#insert
arr.append(50)
arr.insert(2,25)
print(arr)
#deletion
arr.remove(30)
arr.pop()
print(arr)
#traversel
for i in arr:
    print(i,end=' ')
print("\n 25 in array?",25 in arr)    
text=input("enter a name")
if text==text[::-1]:
    print("palindrome")
else:
    print("not")
freq={}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
print(freq)           

'''arr of list of size n
key for search element
start with zero index
compare arr[i]==key
  arr[i]=key return index
  else not(move to next index)
repeat same steps till n-1  
'''
def linear_searh(arr,key):
    for i in range(len(arr))
size=int(input("enter the size of array:"))
arr=[]
print("enter the elements:")
for i in range(size):
    num=int(input(f"Element {i+1}:"))
    arr.append(num)
key= int(input("Enter the element to search")) 
result=linear_search(arr,key)
if result !=-1:
    print(f"\n Element {key} found at {result} ")   
else:
    print(f"\n ")    
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid  
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
            
    return -1


