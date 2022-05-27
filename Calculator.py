def add(a,b):
    answer = a+b
    return answer

def subtract(a,b):
    answer = a-b
    return answer

def multiply(a,b):
    answer = a*b
    return answer

def divide(a,b):
    answer = a/b
    return answer

def modulus(a,b):
    answer = a%b
    return answer

def exponent(a,b):
    answer = a**b
    return answer

def int_divide(a,b):
    answer = a//b
    return answer

def square(a):
    answer = a*a
    return answer

def cube(a):
    answer = a**3
    return answer

def factorial(num):
    factorio = 1
    for nums in range(1, num+1):
        factorio*=nums
    return factorio
    