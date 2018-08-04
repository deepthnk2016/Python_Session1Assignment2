#-----------------------------------------------------------------
# Python - Session 1 Assignment 2
# Descr - Loop through the numbers from 2000 to 3200 and print
#         those numbers which are divisble by 7 but not by 5
#-----------------------------------------------------------------

# Loop through 2000 to 3200
print("List of Numbers between 2000 & 3200 which are divisible by 7 but not by 5")
for i in range(2000,3200):
    #Check that the number is divisible by 7 but not by 5
    if(i%7==0) and (i%5!=0):
        res=str(i)+','
        print(res,end='') #If satisfies the condition print the number