temp = float(input("Enter temperature: "))
sys = input("Enter unit in F/f or C/c: ")

if sys.lower()=="f":
    print(f"{temp}° in Fahrenheit is equivalent to {(temp-32)*5/9}° Celsius.")
elif sys.lower()=="c":
    print(f"{temp}° in Celsius is equivalent to {(temp*9/5)+32}° Fahrenheit.")
else:
  print(f"Invalid unit((sys)).")