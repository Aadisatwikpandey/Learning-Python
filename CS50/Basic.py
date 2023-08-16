print("Hello world")

"""
Argument- It is an input to a function that somehow affects the behaviour of the function.
Side effect- The output that comes on the screen is known as side effect.
Bugs - Mistakes in a program
"""

name=input("What is you name? ")
# First way
print("hello,")
print(name)

"""
Variables- a container for some value inside a computer .
'=' or 'single equal sign'is an assignment operator in most of the languages.
"""

# second way(There is an extra space by default(after Hii,))
print("Hii,",name)

"""
Comment- A function that is ignored by computer but a note for coder or user writing code
 Pseudocode- It a way of structuring a big code or a todo list prepared before coding
 triple times double quotation(""" """) is used for multiline comment.
When you pass multiple argument to print, it automatically add an extra space after each argument.
"""


#Third way(There is no extra gap by default(After hello,))
print("Hello," + name)


"""
'\n'- is used for new line

print(*object, sep=' ', end='\n')
1.In the above given comment, * indicates it can take as many lines of codes as it wants
2. Sep=' '- indicates that there is always a gap after each objects
3. end="\n' indicates that there will be always a new line after each print function
4. we can modify each values 
"""

# Fourth way(override the next line command(\n) form the print function)
print("Hii,", end="")
print(name)

"""
Parameters- 

Double quote(") inside a double quote is not entertained or understood by the computer
To make it work, we can change outer double quote to single quote, and put inside quote as it is.
or, we can put \ insted.
e.g.,
"""

print('Hello,"friend"')
#or
print("hello,\"friend\"")

"""format string or fstring- this tells python that this a special string so, format it in different way."""
#Fifth way
print(f"Hii,{name}")


