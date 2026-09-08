print("===== NUMBER TOOLS =====")

num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Prime Check
if num < 2:
    print("Not a Prime Number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")

# Square and Cube
print("Square:", num ** 2)
print("Cube:", num ** 3)

# Factorial
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)