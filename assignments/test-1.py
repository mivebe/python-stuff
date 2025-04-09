

# def test(i,j):
#     if(i==0):
#         return j
#     else:
#         return test(i-1,i+j)
 
# print(test(5,2))

# ------

def fun(n):
    if (n > 100):
       return n - 5
    return fun(fun(n+11));

print(fun(42))