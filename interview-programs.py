# Prgrams
# ===================
# 1.Fibbonacci series
# --------------------------------------------
def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1)+fib(n-2))

n = 10
if n <= 0 :
    print("No shold be positive")
else:    
    for i in range(n):
        print(fib(i))

f1 = 0 
f2 = 1
cnt = 0
while(cnt < 10):
    print(f1)
    tmp = f1+f2
    f1 = f2
    f2 = tmp
    cnt += 1        
# =============================================		
# 2. prime no
# ---------------------------------------------
for num in range(10,50):
    if num > 1:
        for j in range(2,num):
            if (num % j) == 0:
                break
        else:
            print(num)
# ==============================================        

# 3. palindrom
# ----------------------------------------------
ip = "MADAM"

if ip == ip[::-1] :
    print("Palindrome")
else:
    print("Not Palindrome")

# ==============================================	
# 4. Matrix
# ----------------------------------------------
matrix = []
for i in range(2):
    a = []
    for j in range(3):
        a.append(int(input()))
    matrix.append(a)

for i in range(2):
    for j in range(3):
        print(matrix[i][j], end =" ")
    print()
# =============================================	
# 5. Patterns
# 6. array sort 
# ---------------------------------------------
ip = [32,5,3,6,7,54,87]
data = len(ip) - 1

for i in range(data):
    for j in range(data-1):
        if ip[j] > ip[j+1]:
            tmp = ip[j]
            ip[j] = ip[j+1]
            ip[j+1] = tmp
print(ip)
# ==============================================
# 7. Count of Duplicate character in string
# ----------------------------------------------
ip = 'oo mmaaa toollula'
op = {}
for i in ip:
    op[i] = ip.count(i) 

print(op)   
# ==============================================
# 8. Remove Duplicate character from string
# ----------------------------------------------
ip = 'oo mmaaa toollula'
sets = set()
print(sets)
op = []
for i in ip:
    if i not in sets:
       sets.add(i)
       op.append(i)
output = "".join(op)
print(output)       
# ================================================
# 9. GCD of array and 2 no.series
# -----------------------------------------------
x = 54
y = 24

for i in range(1,10):
    if x % i == 0 and y % i == 0:
        gcd = i
print(gcd)        

# ======
# Array
# ======
def find_gcd(x,y):
    x,y = y,x%y
    return x

l = [50,20,30,40]
num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1,num2)

for i in range(len(l)):
    gcd = find_gcd(gcd,l[i])
print(gcd)    
  
# =========================================================
# 10. Smallest value and highest value without any function
# ---------------------------------------------------------
ip = [32,5,3,6,7,54,87]
length = len(ip) - 1
for i in range(length):
    for j in range(length-1):
        if ip[j] >= ip[j+1]:
            tmp = ip[j]
            ip[j] = ip[j+1]
            ip[j+1] = tmp
print("min value",ip[0])
print("maxmium value",ip[-1])
# ==========================================================
# 12, Reserve a sentence 
# ----------------------------------------------------------
ip = "Hello world"
op = []
lst = ip.split()
output = lst[::-1]
result = ' '.join(output)
print(result)

# ============================================================
# 13 Maintain the sentence but, reverse each word
# --------------------------------------------------
ip = "Hello world"
print(ip[::-1])
# ==================================================

# 14 sort dict by values
# =========================================
d = {'a':4,'b':5,'c':1}
op = {}
for w in sorted(d, key=d.get, reverse=True):
    op[w] = d[w]
print(op)

	
# 15 Factorial number
# ===========================================
num = 5
fact = 1
if num < 0 :
    print("Number should be positive")
elif num == 0:
    print("0 factorial num is 1")
else:
    for i in range(1,num+1):
        fact = fact * i
    print("The factorial of",num,'is:-',fact)


# Non Duplicate element between 2 list 
l1 = [1,2,3,4,5,6]
l2 = [1,2,3,7]
op1 = []
l1.extend(l2)


for i in l1:
    if l1.count(i) < 2: 
        op1.append(i)
print(op1)


# 
data = "!*"
ops = "i am checking this string to see how many times each character appears I!*"


datas =  ops.replace(data,'')
print(datas)

ips = ops.lower()
check_string = ips.split()

count = {}
for s in check_string:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

print(count)

#  Divide string into N parts

s = 'AABCAAADA'

s_len = len(s)
part = int(s_len / 3)
k = []

for i in range(0,s_len,part):
    data = s[i:i+part]
    k.append(data)

print(k)

# Merge the Tools!

for i in zip(*[iter(s)]*n):
    print(i)
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in i if c not in d ]))
