val=int(input("enter a number: "))
str_val=str(val)
if str_val==str_val[::-1]:
    print("palindrome")
else:
    print("not palindrome")

for i in range(10):
    if str_val.count(str(i))>0:
        print(str(i),"appeared",str_val.count(str(i)),"times")
