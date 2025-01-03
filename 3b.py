str1=input("enter str1: ")
str2=input("enter str2: ")
shortstring=min(len(str1),len(str2))
longstring=max(len(str1),len(str2))
count=0
for i in range(shortstring):
    if(str1[i]==str2[i]):
        count+=1
print("letters matched is :",count)
print("match percent is: ",(count/longstring)*100)
