# program to print no. that are not divisible by 2 or 3 or 5 from 1-40
count = 0
for i in range(2,1000):
    if i%2==0 or i%3 == 0 or i%5 == 0 or i%7==0 :
        continue
    else:

        count+=1
        
print("The no. of such numbers is {}".format(count))
