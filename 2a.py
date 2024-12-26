def fibonacci(n):
    if n==1:
        return 0;
    elif n==2:
        return 1;
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num=int(input("enter the number: "))
if num>0:
    result=fibonacci(num)
    print("fibonacci of ",num," is ",result)
else:
    print("error in input")
