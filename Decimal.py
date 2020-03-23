 ####Decimal Module
#from Decimal import decimal as D
import string


from pylint import epylint as lint
(pylint_stdout, pylint_stderr) = lint.py_run('module_name.py', return_std=True)

"""
sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")
"""

print(type(3))
print(type(3.15))
print(type("3"))
print(type('3'))

samp_string = "This is a avery important String"
print(samp_string[0])
print(samp_string[-1])
print(samp_string[3+5])
print("Length :", len(samp_string))
print(samp_string[8:])
print(samp_string[0:4])
print("Hello PRAFUL " * 5)
num_string = str(5)
for char in samp_string:
    print(char)

#printing pair string
    for i in range(0,len(samp_string)-1,3):
        print(samp_string[i] + samp_string[i+1])


samp_string = "This is very Important String"
#A -Z - 90
#a - z -122
print("A= ", ord("A"))
print("65= ", chr(65))

rand_string = "            This is my Love Dearling"
rand_string = rand_string.lstrip()
rand_string = rand_string.rstrip()
rand_string = rand_string.strip()
print(rand_string.capitalize())
print(rand_string.lower())
print(rand_string.upper())
a_list= ["bunch","of","Random","Words"]
print(" ".join(a_list))

a_list_2 = rand_string.split()
for i in a_list_2:
    print(i)


## NEED TO CHECK
print("How many is :",rand_string.count("is"))
print("where is string :",rand_string.find("string"))
print(rand_string.replace("an","a kind of"))

#Random  Access Memory : RAM
#Ask for a String
orig_string = input("Convert it to  Accronym : ")
#Convert the string to uppercase
orig_string = orig_string.upper()
#Convert the string into a list
list_of_words= orig_string.split()

#Cycle through the list
for word in list_of_words:
    
#Get the list letter of the word and eliminate the newline
   print(word[0],end="")
# Add a newline

print()


letter_z = "Z"
num_3 = "3"
a_space = " "
print("Is z a letter or number :" ,letter_z.isalnum())
print("Is z a letter  :" ,letter_z.isalpha())
print("Is 3  :" ,num_3.isdigit())
print("Is z a letter  :" ,letter_z.islower())
print("Is z a upper  :" ,letter_z.isupper())
print("Is space is Space  :" ,a_space.isspace())

