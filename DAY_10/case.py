f_name= input("Enter your name: ")
l_name= input("Enter your name: ")

def format_name(f_name,l_name):
  formated_lname= f_name.title()
  formatted_fname= l_name.title()
  return(f"{formated_lname} {formatted_fname}")
print(format_name(f_name,l_name))