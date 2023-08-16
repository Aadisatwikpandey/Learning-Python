name=input("What is you name? ")

""".strip()-Remove white space from a string"""
name = name.strip()

""".Capitalize()- is used to capitalize the first number"""
name = name.capitalize()

""".title() is used to capitalize the name in a specific way"""
name=name.title()

""".split()-Splits the given string"""
first, last = name.split(" ")

"""To make the code short, the whole code be written as:
name = name.strip().title()
#Or,
name = ("what is your name ?").strip().title()
"""
print(name)
print(f"hello,{first}")



