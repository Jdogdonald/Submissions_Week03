#!/usr/bin/env python
# coding: utf-8

# ## Week 3 Homework
# 
# Write a script to solve each of the following problems. Please create a new Jupyter notebook and save the notebook.  Please upload the notebooks to the GitHub repository in your SUBMISSIONS/week_03 folder.
# 
# Assignment due date: 11:59PM Wednesday.
# 
# Objectives:
# 
#   -Demonstrate how to obtain user input into a Python script
#   -Demonstrate outputting useful information to the user in the correct format
#   -Use Python numerical and string variables to calculate values and output these to user
#   -Demonstrate use of the while loop and if statements

# 
# ### General Guidelines:
# 
# Please format your input and output strings to be user friendly. For tips on how to do this, see the python string formatting cookbook at: https://mkaz.blog/code/python-string-format-cookbook/. For example, in the first problem below, format the tip to two decimal places like 15.25 instead of 15.25000001.
#     
# Limited user input validation and error checking is encouraged on this assignment. Each question below will indicate the type of input that you can expect. (for example, if the question states the input will be an integer you can expect the user to input an integer and do not need to check to ensure it is an integer versus a float or a string)
#     
# Adding comments in your code is strongly suggested but won't be graded.
#     
# The examples given are samples of how we will test/grade your code. Please ensure your scripts output the same information.
#     
# If you are stuck on a problem or do not understand a question - please come to office hours or ask questions to the slack group (please don't post your code though). If it is a coding problem send a private email to all of the instructors.
# 
# Hints are given in some of the questions; these are optional so you do NOT need to use the hint (or code your answer that way) as long as your code meets the requirements of the problem.

# ### Grading Rubric
# 
# -General grading rubric guidelines / philosophy:
# 
# -The total possible points will be shown for each question
# 
# -Please read each question carefully to understand the requirements
# 
# -Points for each question are rewarded based on how well your code fulfills those requirements
# 
# -Some problems have an example given to help show what is needed and how to format the answer
# 
# 
# #### More on grading:
# 
# -If the question is blank / not attempted, no points will be given
#     
# -Most points are given for code that runs and fulfills the requirements
# 
# -Minor points are given for formatting the answer in accordance with the question

# ## Basic Variables and Strings (20 pts)
# 
# ### Basic Variables
# 

# ### 3.1: (2pts) Write a program that gets a number between 1 and 1,000,000 from the user and determines whether it is odd or even using an if statement. Print the results. *Note use the input function.

# In[10]:


a= 46695.123456789
print("{:.2f}".format(a));


# In[14]:


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# ### 3.2: (2pts) Write the necessary code 
# that prints out the area and the circumference of a circle with a radius of 3.14.
# 

# In[21]:


r = 3.14


# In[35]:


pi = 3.14
r = 3.14
c = 2 *pi* r


# In[36]:


print(c)


# 3.3: (2pts)  Write the necessary code to display the area and perimeter of a rectangle that has a width of 24 and a height of 6.4.
# 

# In[37]:


w=24
h=6.4


# In[38]:


a= w*h
p= 2*w + 2*h


# In[56]:


print("The area is", "{:.2f}".format(a))
print("The perimeter is", p)


# 3.4: (2pts) A runner runs 12 kilometers in 30 minutes and 30 seconds. What is her/his average speed in miles per hour?
# 

# In[47]:


km1=0.621371 
milestotal=12*(km1)
timetotal=(30.5/60)


# In[53]:


speedtotal=milestotal/timetotal
print("The runner's average speed was", speedtotal, "mph.")


# 3.5:(2pts) In the U.S., if there is:
# 
# -One person who is born every 6 seconds
# 
# -One person who dies every 12 seconds 
# 
# -One person who immigrates every 40 seconds
# 
# Write the necessary code to display the total population for the next three years (without a leap year). Do not forget to investigate the current population as baseline.
# 

# In[66]:


startingpop= 329450000 
secsperday=86400
daysperyear=365
totaldays=3*(daysperyear)


# In[67]:


birthsperday=86400/6
deathsperday=86400/12
immigrationsperday=86400


# In[68]:


newpop= startingpop +
((totaldays)*(birthsperday)) + ((totaldays)*(immigrationsperday)) 
- ((totaldays)*(deathsperday))


# In[69]:


print(newpop)


# ###3.6: (2pts) Write the necessary code to read a degree in Celsius then convert it to Fahrenheit and print it to the console.
# 
# F = C * 1.8 + 32
# 
# Output should read as in the following format example: "27.4 degrees Celsius = 81.32 degrees Fahrenheit."
# 
# 
# *Hint: If you get an error, look up what input( ) returns!

# In[74]:


temp = float(input("Enter a Temperature in degrees Celsius: "))
print((temp * 1.8 + 32), "degrees Fahrenheit.") 


# 
# 3.7: (2pts) Receive the following arguments from the user:
# - miles to drive
# - mpg of the car
# - price per gallon of fuel
# 
# print these and the cost of the trip

# In[94]:


dist, mpg, price = int(input("Enter miles to drive ")), int(input("Enter miles per gallon of your car ")), int(input("Enter price of gas per gallon "))
print(((dist)*(price))/(mpg), "is the cost of your trip.") 


# ### Strings

# 3.8 (2pts) There are many string methods available to perform all sorts of tasks.
# Experiment with some of them to make sure you understand how they work. Strip and replace are particularly useful.
# Python documentation uses a syntax that might be confusing. For example, in
# 
# find(sub [ , start [, end ] ] ) 
# 
# the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.
# For this exercise, demonstrate the following string methods below:
# 
# -strip
# 
# -replace
# 
# -find
# 

# In[138]:


#strip
string="When I typed strip in into Google, the first result was 'strip in Vegas'"

print(string.strip('When I typed strip in into Google, the first result was'))


# In[130]:


#replace
string = 
print(string.replace(


# In[166]:


#find
#returns indexes of the string you're looking for, e.g. placement of Stanley
laundry = "Bob's burgers and my dog Stanley"

x = str(laundry.find('Stanley'))

print("Index for Stanley found at", x)


# 3.9 (2pts) There us a string method called 'count'. Read the documentation of the 'count' method and write a script that counts the number of a's in 'banana' that uses the built in method 'count.'

# In[99]:


string = "banana"
substring = "a"

count = string.count(substring)
print("The count is", count)


# 3.10 (2pts) Write a script that takes a user inputted string and prints it out in the following three formats.
# 
# -All letters capitalized 
# 
# -All letters lowercase 
# 
# -All vowels lowercase and all consonants uppercase.
# 

# In[183]:


favcol= str(input("Enter your favorite color"))
vowels= str(('U','O', 'E', 'A', 'I'))
print(favcol.lower())
print(favcol.upper())
print("I've tried 914598685486 different ways to do the uppercase consonants and lowercase vowels and cannot figure it out")


# ## 3.11. Short Answers (20pts total)

# 3.11a (2pts): In Python, what is the difference between =(single equal) and == (double equal)?

# In[ ]:


# = is used to assign value, rename, etc. It sets two things equal to each other. 
# == is often described as a comparison, but I think of more as a condition. 


# 3.11b (2pts): If I am commenting on my code in a cell, what are the two ways to do this in Python?

# In[115]:


#Like this 
"""or like this"""


# 3.11c (2pts): Write a print statement to print the following: It's very clear I'm going to get this right 100%.

# In[108]:


print("It's very clear I'm going to get this right 100%.")


# 3.11d (2pts): Name four data types in Python. Use a markdown cell type for this answer.

# Boolean (true or false), Integers, strings and floats

# 3.11e (4pts): Assign your name, your Yale program, and your year of graduation equal to variables of your choosing. Then write a print statement using an "f string" that says "Hello, my name is (name). I am in Yale's (program) and I hope to graduate in (year)."

# In[120]:


a= "Julia"
b= "School of Public Health"
c= "2020"
print(f"Hello, my name is {a}. I am in Yale's {b} and I hope to graduate in {c}.")


# 3.11f (2pts): Write the mathematical operators for the following using a markdown cell type and give a code example of each:
# For example:
# plus: + , 3 + 4
# 
# minus:
# 
# multiply:
# 
# divide:
# 
# find the remainder of two numbers divided:
# 
# square: (as in 3 squared is 9)
# 
# cube: (as in 2 cubed is 8)
# 
# greater than:
# 
# greater than or equal to:
# 
# less than:
# 
# less than or equal to:
# 
# 
# 

# minus: -, 4-3=1
# 
# multiply: *, 4*3=12
# 
# divide: /, 4/2=2
# 
# find the remainder of two numbers divided: %, 3%2=1
# 
# square: (as in 3 squared is 9) **2, 3**2 = 9
# 
# cube: (as in 2 cubed is 8) **3, 2**3=8
# 
# greater than: >, 3>2
# 
# greater than or equal to: >=, 3 >=2
# 
# less than: < , 2 < 3
# 
# less than or equal to: <= , 2<=3

# 3.11g (2pts): What is the built-in Python function to determine the type of an object?
# Give four examples of using this function on four different object types.

# In[160]:


print(type(1.2))
print(type(1))
print(type(True))
print(type("True"))


# 
# 
# 3.11h (4pts): Write a program using print that, when run, prints out a tic-tac-toe board.
# Expected output:

# In[164]:


t="    |   |    "
i="-----------"
c= "    |   |    "
tac="-----------"
toe="    |   |    "
print(t)
print(i)
print(c)
print(tac)
print(toe)


# ## Some Puzzles (60 pts total)

# 3.12. Tip Calculator (20 points)
# 
# Below, you can see the script I wrote to compute the tip for a meal. Fix it so that it works correctly. Expect the input to be a number. Please format the output to 2 decimal places.
# 
# 
# Example Grading Rubric:
# 
#     10 points: fixing the crash so the program works with numbers (for example: 10 or 4.99)
#     5 points: formatting the output correctly to 2 decimal places
#     5 points: naming the file correctly (tip.py)
# 
# price = input("Enter the price of a meal: ")
# 
# tip = price * 0.16
# total = price + tip
# 
# print("A 16% tip would be:", tip)
# print("The total including tip would be:", total)
# 
# Enter the price of a meal: 10
# 
# -----------------------------------------------------------------------

# In[203]:


price = float(input("Enter the price of a meal: "))
tip = price * 0.16
total = price + tip
print("Your total is $""{:.2f}".format(total))


# 3.13. Gas Pump Informer (15 points)
# 
# Write a script that prompts the user for a number of gallons of gasoline. Reprint that value, along with its conversion to other measurements:
# 
#     Equivalent number of liters (format to 4 decimals)
#     Number of barrels of oil required to produce it (format to 3 decimals)
#     Price in U.S. dollars (format to 2 decimals)
# 
# Figures to use:
# 
#     1 gallon is equivalent to 3.7854 liters.
#     1 barrel of oil produces 19.5 gallons of gas.
#     The average price of gas is approximately $3.65 per gallon.

# In[204]:


gallons = float(input("Enter the number of gallons of gasoline: "))
liters= float(3.7854 * gallons)
barrels=gallons/19.5
price= gallons *3.65
print("The amount of gallons of gasoline entered was", gallons)
print("That is", "{:.4f}".format(liters) ,"liters of gasoline.")
print("{:.3f}".format(barrels), "is the number of barrels required to produce that amount of gas.")
print("That would cost about $""{:.2f}".format(price))      


# 
# 3.14. Income Tax (20 points)
# 
# The mythical island nation of Kinglandia has a rather simple tax code. The first 1000 dollars of income is taxed at 5%. The next 1000 dollars is taxed at 10%. Any income beyond the first 2000 dollars is taxed at 15%. Complete the following script so that it asks the user for his or her income (a number) and outputs the amount of tax owed.
# 
# Example:
# 
# Please enter your income: 1500
# 
# The tax owed is: $100
# 

# In[219]:


income = float(input("Please enter yoru income to know the amount of taxes due"))
if income <= 1000: print(income * (.05)), 
if 2000> income > 1000: print((income -1000)*(.10)+ (50)),
if income >= 2000: print((150)+(income-2000)*(.15))


# 
# 3.15 Palindrome (20 points)
# 
# Write a script that prompts the user for a name (this input will be a 1 word string). Using a while loop that counts downwards (instead of using the 'reverse' function or the string slicing [::-1] method), print the letters of the name reversed (hint: you can use print(var, end='') in each iteration of the loop). You should use s.lower() and s.upper(), as appropriate, to change the string to lowercase and print it out with only the first letter of the reversed word in uppercase. If the name is the same forward and backwards, print "Palindrome!" on the next line. Make sure your code prints the sample examples exactly as shown below.
# 
# Examples:
# 
# Enter your name: Paul
# Luap
# 
# Enter your name: ANA
# Ana
# Palindrome!
# 
# 
# 
# 
# 

# In[250]:


palin = input("Enter a name:").lower()
palin2 = (palin[::-1]).lower()

print(palin2), 
if palin==palin2: print("Palindrome!") 

