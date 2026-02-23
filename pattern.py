# Patterns
# # # # 
# # # # 
# # # # 
# # # #
for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()

'''
*  
*  *  
*  *  *
*  *  *  *
'''

for i in range(4):
    for j in range(i+1):
        print("* ",end=" ")
    print()

'''
*  *  *  *  
*  *  *  
*  *     
*   
'''
n = 4
for i in range(n):
    for j in range(n-i):
        print("* ",end=" ")
    print()    
'''
    *
   **
  ***
 ****
*****  
'''  
n = 6
for i in range(1,n):
    for k in range(1,n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

'''
*****
 ****
  ***
   **
    * 
'''
n = 6
for i in range(5,0,-1):
    for k in range(1,n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

'''
    *
   ***
  *****
 *******
*********  
'''
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,(2*i-1)+1):
        print("*",end="")
    print()        

'''
*********
 *******
  *****
   ***
    *
'''
for i in range(5,0,-1):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,(2*i-1)+1):
        print("*",end="")
    print()

'''
*  *  *  *  
*  *  *  
*  *
*
*
*  *
*  *  *
*  *  *  *
'''
n = 4
for i in range(n):
    for j in range(n-i):
        print("* ",end=" ")
    print()   
n = 4
for i in range(n):
    for j in range(i+1):
        print("* ",end=" ")
    print()  

'''
*****
 ****
  ***
   **
    *
    *
   **
  ***
 ****
*****
'''
n = 6
for i in range(5,0,-1):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()             
