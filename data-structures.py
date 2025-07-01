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