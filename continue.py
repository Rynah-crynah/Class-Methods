x = 1
y = 20
while x < y:
    x+=1
    if x % 2 != 0:
        continue
    print(x)

# Using while, if and continue statements print all the numbers that are divisible by 5 between 100 and 200     
x = 100
y = 200
while x<y:
    x+=1
    if x % 5 != 0:
        continue
    print(x)