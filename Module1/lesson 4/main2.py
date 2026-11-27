# Operators: they are symbols that perform specific mathematical logical or asssignment operations on values called operands 
#operands : they are the values  or variables on which operators act.
#TYPES OF OPERATORS : ARITHMETIC OPERATORS - they perform mathematical calculations  such as addition, subtraction, multiplication, division and more. (+): add, (-): sub, (*): multiply, (/): divide, (%): modulus (remainder), (**): exponents and (//): floor division (quotient)
# COMPARISON OPERATOR : they compare 2 operands and return either true or false. (==) : equal to , (!=): not equal to , (>): greater than , (<): less than , (>=): greater than equal to, and (<=): less than equal to. they are very useful for making decisions in programs
# ASSIGNMENT OPERATORS : they are used to  assign or update the value of variable  with new values . often used with arithmatic operators.(=) simple assignment, (+=): add and a assignment , we can use the other arithmatic operators to assign and update values according to the arithmetic operatos behaviour. 
# ACTIVITY 1 : There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper. Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?
# solution 1:
tree1=98
tree2=94
tree3=41
tree4=96
tree5=11
sum=tree1+tree2+tree3+tree4+tree5
print("the sum of five trees is",sum)
average=sum/5
print("the average height of a tree is",average)
# ACTIVITY 2: Write a program to calculate the number of notes in the given amount?
amount=int(input("please enter an amount ")) 
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notes of 100 rupee",note1)
print("notes of 50 rupee",note2)
print("notes of 10 rupee",note3)

