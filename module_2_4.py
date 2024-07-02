#Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes=[]
for index in range(len(numbers)):
    if numbers[index]<=1:
        continue
    is_prime = True
    for N in range(2, numbers[index]):
        if numbers[index] % N == 0:
            not_primes.append(numbers[index])
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[index])
print("Primes: ", primes)
print("Not Primes: ", not_primes)
