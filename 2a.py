def fn(n):
    if n==1:
        return 0;
    elif n==2:
        return 1;
    else:
        return fn(n-1)+fn(n-2)

num=int(input("enter the number: "))
if num>0:
    result=fn(num)
    print("fn(",num,") is ",result)
else:
    print("error in input")
