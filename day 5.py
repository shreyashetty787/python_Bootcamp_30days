# 1create a program of list of  n integer values
n=25
list1=[x for x in range(0,n)]
print("list=\n",list1)

# add an item into the list 
list1.append(454)
print("list after adding an item :\n",list1)


#delete an item
del list1[9]
print("list after deleting:\n",list1)

#largest no of the list
lar=max(list1)
print(" the largest no in the list:",lar)
#smallest no in the list
small=min(list1)
print("the smallest no in the list :",small)

#create a tuple and print reverse of the created tuple
tuple=(45,78,90,67,43,65,12,89)
s=sorted(tuple)
print("tuple before sorting",tuple)
print(" reverse the tuple",sorted(tuple,reverse=True))
print("sorted tuple",s)

#create a tuple  and convert into list
tuple = [(1,2),(3,6),(7,78)]
result=[]
for t in tuple:
    for x in t:
        result.append(x)
print(result)
        
