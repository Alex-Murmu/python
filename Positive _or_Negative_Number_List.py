numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
for num in numbers:
    if num >= 0:
        print(f"{num} is positive.")
    else:
        print(f"{num} is negative.")
