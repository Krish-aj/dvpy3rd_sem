def compare(s1,s2):
    count=0
    n=min(len(s1),len(s2))
    for i in range(n):
        if(s1[i]==s2[i]):
            count+=1;
    return count
    
s1=input("enter string 1: ")
s2=input("enter string 2: ")
count=compare(s1,s2)
mx=max(len(s1),len(s2))
match=count/mx*100
print("letters match is: ",count)
print("match percent: ",match)
