#the output tool
#the print function tells the computer to display something on the screen. It can be used to show text, numbers, or the results of calculations.
print("Hello, World!")  # This will display the text "Hello, World!" on the screen.
print("We will mainly be using the print function for the lesson")
print("The input tool")
print("the input function allows the user to enter data. When the input function is called, the program will pause and wait for the user to type something and press Enter. The text entered by the user will be returned as a string.")
print('Example: input("Please enter your name: ")  # This will prompt the user to enter their name and return it as a string.')
print("however, we need a place to store the user's input. We can use a variable for that. A variable is like a container that holds a value. We can assign a value to a variable using the equals sign (=).")
name1 = input("Please enter your name: ")  
print("the previous function will store the user's input in the variable 'name1'.")
print("we can implement both the print and input functions together to create a simple program that greets the user by name.")
print("Hello, " + name1 + "!")
print("The previous function will display a greeting message that includes the user's name.")
print("Data types: strings")
print("A string is a sequence of characters enclosed in quotes. You can use either single quotes (' ') or double quotes (\"\" ) to create a string.")
print("If you are not sure whether or not a data in your code is a string, you can use the type function to check. The type function will return the data type of the value you pass to it.")
print(type("Hello, World!"))
print("The previous function will output: <class 'str'>")
print(type(name1))
print("The previous function will also output: <class 'str'>, since the user's input is stored as a string.")
print("In our previous example, 'Hello, World!' and 'Please enter your name: ' are both strings. We can also create strings that include variables by using the + operator to concatenate (join) them together.")
word1 = "Hello" 
print("word1 is a string variable that holds the value 'Hello'.")
word2 = "World"
print("word2 is another string variable that holds the value 'World'.")
greeting1 = word1 + ", " + word2 + "!"  
print("The previous function will concatenate the strings stored in word1 and word2, along with some additional characters to create a greeting message.")
print(greeting1)
print("The previous function will display: Hello, World! or whatever values are stored in word1 and word2.")
print("Data types: integers")
print("An integer is a whole number without a decimal point. You can create an integer by simply writing a number without quotes.")
age1 = 25
print("age1 is an integer variable that holds the value 25.")
print(type(age1))
print("The previous function will output: <class 'int'> since age1 is an integer.")
print("you can also perform arithmetic operations with integers using various operators. arithmetic operators:")
print("arithmetic operators:+(addition)")
print("we previously explored the use of + for concatenating strings, but it can also be used for arithmetic operations with numbers. When you use the + operator with numbers, it performs addition.")
num1 = 10
num2 = 5
result1 = num1 + num2
print("The previous function will calculate the sum of num1 and num2, which is 15.")
print(result1)
print("The previous function will display: 15, or the result of adding num1 and num2.")
print("we can use what we learned to make a basic calculator that adds two integers entered by the user.")
print("however we must make sure that the input is always an integer. We can do this by using the int function to convert the user's input to an integer.")
print("we can also involve a loop in order to make sure that the input is always an integer. We can use a while loop to keep prompting the user until they enter a valid integer.")
while True:
    try:
        num3 = int(input("Enter the first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
print("The previous function will prompt the user to enter the first number and convert it to an integer.")
while True:
    try:
        num4 = int(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
print("The previous function will prompt the user to enter the second number and convert it to an integer.")
result = num3 + num4
print("The previous function will calculate the sum of num3 and num4, which is stored in the variable 'result'.")
print("The sum is:", result)
print("The previous function will display the result of adding num3 and num4.")
print("function: while loop")
print("the while function is a loop that will keep prompting the user until they enter a valid integer." )
print("The try function is used to attempt to convert the user's input to an integer. If the conversion fails, a ValueError will be raised, and the except block will be executed, prompting the user to enter a valid integer.")
print("ValueError is an error that occurs when a function receives an argument of the correct type but an inappropriate value. In this case, it occurs when the user enters a non-integer value that cannot be converted to an integer.")
print("data types: floats")
print("A float is a number with a decimal point. You can create a float by writing a number with a decimal point or using scientific notation.")
price1 = 19.99
print("price1 is a float variable that holds the value 19.99 in decimal notation.")
price2 = 1.5234e2
print("price2 is a float variable that holds the value 152.34 in scientific notation.")
print(type(price1))
print("The previous function will output: <class 'float'> since price1 is a float.")
print(type(price2))
print("The previous function will output: <class 'float'> since price2 is also a float.")
print("arithmetic operators:-(subtraction)")
print("similarly to the + operator, the - operator can be used for arithmetic operations with numbers. When you use the - operator with numbers, it performs subtraction.")
difference = num1 - num2
print("The previous function will calculate the difference between num1 and num2, which is 5.")
print(difference)
print("The previous function will display: 5, or the result of subtracting num2 from num1.")
print("after learning about the + and - operators, we can create a basic calculator that performs addition and subtraction based on user input.")
while True:
    print("Please enter two numbers to perform addition and subtraction.")
    while True:
        try:
            num5 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            num6 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    operation = input("Enter '+' for addition or '-' for subtraction: ")
    if operation == "+":
        result = num5 + num6
        print("The sum is:", result)
    elif operation == "-":
        result = num5 - num6
        print("The difference is:", result) 
    else:
        print("Invalid operation. Please enter '+' or '-'.")

    while True:
        try:
            choice1 = int(input("press 1 to repeat the calculator, 2 to continue to the next lesson, or 3 to exit the program."))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    if choice1 == 1:
        continue
    elif choice1 == 2:
        break
    elif choice1 == 3:
        print("Exiting the program. Goodbye!")
        exit()
print("What we did previously involved if loops and elif loops. The if loop checks if a condition is true, and if it is, it executes the code block under it. The elif loop checks for additional conditions if the previous if condition was false. If none of the conditions are true, the else block can be executed.")
print("WIP")

