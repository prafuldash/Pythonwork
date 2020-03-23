while True:

 try:
    number = int(input("Please enter a number :"))
#print(number)
    break

 except ValueError:
    print("you didnt enter a number")
 except:
    print("An Unknown Error Occured")
print("Thank you for entering a number")

secret_number = 7
while True:
   guess = int(input("Guess a number between 1 and 10 :"))
   if guess == secret_number:
      print("you guessed it ")
      break
   else:
      print("Out of scope")
      break
