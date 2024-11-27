l = [1, 24, 54, 125, 32, 90, 15, 0, 155]

def divisible(n):
    if(n % 5 == 0):
        return True
    return False

print(list(filter(divisible, l)))