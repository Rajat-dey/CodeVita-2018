
import math

prime_numbers = [2, 3, 5, 7, 11, 13]


n = int(input())


dividors_prime = []

for prime in prime_numbers:
    if n % prime == 0:
        dividors_prime.append(prime)


answer = 0
for i in range(1, pow(2, len(dividors_prime))):
    k = i
    result = 1
    token = 0
    count_of_ones = 0
    while k > 0:
        if (k % 2 == 1):
            result = result * dividors_prime[token]
            count_of_ones += 1
        token += 1
        k = int(k / 2)

    if count_of_ones % 2 == 0:
        answer -= (n / result)
    else:
        answer += (n / result)


print (min(int (n - answer), n - 1))