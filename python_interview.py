#
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=' ')
    print()


for i in range(0, -1):
    for j in range(0, i+1):
        print("*", end=' ')
    print("\r")

# pyramid
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i+1):
        print("* ", end=' ')
    print(" ")

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print('')

for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print('')

last_num = 6

for num in range(1,last_num):
    for i in range(1 , num + 1):
        print(i,end='')
    print('')
