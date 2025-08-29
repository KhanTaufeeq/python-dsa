# delete all consonants 

# def del_consonants(data = 'Python and Data Science'):

#     vowels = 'aeiouAEIOU'

#     vowel_str = ''.join([char for char in data if char in vowels or not char.isalpha()])

#     return vowel_str 

# print(del_consonants())                                                                                                                                                               

print(list(range(2,2)))

# find the sum of all prime numbers from 1 to N 

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False 
    return True



print(is_prime(2))

def sum_n_prime(number):

    total = 0

    for i in range(1, number+1):
        if is_prime(i):
            total += i
        else:
            continue
    return total 

print(sum_n_prime(20))

# print(list(range(2,1)))
