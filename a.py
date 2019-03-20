
import math

prime_numbers = [2, 3, 5, 7, 11, 13] 	#since the input no. should not be divisible by prime numbers other than 13.


n = int(input())				#input number


dividors_prime = []

for prime in prime_numbers:						#this loop is used to check if the input is divisible by prime in prime_numbers if the results is 0 then add it to the list of divisior_prime
    if n % prime == 0:					#if the number get perfectly divisible then add to the list
        dividors_prime.append(prime)


answer = 0				#inclusion-exclusion method is used after that
for i in range(1, pow(2, len(dividors_prime))):			#taking a variable i from 1 to the power of 2, where the power of 2 is the total divisor_prime numbers present in the list
    k = i				#i is assign to k as to remove the errors facing in the loop
    result = 1			#taken a variable to store the divisibility of the number
    token = 0			#storing the temporary number
    count_of_ones = 0	#storing the 1 which will comes out through division of the number
    while k > 0:				#while condition is used for the number greater than 0 due to positive integer
        if (k % 2 == 1):		#we know that multiplicative inverse follows when there is 1 as mod of no.
            result = result * dividors_prime[token]
            count_of_ones += 1	#now adding 1 everytime when the loop move forward
        token += 1				#while token also add 1 value
        k = int(k / 2)			#As the modulas of 2 is 1, so dividing all th number with 2 reduced th number by half

    if count_of_ones % 2 == 0:		# the if-else loop check the modularity of the one stored during the while loop
        answer -= (n / result)		#divisibility of the number with the input is the part of general form in inclusion-exclusion principle
    else:
        answer += (n / result)


print (int (n - answer))			#At last subtract the anser from the input to get all the multiplicative inverse.