#Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 552]
primes =[]
not_primes=[]
for index in range(len(numbers)):
    if numbers[index] == 2:
        primes.append(numbers[index])
        continue
    if numbers[index] % 2 == 0:
        primes.append(numbers[index])
        continue
    for N in range(3, int(numbers[index]**0.5)+1, 2):
        if numbers[index] % N == 0:
            primes.append(numbers[index])
            continue
        not_primes.append(numbers[index])
print(primes, not_primes)