

# 1 
value = 2
'''if (value > 0):
    if (value < 10):
        print("did it")'''
    
if value > 0 and value < 10:
    print("did it")


#2 
my_str = "password"
'''if ((len(my_str) > 0) and (my_str!= "password")):
  print("did it")'''

if len(my_str) > 0:
    if my_str!= "password":
        print("did it")

#3
'''if ((len(my_str) == 0) or (my_str!= "password")):
  print("did it")'''

if len(my_str) == 0:
    print("did it")
if my_str!= "password":
    print("did it")

'''
Consider the following debugging techniques and describe how each one is most useful. List the pros and cons of each technique. 
Comments - easy to identify what each code segment does within a program but is not able to identify errors
Print statements - able to print the certain debug codes which can help debug a program but this is not their main usage and a debugger would be more useful.
Hand tracing - very inefficient way of debugging but can help identify the problematic code segment
Test cases vs. user-defined input - test cases are used for testing the problematic code segments to try and fix errors, while user defined input can be used to test logic errors.
Debuggers - used to fix the code that is not working and can identify where exactly the code is not working and list some potential solutions, however it can be very slow in longer code.
'''