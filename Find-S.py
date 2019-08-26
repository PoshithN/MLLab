# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 00:17:10 2019

@author: Prajwal Bharadwaj N
"""
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

S= a[0][:-1]
print("\n FIND-S algorithm")

for i in range(len(a)):
    if a[i][n]=='Positive':
        for j in range(n):
            if a[i][j]!=S[j]:
                S[j]='?'
    
    print("\n For Training Example No :{0} the hypothesis is S{0} ".format(i+1),S)
print("\nMaximally Specific Hypothesis of Training set  ",S)
