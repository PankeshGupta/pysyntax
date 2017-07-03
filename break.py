import random
secret = random.randrange(1,10)
while True:
   number = int(input("Please guess a no. between 5-10 \n"))
   if number==secret:
       break
print("Finally found out the secret no. {}".format(secret))    
