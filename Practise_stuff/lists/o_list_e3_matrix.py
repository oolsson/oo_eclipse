'''
Created on Dec 26, 2011

@author: oo
'''
M=[[1,2,3],
   [4,5,6],
   [7,8,9]]

print M
print M[1]
print M[1][2]

col2 = [[column[2]] for column in M]
print col2

col2=[row[0] for row in M] #creates a coloumn vector of row value '0' in each row
print col2

col2=[col[2] for col in M] #creates a coloumn vector of row value '0' in each row
print col2
print '--------------------------'
col2=[row[0] + 11 for row in M] #qdds 11 to each of the values in the coloumn
print col2

col2=[row[0] for row in M if row[1] % 2 == 0] #filters out odd numbers from coloumn
print col2

diag = [M[i][i] for i in [0, 1, 2]]
print diag

doubles = [c * 2 for c in 'spam']
print doubles

s1=list(map(sum, M))
print s1

s1=map(sum, M)
print s1

s1={i : sum(M[i]) for i in range(3)}
print s1