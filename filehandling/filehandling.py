# File Handling Mean create,append,read,write the file
# "r" -> Read
# "x" -> create
# "a" -> append
# "w" -> write

# create a file
# f = open("myfile.txt","x")

# write a file
import os
f = open("myfile.txt", 'a')
f.write("Now the file has more contentssssssssssssssssss!")
f.close()

# read data of the file
f = open("myfile.txt", 'r')
print(f.read())


f = open("myfile.txt", 'w')
f.write("Now the file has more asdasd!")
f.close()

# read data of the file
f = open("myfile.txt", 'r')
print(f.read())


# Delete file
# import os
f.close()
os.remove("myfile.txt")

# check if file exists
if os.path.exists("myfils.txt"):
    os.remove("myfils.txt")
else:
    print("file not found")
