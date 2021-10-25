def isPythagoras(a, b, c):
    if(c**2 == (a**2 + b**2)):
        return True
    else:
        return False


print(isPythagoras(3, 4, 5))
print(isPythagoras(5, 9, 12))
print(isPythagoras(8, 6, 10))
print(isPythagoras(7, 8, 11))
