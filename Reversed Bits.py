def reverse_bits(n):
    num_bits = n.bit_length()
    
    reversed_num = 0
    
    for i in range(num_bits):
        reversed_num <<= 1
        
        reversed_num |= (n & 1)
        
        n >>= 1
    
    return reversed_num

input_number = int(input("Enter a number: "))
result = reverse_bits(input_number)

print(f"The number with its bits reversed is: {result}")