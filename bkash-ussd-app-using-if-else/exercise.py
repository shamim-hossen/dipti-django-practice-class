'''List of problem
1.Searching from list
2.Summation list value
3.Reverse list item
4.Maximum number and minimum number from list
5.Prime number
6.Prime number series
7.Factorial
8.Digit reverse
9.Palindrome number
10.Armstrong number
11.Armstrong number series
12.Leap year
13.Pattern
14.Find the sequence of numbers
15.Fibonacci series
16.Geomatric series
17.Arithmatic series
18.Bubble sort (Any sorting algorithm)
'''


# def my_function(fname, lname):
#     fullName = fname+lname
#     for i in fullName:
#         print(i)


# my_function("Shamim","Hossen")




# def fun(*kids):
#     print("The youngest child are", end=' ')
#     for i in kids:
#         if i == kids[-1]:
#             print(i, end='.')
#         else:
#             print(i, end=',')
#     print(len(kids))
# fun("Emil", "Tobias", "Linus")




# def fun(**kid):
#     print("His last name is "+ kid['lname'])
# fun(fname = "Shamim", lname = "Hossen")




# def myfun(*food):
#     for i in food:
#         print(i)


# fruits_list = ['apple', 'banana', 'cherry']
# fruits_touple = ('a', 'b', 'c')
# fruits_dictionary = {'key1': 'apple', 'key2': 'banana', 'key3': 'cherry'}


# myfun(fruits_list, type(fruits_list))
# myfun(fruits_touple, type(fruits_touple))
# myfun(fruits_dictionary, type(fruits_dictionary))




# def fun(country = "Norway"):
#     print("I am from "+ country)


# fun("Sweden")
# fun("India")
# fun("Brazil")
# fun()



#return
# def fun(x):
#     return 5*x
# n=int(input("Enter number:"))
# y = fun(n)
# print(y)
# print(fun(5))
# print(fun(9))




# def fun():
#     n=int(input("Enter number:"))
#     return 5*n

# print(fun())



# Digit reverse
def reverse_digits(number):
    if number < 0:
        return -int(str(-number)[::-1])  
    else:
        return int(str(number)[::-1]) 

number = 12345
reversed_number = reverse_digits(number)
print("Reversed number:", reversed_number)
