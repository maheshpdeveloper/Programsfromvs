#1. Convert List to Tuple
mylist = {1,4,8,90}
print(f'my list - {mylist}')
#convert list to tuple
mytuple = tuple(mylist)
print(f'my tuple - {mytuple}')

#2. Find Sum of Elements in a Tuple
print(f'sun of the elemnts in tuple -- { sum(mytuple)}')

#3. Find Maximum and Minimum in List
print(f'min value and max value from list -- {min(mylist)} and {max(mylist)}' )

#4. Count Occurrences in Tuple
mytuple1 = (4,7,89,2,4,8,34,)
print(f'occurance of the elements { mytuple1.count(4)}')

#5. Remove Duplicates from List
#we can use set and remove duplicates
listm = [2,3,7,90,2,3,6]
newlist = []
for elm in listm:
    if elm not in newlist:
        newlist.append(elm)
print(f'new list  { newlist}')


#6. Reverse a Tuple
revtuple = (3,7,90,123,6)
print(f'actual tuple {revtuple}')

negvar = -1
for i in revtuple:
    print (revtuple[negvar])
    negvar = negvar -1

#second way using slicing..need to learn slicing
print(revtuple[::-1])


#7. Check if Element Exists in Tuple
revtuple1 = (3,7,90,123,6)
myinput = 3
if myinput in revtuple1:
    print('exits')
    
else:
    print('not exits')
    

#8. Merge Two Lists into Tuple
list1 = [1,7,9]
list2 = [123,78,45]
#merging
newtuple = (list1 + list2)
print(f'new merged tuple { newtuple}')

#9. Find Second Largest Number in List
list3 = [122,123,78,45,2,4,7,8]
list3 = list(set(list3)) #remove duplicates
list3.sort()
print(f'second max value { list3[-2]}')



#10. Swap First and Last Element in List
list4 = [122,123,78,45,2,4,7,8]
list4[-1],list4[0] = list4[0],list4[-1]
print(f'new after swap list -- {list4}')

#13. Find Common Elements in Two Lists
list5 = [122,123,78,45,2,4,7,8]
list6 = [7,1233,4,7]
common = []
for i in list5:
    if i in list6:
        common.append(i)
print(common)