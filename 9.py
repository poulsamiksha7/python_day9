# #Q1  Fibonacci using recursion

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print("Fibonacci Series")

# for i in range(10):
#     print("Fibonacci Series",fibonacci(i))

# #Q2  Sum of N natural numbers
# def sum_total(n):
#     total=0
#     for i in range(1,n+1):
#         total+=i
#     return total
# n=10
# print("Sum of ", n, "Numbers is", sum_total(n))       
# #Q3 Factorial via recursion

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# num=5
# print("The Factorial of ", num , "is", factorial(num))    

# #Q4  GCD using recursion
# def gcd(a,b):
#     if b==0:
#      return a
#     else:
#        return gcd(b, a%b)
    
# num1 = 60
# num2 = 48

# print("The GCD of ", num1,"and ",num2, "is", gcd(num1,num2))

#Q5 - Power of a number
# def power(base,exponent):
#     return(base**exponent)

# # print(power(2,3))

#Q6  List flatten using recursion
# def flatten_list(nested_list):
#     flat_list=[]
#     for item in nested_list:
#          if isinstance(item,list):
#           flat_list.extend(item)
#          else:
#              flat_list.append(item)
#     return flat_list  

# lst=[1,[1,2],[3,4],5]

# print("The list flatten using recursion", flatten_list(lst))

##Q7 Binary to decimal using recursion
# def binary_to_decimal(binary_str):
#   if binary_str=='':
#     return 0
#   else:
#     return int(binary_str[0]) * (2 ** (len(binary_str) - 1)) + binary_to_decimal(binary_str[1:])
  
# binary="1011"
# decimal=binary_to_decimal(binary)
# print("The binary ", binary,"to decimal is",binary_to_decimal(binary) )  

##Q8  Nested function example
def greet(name):
    def format_name(n):      # 👈 nested function
        return n.capitalize()
    
    formatted = format_name(name)
    return "Hello, " + formatted + "!"

# Call the outer function
print(greet("samiksha"))





        