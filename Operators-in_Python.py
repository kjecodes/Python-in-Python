#the output tool
#the print function tells the computer to display something on the screen. It can be used to show text, numbers, or the results of calculations.
print("Hello, World!")  # This will display the text "Hello, World!" on the screen.
print("We will mainly be using the print function for the lesson")
print("The input tool")
print("the input function allows the user to enter data. When the input function is called, the program will pause and wait for the user to type something and press Enter. The text entered by the user will be returned as a string.")
print('Example: input("Please enter your name: ")  # This will prompt the user to enter their name and return it as a string.')
print("however, we need a place to store the user's input. We can use a variable for that. A variable is like a container that holds a value. We can assign a value to a variable using the equals sign (=).")
name = input("Please enter your name: ")  
print("the previous function will store the user's input in the variable 'name'.")
print("we can implement both the print and input functions together to create a simple program that greets the user by name.")
print("Hello, " + name + "!")
print("The previous function will display a greeting message that includes the user's name.")
print("Data types: strings")
print("A string is a sequence of characters enclosed in quotes. You can use either single quotes (' ') or double quotes (" ") to create a string.")
print("If you are not sure whether or not a data in your code is a string, you can use the type function to check. The type function will return the data type of the value you pass to it.")
print(type("Hello, World!"))
print("The previous function will output: <class 'str'>")
print(type(name))
print("The previous function will also output: <class 'str'>, since the user's input is stored as a string.")
print("In our previous example, 'Hello, World!' and 'Please enter your name: ' are both strings. We can also create strings that include variables by using the + operator to concatenate (join) them together.")
word1 = "Hello" 
print("word1 is a string variable that holds the value 'Hello'.")
word2 = "World"
print("word2 is another string variable that holds the value 'World'.")
greeting = word1 + ", " + word2 + "!"  
print("The previous function will concatenate the strings stored in word1 and word2, along with some additional characters to create a greeting message.")
print(greeting)
print("The previous function will display: Hello, World! or whatever values are stored in word1 and word2.")
print("Data types: integers")
print("An integer is a whole number without a decimal point. You can create an integer by simply writing a number without quotes.")
age = 25
print("age is an integer variable that holds the value 25.")
print(type(age))
print("The previous function will output: <class 'int'> since age is an integer.")
print("you can also perform arithmetic operations with integers using various operators. The most common arithmetic operators are:")
print("arithmetic operators:+(addition)")
print("we previously explored the use of + for concatenating strings, but it can also be used for arithmetic operations with numbers. When you use the + operator with numbers, it performs addition.")
num1 = 10
num2 = 5
result = num1 + num2
print("The previous functionwill calculate the sum of num1 and num2, which is 15.")
print(result)
print("The previous function will display: 15, or the result of adding num1 and num2.")
print("we can use what we learned to make a basic calculator that adds two numbers entered by the user.")
num1 = int(input("Enter the first number: "))
print("The previous function will prompt the user to enter the first number and convert it to an integer.")
num2 = int(input("Enter the second number: "))
print("The previous function will prompt the user to enter the second number and convert it to an integer.")
result = num1 + num2
print("The previous function will calculate the sum of num1 and num2, which is stored in the variable 'result'.")
print("The sum is:", result)
print("The previous function will display: The sum is: 15, or the result of adding num1 and num2.")
