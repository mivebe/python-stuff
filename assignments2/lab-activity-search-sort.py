# Зад. 1 Дадено е цяло положително число N, 1<N<20 и последователност от N различни цели положителни числа, не по-големи от 1000. Напишете програма sort, която подрежда числата в нарастващ ред на сбора на цифрите им, с които са представени в десетичната бройна система. Ако две числа имат равен сбор на десетичните си цифри, по-напред в подреждането да бъде поставено това от двете числа, което е по-малко. На първия ред на стандартния вход ще бъде зададен броят N на числата, а на следващите редове – N-те числа. На стандартния изход програмата трябва да изведе подредените според изискванията числа.
# Примерен вход:
# 5
# 203 189 41 900 666
# Примерен изход:
# 41 203 900 189 666

n = int(input())
if n < 1 or n >= 20:
    print("Error: N must be between 1 and 20")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != n:
    print("Error: Numbers must be as many as previously specified")
    exit()

def digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# Sort by digit sum, then by value if digit sums are equal
for i in range(n - 1):
    for j in range(n - i - 1):
        sum_j = digit_sum(numbers[j])
        sum_j1 = digit_sum(numbers[j + 1])
        if sum_j > sum_j1 or (sum_j == sum_j1 and numbers[j] > numbers[j + 1]):
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(" ".join(map(str, numbers)))

# Зад. 2. Дадено е множество A от n дробни числа, n<=1000 и множество B от m дробни числа, n<=100000. Да се състави програма, която определя колко от числата в първото множество се срещат и във второто. На първия ред на стандартния вход ще бъде зададен броят n на елементите на първото множество, на следващите n реда n-те дробни числа на това множество. На следващия ред ще бъде зададен броят m на числата във второто множество, а след това– m-те дробни числа на множеството, всяко на нов ред. На първия ред програмата трябва да изведе броя k на първото множество, които се срещат във второто, а на следващите редове самите k числа. Ако нито един от елементите на първото множество не се среща във второто, тогава програмата трябва да изведе ж на стандартния изход само един ред, съдържащ числото 0.
# Примерен вход:
# 3
# 2.5 4 8
# 6
# 4 9 10 3.5 6 1
# Примерен изход:
# 1
# 4

# Примерен вход:
# 3
# 2.5 4 8
# 6
# 15 9 10 3.5 6 1
# Примерен изход:
# 0

n = int(input())
set_a = list(map(float, input().split()))

m = int(input())
set_b = list(map(float, input().split()))

# Sort set B for binary search
set_b.sort()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

found = []
for num in set_a:
    if binary_search(set_b, num):
        found.append(num)

if len(found) == 0:
    print(0)
else:
    print(len(found))
    for num in found:
        if num == int(num):
            print(int(num))
        else:
            print(num)

# Зад. 3 (С.Р. след лекцията за string) Някога питали ли сте се какво става с едно число, ако постоянно дописваме по една нула зад него? Например, ако вземем числото 1 и допишем 0 зад него, се получава числото 10. Ако допишем още една нула зад него, се получава числото 100 и т.н., докато се уморим да дописваме нули или ни сворши мястото на листчето, на което си записваме това число. Това, разбира се, е скучна работа. Затова да направим нещо по-интересно. Започвайки с 1, да запишем всяко следва-що число, което се получава с дописване на 0, зад числата, които вече имаме. Така ще получим една много дълга редица от цифри, записани една след друга, броят на които ще искаме да не надминава 65000: 1101001000100001000001000000... Напишете програма NRED, която по зададено N намира N-тата цифра на числото, броено от ляво надясно.
# На пырвия ред на стандартния вход ще бъде зададено цялого положително число N, N ≤ 65000. На единствения ред на стандартния изход програмата трябва да изведе N-тата цифра на получената редица.
# Примерен вход:
# 2
# 5
# Примерен изход:
# 1
# 0

n = int(input())
if n > 65000:
    print("Error: N must be <= 65000")
    exit()

# Build the sequence: 1, 10, 100, 1000, ...
# Concatenated: 1101001000100001000001000000...
sequence = ""
zeros = 0
while len(sequence) < n:
    sequence += "1" + "0" * zeros
    zeros += 1

print(sequence[n - 1])

# Зад. 4 Кодирано съобщение се състои от числа, всяко от които се среша точно К пьти. При предаване на съобщението, в него често по-падат и други числа, които не са част от оригиналното съобщение и са излишни. Те се срещат по-малко от К пти. Напишете програма EXCESS, която намира броя на излишните числа в дадено съобщение. На първите два реда на стандарния вход са зададени две цели числа: броят N на числата в полученого съобщение и броят К на повторението на числата в коректното съобщение. На следващите редове са зададени получените N числа, които са цели, положителни и не по-големи от 100000. На стандартния изход програмата трябва да изведе едно цяло число - броя на излишните числа в съобщението. Ограничения: 1 ≤ N ≤ 100000, 2 ≤ K ≤ 1000.
# Примерен вход:
# 10 3
# 7 10 7 4 2 2 4 7 10 4
# Забележка: Излишните числа са 10 и 2.
# Примерен изход:
# 2

first_line = list(map(int, input().split()))
n = first_line[0]
k = first_line[1]

numbers = list(map(int, input().split()))

# Count occurrences of each number
counts = {}
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

# Count how many unique numbers appear less than K times
excess_count = 0
for num in counts:
    if counts[num] < k:
        excess_count += 1

print(excess_count)

# Зад. 5 Да се засече времето на различните сортировки с различен брой елементи и да се нанесат в таблица. Еко код за засичане, в който само да се смени сортировката и броят на елементите, с които да се запълни масива. 
# import random
# import time
# # 1. Генерира се масив от случайни числа
# N = 10000  # размер на масива (можеш да го променяш)
# arr = [random.randint(1, 100000) for _ in range(N)]
# # 2. Копира се масива, за да не се променя оригинала
# data = arr.copy()
# # 3. Засича се време преди сортиране
# start_time = time.time()
# # =======================
# # Тук се поставя алгоритъм за сортиране
# # Пример: Bubble Sort
# for i in range(len(data)):
#     for j in range(len(data) - i - 1):
#         if data[j] > data[j + 1]:
#             data[j], data[j + 1] = data[j + 1], data[j]
# # =======================
# # 4. Засичаме време след сортиране
# end_time = time.time()
# # 5. Извеждаме резултатите
# print(f"Първите 20 числа след сортиране: {data[:20]}")
# print(f"Време за сортиране: {end_time - start_time:.6f} секунди")

# Сортировка	1000 елементи	10000000 елементи
# <сортировка1>	<време за сортиране>	< време за сортиране>
# <сортировка2>	<време за сортиране>	< време за сортиране>
# <сортировка3>	<време за сортиране>	< време за сортиране>
# ...	...	...

import random
import time

def bubble_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def selection_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def insertion_sort(arr):
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def quick_sort(arr):
    data = arr.copy()
    def partition(low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

    def quick_sort_helper(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_helper(low, pi - 1)
            quick_sort_helper(pi + 1, high)

    quick_sort_helper(0, len(data) - 1)
    return data

def merge_sort(arr):
    data = arr.copy()
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def benchmark_sort(sort_func, arr):
    start = time.time()
    sort_func(arr)
    end = time.time()
    return end - start

# Test with different array sizes
sizes = [1000, 10000]
algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Quick Sort", quick_sort),
    ("Merge Sort", merge_sort),
]

print(f"{'Сортировка':<20}", end="")
for size in sizes:
    print(f"{size} елементи".ljust(20), end="")
print()

for name, func in algorithms:
    print(f"{name:<20}", end="")
    for size in sizes:
        arr = [random.randint(1, 100000) for _ in range(size)]
        time_taken = benchmark_sort(func, arr)
        print(f"{time_taken:.6f} сек".ljust(20), end="")
    print()
