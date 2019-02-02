n = eval(input("How many  numbers  do you have? "))
sum  = 0.0
for i in range(n):
    x = int(input("Enter the numbers  >> "))
    sum  = sum  + x.split('', n)
print("\nThe average  of the numbers  is", sum  / n)
