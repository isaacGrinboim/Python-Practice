def f(m):
    if m == 1:
        return 10
    else:
        return 4 + (2/3)*f(m-1)
    
print("f(900) = ", f(900))


