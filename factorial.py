# num = int(input("Enter a number whose factorial you want to remove: "))
# num1 = num
# while num > 0:
#     if num < 1:
#         print(num,"is the factorial of",num1)
#     else:
#         num = num1 * num
#         num1-=1
# else:
#     print("Enter a number greater than 0")
    

def fact(n):
    if n==0 or n ==1:
        return 1
    else:
        return n*fact(n-1)
    
factorial = fact(5)
print(factorial)