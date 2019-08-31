from __future__ import print_function
# Initialization of 2D Array
timetable = [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], 
             ["X", "X", "X", "X", "X", "X", "X", "210CT", "210CT", "210CT"], 
             ["220CT", "220CT", "260CT", "260CT", "X", "X", "X", "X", "X", "X"], 
             ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], 
             ["220CT", "220CT", "X", "X", "210CT", "X", "X", "A202SGI", "A202SGI", "X"]] 

# Print out timetable
for x in range(5):
    for y in range(10):
        print(timetable[x][y], end = "\t")
    print("\n")
print("\n-----------------------------------------\n")

# a) List out all the subjects in Wednesday.
print("Subjects in Wednesday: ")
#print(timetable[2][0:10]) 
temp = ""
for x in range(10):
    if timetable[2][x] != "X" and temp != timetable[2][x]:
        print(timetable[2][x])
        temp = timetable[2][x]
print("\n-----------------------------------------\n")


#  b) Count how many hours of classes do you need to attend on Friday.
hours = 0
print("Hours of classes on Friday: ")
for x in range(10):
    if timetable[4][x] != "X":
        hours += 1
print(hours,'hours')
print("\n-----------------------------------------\n")

# c) Determine whether you have any class on Monday.
print("Classes on Monday: ")
classMon = 0
for x in range(10):
    if timetable[0][x] != "X":
        classMon += 1
print(classMon,'classes')
print("\n-----------------------------------------\n")

