# def odds(start=1):
#   ''' return all odd numbers from start upwards'''
#   if int(start) % 2 == 0: start = int(start) + 1
#   while True:
#     yield start
#     start += 2

# with open("odds.txt", "w") as file:
#   for n in odds(2):
#     if n > 10: break
#     else: file.write(f"{n}\n")

# ------

def f(x):
    def f1(a, b):
        print("hello")
        if b==0:
            print("NO")
            return
        return f(a, b)
    return f1

@f
def f(a, b):
     return a%b

f(4,0)