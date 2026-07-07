#dictionary example

dicEmp = {
    "emp1" : "manager",
    "emp2" : "developer",
    "emp3" : "tester"
}

print(f"all emps frmo dic are {dicEmp}")

#Insert #this will careate new dic and displays only one item
dicEmp = {"emp4" : "teamlead"}
print(f"all emps frmo dic are {dicEmp}")


#Insert
dicEmp["emp1"] = "manager"
print(f"all emps frmo dic are {dicEmp}")

#modify
dicEmp["emp4"] = "srmanager"
print(f"all emps frmo dic are {dicEmp}")

#access values
print(f"all emps frmo dic are {dicEmp['emp4']}")

#delete using pop
print(f"all emps frmo dic are {dicEmp}")
print("after deleting")
dicEmp.pop("emp4")
print(f"all emps frmo dic are {dicEmp}")

#delete using del
dicEmp = {
    "emp1" : "manager",
    "emp2" : "developer",
    "emp3" : "tester"
}
print("before deleting")
print(f"all emps frmo dic are {dicEmp}")
del dicEmp["emp2"]
print("after deleting")
print(f"all emps frmo dic are {dicEmp}")

#loop through
dicEmp = {
    "emp1" : "manager",
    "emp2" : "developer",
    "emp3" : "tester"
}
for key,value in dicEmp.items():
    print(key, ":", value )

#get value
print(f"getting value  :{ dicEmp.get("emp1")} ")     

#clear dic
print(f"before clear   : {dicEmp}")
dicEmp.clear()
print(f"after clear  : {dicEmp} ")



