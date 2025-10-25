try:
  a = float(input("Enter first number:"))
  b = float(input("Enter second number:"))
  print(f"Addtion:{a+b}")
  print(f"subtraction:{a-b}")
except ValueError:
  print("please Enter valid number.")

