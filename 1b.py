val=int(input("enter a number: "))
string=str(val)
if string==string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

for i in range(10):
    if string.count(str(i))>0:
        print(str(i),"appeared",string.count(str(i)),"times")
