import matplotlib.pyplot as plt
import random as r 
usn=["1","2","3","4","5"]
marks=[]
for i in range(len(usn)):
    marks.append(r.randint(0,101))
plt.xlabel=("student")
plt.ylabel=("marks")
plt.title=("class record")
plt.plot(usn,marks,color='green',linestyle='solid',marker='o',markerfacecolor='red',markersize=15)
plt.show()
