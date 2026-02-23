# 1 + 2 + 3 + 4 + 5 + ... + n
n = 10
output = 0
for i in range(n):
    output = output + i
print("Sum series output",output)     

# (1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n)

n = 3
out = 0
for i in range(n+1):
    output = i * i
    out = out + output
print("Multiple series output",out)    

#  (1) + (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n)
n = 5
output = 0
for i in range(1,n+1):

    out = i*(i+1)/2
    output = output + out
print("Output of series",output)

# 1! + 2! + 3! + 4! + 5! + ... + n!
# 1 + 2 + 6 + 24 +

n = 4
factorial = 1
output = 0
for i in range(1,n+1):
    factorial = factorial * i
    output = output + factorial
print(output)

# (1^1) + (2^2) + (3^3) + (4^4) + (5^5) + ... + (n^n)
n = 5 
output = 0
for i in range(1,n+1):
    power = i * i
    output = output + power
print(output)

# (1!/1) + (2!/2) + (3!/3) + (4!/4) + (5!/5) + ... + (n!/n)

n = 5 
factorial = 1
output = 0
sums = 0
for i in range(1,n+1): 
    factorial = (factorial * i)
    output = factorial/i
    sums = sums + output
print(sums)    

# [(1^1)/1] + [(2^2)/2] + [(3^3)/3] + [(4^4)/4] + [(5^5)/5] + ... + [(n^n)/n]
n = 5 
output = 0
sums = 0
for i in range(1,n+1):
    power = i * i
    output = power / i
    sums = sums + output
print(sums)
