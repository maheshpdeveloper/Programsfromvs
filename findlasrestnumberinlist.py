#create list first

numbers = [15,29,30,4,45,6,787,80]


#with max method we can get the big number
#print(f"largest number",{max(numbers)})


def findlargestnumber(numbers):
    return max(numbers)

maxnumber = findlargestnumber(numbers)
print(f'max number in the list is',maxnumber)
    
temp = 0
#without max function
for num in numbers:
    if num>temp:
        temp = num

    print(f"biggest number{temp}")
 