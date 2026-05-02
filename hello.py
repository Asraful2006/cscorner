#nested loop

for i in range(5):
    sum = 0
    for j in range(1, i+2):
        sum = sum + j
        print(j, end = " ")
    print(" = ", sum)