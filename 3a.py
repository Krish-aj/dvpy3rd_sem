sentence=input("enter a sentence: ")
wordcnt=digitcnt=upcnt=lowcnt=0
words=sentence.split()

for c in sentence:
    if(c>='0' and c<='9'):
        digitcnt+=1
    if(c>='A' and c<='Z'):
        upcnt+=1
    if(c>='a' and c<='z'):
        lowcnt+=1
print("the sentence has:")
print(f"word:{len(words)}\ndigit:{digitcnt}\nuppercase:{upcnt}\nlowercase:{lowcnt}")
