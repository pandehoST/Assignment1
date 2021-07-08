seq = [2, 3, 4, 5, 12, 15, 20, 24, 25, 30, 40, 60]
z = 30
count = 0

# use anonymous function to filter
for i in seq:
    if z % i == 0:
        print("X=", i, ", Y=", z, ", Z=", z)
        count += 1
"""    else:
        print("X=not found, Y=not found, Z=not found")
        break"""

print()
print("Total match is ", count, ".")



