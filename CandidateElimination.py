import csv
a = []
with open('jap.csv', 'r') as trainData:
    for row in csv.reader(trainData):
        a.append (row)
        print(row)
n= len(a[0])-1 

print("\n The initial value of hypothesis: ")
S = ['0'] * n
G = ['?'] * n
print ("\n The most specific hypothesis S0 :",S)
print (" \n The most general hypothesis G0 :",G)

S=a[0][:-1]
print("\n Candidate Elimination algorithm\n")
temp=[]

for i in range(len(a)):
    if a[i][n]=='yes':
        for j in range(n):
            if a[i][j]!=S[j]:
                S[j]='?'

        for j in range(n):
            for k  in range(len(temp)):
                if temp[k][j] != '?' and temp[k][j] != S[j]:
                    del temp[k] 
    
    if a[i][n]=='no': 
        for j in range(n):
             if S[j] != a[i][j] and S[j]!= '?': 
                 G[j]=S[j]
                 temp.append(G) 
                 G = ['?'] * n

    print("\n For Training Example No :{0} the hypothesis is S{0} ".format(i+1),S)
    if (len(temp)==0):
            print(" For Training Example No :{0} the hypothesis is G{0} ".format(i+1),G)
    else:
            print(" For Training Example No :{0} the hypothesis is G{0}".format(i+1),temp)
       