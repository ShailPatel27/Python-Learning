'''

*****
 ***
  *

'''

def star(n):
    if(n == 0):
        return
    else:
        print("*" * n)
    star(n-1)
    
n = int(input("Enter a number: "))
star(n)    