mystring = "hello my programAEIOU"

#to test in 
ch = 'g'
if ch in mystring:
    print("yes im im")




owelstring="aeiouAEIOU"
count = 0
for owelstr in mystring:
    if owelstr in owelstring:
        count= count+1

print(f"Total count {count} ")
