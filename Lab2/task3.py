number = int(input("Enter a five-digit number: "))

digit1 = number // 10000
digit2 = number // 1000 % 10
digit3 = number // 100 % 10
digit4 = number // 10 % 10
digit5 = number % 10

sim_digits = digit1 + digit2 + digit3 + digit4 + digit5

reversed_number = (
    digit5 * 10000
    + digit4 * 1000
    + digit3 * 100
    + digit2 * 10
    + digit1
)
print("Sum of digits:", sum_digits)
print("Reversed number:",
reversed_number)
