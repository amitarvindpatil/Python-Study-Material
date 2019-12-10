# Filter
# -----The filter() method filters the given sequence with the help
#       of a function that tests each element in the sequence to be true or not.

# Example


# def check_even(num):
#     return num % 2 == 0


# num = [0, 3, 2, 4, 5, 2, 6, 7, 34, 23, 5, 78, 32, 2, 1, 1, 0]
# filter_even = filter(check_even, num)
# print(list(filter_even))

# Example 2


def vovels(letters):
    vows = ['e', 'a', 'i', 'o', 'u']
    for v in vows:
        print(v)
        if letters[0] == v:
            return True
        else:
            return False


letters = ["amit", "patil", "iskon", "ervind"]
filter_vovels = filter(vovels, letters)
print(list(filter_vovels))
