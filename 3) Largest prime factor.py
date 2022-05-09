'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

z = 600851475143
x = 6
divisor = 1
factor_list = []
prime_factor_list = []

while divisor <= x:
    q = x/divisor
    if q.is_integer():
        factor_list.append(q)
    divisor += 1

n1 = 0
n2 = 1
temp_list = []
divisor = 1

print(factor_list)
n3 = n2-n1
while n3 <= len(factor_list):
    q = factor_list[0]/divisor
    if q.is_integer():
        temp_list.append(q)
    if len(temp_list) == 2:
        prime_factor_list.append(q)
    temp_list.clear()
    n3 = n2-n1
    n1 +=1
    n2 +=1
    divisor +=1

print(factor_list)
print(temp_list)
print(prime_factor_list)

