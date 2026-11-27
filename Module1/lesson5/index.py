# CONDITIONAL STATEMENTS are called decision making  statements.  The program runs certain code only when the condition is true
# CONDITIONAL STATEMENTS : if, if-else, if elif else
# if statement runs a block of code only if the condition is true, if the condition is false it skips the block
# if else statement gives us two parts one for the condition is true and other for whent it is false
# if elif else when you have 2 or more options we use if elif else
# indentation tells python which line belongs together
# example: 
#if 5<2:
    #print("5 is greater than 2")    
#activity 1
a=int(input("enter a number "))
if a>0:
    print(a," is positive ")
# activity 2
#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?
cp=int(input("enter the cost price "))
sp= int(input("enter the selling price "))
if sp>cp:
    print("total profit", sp-cp ) 
else :
    print("no profit ")
# activity 4
#Write a program to check whether the given number is even or odd?
x=int(input("enter a number "))
if x%2==0:
    print(x,"is even ")
else:
    print(x,"is odd")