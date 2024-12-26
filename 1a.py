m1=int(input("enter marks 1: "))
m2=int(input("enter marks 2: "))
m3=int(input("enter marks 3: "))
l=[]
l.append(m1)
l.append(m2)
l.append(m3)

l.sort()
avgmarks=(l[1]+l[2])/2
print("average of best two marks is: ",avgmarks)
