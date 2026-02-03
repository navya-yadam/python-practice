# Strings are immutable 
# a = "!!!Navya!! !!!!!!! Harry"
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("Navya","John"))
# print(a.split(" "))
# blogHeading = "introduction to js"
# print(blogHeading.capitalize())


# str1 = "Welcome to the Console!!!"
# print(len(str1))
# print(len(str1.center(50)))
# print(str1.center(50))
# print(a.count("Harry"))

str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))

print(str1.endswith("to", 4, 10))


str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))

print(str1.index("is"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())  #A-Z,a-z,0-9

print(str1.isalpha())  #A-Z,a-z

print(str1.isprintable())

str1 = "   "
print(str1.isspace())

str1 = "Navya Sree"    #first letter must be capital
print(str1.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "python is a Interpreted Language"
print(str1.swapcase())

print(str1.title())
# ....End....
