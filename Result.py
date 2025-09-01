name = input("Enter your name: ")  
marks = int(input("Enter your marks: "))  

choice = input("Enter your choice: ('marks' or 'name'): ")

if choice.lower() ==  "name":
  print("your name is:", name)
elif choice.lower() == "marks":
  print("your marks is:", marks)
  if marks >= 90:
    print("your grade is A", "Excellent")
  elif marks >= 80:
    print("your grade is B","Well done")
  elif marks >= 68:
    print("your grade is", "Good")
  elif marks >= 50:
    print("your grade is", "Pass")
  elif marks < 33:
    print("you are fail","Better luck next time")
  else:
    print("Invalid choice! Please enter 'name' or 'marks")