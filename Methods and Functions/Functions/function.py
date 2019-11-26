# Example 1 Simple interest
def simple_interest(p, n, r):
    SI = (p*n*r)/100
    print("Simple Interest is:", SI)


simple_interest(5000, 5, 20)

# Example 2 with return key
def simple_interests(pr, time, rate):
    SIM = (pr*time*rate)/100
    return SIM
simple_interests(10000, 5, 20)

# prime number
def prime(num):
    for nums in range(2, num):
        if num % nums == 0:
            print(num, "Not prime number")
            break
        else:
            print(num,"prime number")
            break
prime(17)
