# def greet(name):
#   print("Hello",name)
#   print("how do you do",name)
# greet(name)
name =input("Kindly enter your name:\n")
location=input("Where are yu from:\n ")

def greet_with_name(name,location):
  print(f"Hello {name} of {location}")
  
greet_with_name(location=location,name=name)

