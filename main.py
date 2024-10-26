def reverse_bits(n):
    binary_representation = bin(n)[2:]
    reversed_binary = binary_representation[::-1]
    reversed_number = int(reversed_binary, 2)
    return reversed_number

number = int(input("Enter a number: "))
new_number = reverse_bits(number)
print(f"The new number after reversing all bits is: {new_number}")
