print("Hello PRAFUL")

print (4+4)
l = ["word1,word2,word3"]
print(l)

import csv

f = open ("Student.csv")
csv_f = csv.reader(f)
students=[]

for row in csv_f:
    students.append(row[2])
    #f.close()
    print (students)