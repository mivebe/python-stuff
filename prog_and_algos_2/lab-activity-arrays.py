# 1 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=400), от втория ред на
# стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата първото
# въведено число, което е по-голямо от 100 или NO, ако няма въведено такова число.

count = int(input())
if count > 400:
    print("Error: number must be <= 400")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

result = "NO"
for i in range(count):
    if numbers[i] > 100:
        result = numbers[i]
        break

print(result)

# 2 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=200), от втория ред на
# стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата първото
# въведено число, което е по-малко от 10 и неговия номер (номерата започват от 1) или NO, ако няма
# въведено такова число.

count = int(input())
if count > 200:
    print("Error: number must be <= 200")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

result = "NO"
for i in range(count):
    if numbers[i] < 10:
        result = f"{numbers[i]} {i+1}"
        break

print(result)

# 3 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=300), от втория ред на
# стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата
# последното въведено число, което има цифра на единиците 5 или NO, ако няма въведено такова число.

count = int(input())
if count > 300:
    print("Error: number must be <= 300")
    exit()
numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

result = 'NO'
for i in range(count):
    if numbers[i] % 10 == 5:
        result = numbers[i]

print(result)

# 4 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=400), от втория ред на
# стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата
# последното въведено число, което е едноцифрено и неговия номер (номерата започват от 1) или NO, ако
# няма въведено такова число

count = int(input())
if count > 400:
    print("Error: number must be <= 400")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

result = "NO"
for i in range(count):
    if -10 < numbers[i] < 10:
        result = f"{numbers[i]} {i+1}"

print(result)

# 5 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=350), от втория ред на
# стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата броя на
# въведените двуцифрени числа, разположени между първото число, което е по-голямо от 100 и последното
# число, което е по-малко от 10 или NO, ако няма въведени числа, по-големи от 100 или числа, по-малки от
# 10.

count = int(input())
if count > 350:
    print("Error: number must be <= 350")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

first_greater_100 = -1
last_less_10 = -1

for i in range(count):
    if numbers[i] > 100 and first_greater_100 == -1:
        first_greater_100 = i
    if numbers[i] < 10:
        last_less_10 = i

if first_greater_100 == -1 or last_less_10 == -1:
    print("NO")
else:
    start = min(first_greater_100, last_less_10)
    end = max(first_greater_100, last_less_10)
    two_digit_count = 0
    for i in range(start + 1, end):
        if 10 <= abs(numbers[i]) <= 99:
            two_digit_count += 1
    print(two_digit_count)

# 6 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=280), от втория ред на
# стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата най-голямото
# число, което е по-малко от 500. Ако няма число, което е по-малко от 500, да се отпечата NO.

count = int(input())
if count > 280:
    print("Error: number must be <= 280")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

result = "NO"
max_val = None
for i in range(count):
    if numbers[i] < 500:
        if max_val is None or numbers[i] > max_val:
            max_val = numbers[i]
            result = max_val

print(result)

# 7 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=400), от втория ред на
# стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата най-малкото
# число, което е по-голямо от 50. Ако няма число, което е по-голямо от 50, да се отпечата NO.

count = int(input())
if count > 400:
    print("Error: number must be <= 400")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

result = "NO"
min_val = None
for i in range(count):
    if numbers[i] > 50:
        if min_val is None or numbers[i] < min_val:
            min_val = numbers[i]
            result = min_val

print(result)

# 8 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=100), от втория ред на
# стандартния вход се въвеждат n на брой числа. На първия ред на стандартния изход да се отпечата
# дължината на най-дългата последователност от едноцифрени числа.

count = int(input())
if count > 100:
    print("Error: number must be <= 100")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

max_length = 0
current_length = 0
for i in range(count):
    if -10 < numbers[i] < 10:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 0

print(max_length)

# 9 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=250) и цяло
# положително едноцифрено число m, от втория ред на стандартния вход се въвеждат n на брой числа. На
# първия ред на стандартния изход да се отпечата дължината на най-дългата последователност от числа,
# чиято цифра на единиците е равна на m.

first_line = list(map(int, input().split()))
count = first_line[0]
m = first_line[1]

if count > 250:
    print("Error: number must be <= 250")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

max_length = 0
current_length = 0
for i in range(count):
    if numbers[i] % 10 == m:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 0

print(max_length)

# 10 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=300), от втория ред
# на стандартния вход се въвеждат n на брой числа. Две числа са „близки", ако са разположени едно след
# друго и първото е по-малко от второто. Например в последователността 6 3 90 100 45 80, „близки" числа са
# 3 и 90, 90 и 100, 45 и 80. На първия ред на стандартния изход да се отпечата броя на „близките" във
# въведената последователност числа.

count = int(input())
if count > 300:
    print("Error: number must be <= 300")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

close_count = 0
for i in range(count - 1):
    if numbers[i] < numbers[i + 1]:
        close_count += 1

print(close_count)

# 11 зад. От първия ред на стандартния вход се въвежда цяло положително число n (n<=300), от втория ред
# на стандартния вход се въвеждат n на брой числа. Три числа са „приятели", ако са разположени едно след
# друго и сумата на първото и третото е равна на второто. Например в последователността 6 96 90 135 45 80,
# „приятели" са числата 6, 96, 90, и 90, 135, 45. На първия ред на стандартния изход да се отпечата броя на
# „приятелите" във въведената последователност числа.

count = int(input())
if count > 300:
    print("Error: number must be <= 300")
    exit()

numbers = list(map(int, input().split()))
if len(numbers) != count:
    print("Error: Numbers must be as many as previously specified")
    exit()

friends_count = 0
for i in range(count - 2):
    if numbers[i] + numbers[i + 2] == numbers[i + 1]:
        friends_count += 1

print(friends_count)
