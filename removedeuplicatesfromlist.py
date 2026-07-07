#create list first

"""
one
two
"""
listofitems = [1,34,8,90,45,4,8,1,1,1,1]


'''
four
three
'''

#first way
def removeDuplicates(listofitemss):
    return list(set(listofitems))

mylist = removeDuplicates(listofitems)
print(mylist)

print("===========================================")
#secondway
