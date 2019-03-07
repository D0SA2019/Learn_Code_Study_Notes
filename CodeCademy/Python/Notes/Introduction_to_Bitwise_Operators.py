print("")
print("------ Introduction to Bitwise Operators ------")

print("")
print("------ 1. Just a Little BIT ------")
print(5 >> 4)  # Right Shift
print(5 << 1)  # Left Shift
print(8 & 5)   # Bitwise AND
print(9 | 4)   # Bitwise OR
print(12 ^ 42) # Bitwise XOR
print(~88)     # Bitwise NOT




print("")
print("------ 2. Lesson I0: The Base 2 Number System ------")
print(0b1)
print(0b10)
print(0b11)
print(0b100)
print(0b101)
print(0b110)
print(0b111)
print("******")
print(0b1 + 0b11)
print(0b11 * 0b11)




print("")
print("------ 4. The bin() Function ------")
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))




print("")
print("------ 5. int()'s Second Parameter ------")
print(int("42"))
print(int("110", 2))
print("")
print(int("1",2))
print(int("10",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
print(int("11001001", 2))




print("")
print("------ 6. Slide to the Left! Slide to the Right! ------")
shift_right = 0b1100	# 0011
shift_left = 0b1			# 100

shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))




print("")
print("------ 7. A BIT of This AND That ------")
print(bin(0b1110 & 0b101))




print("")
print("------ 8. A BIT of This OR That ------")
print(bin(0b1110 | 0b101))




print("")
print("------ 9. This XOR That? ------")
print(bin(0b1110 ^ 0b101))




print("")
print("------ 10. See? This is NOT That Hard! ------")
print(~1)
print(~2)
print(~3)
print(~42)
print(~123)




print("")
print("------ 11. The Man Behind the Bit Mask ------")
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print("Bit was on")

def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"





print("")
print("------ 12. Turn It On ------")
a = 0b10111011
mask = 0b100
print(bin(a | mask))




print("")
print("------ 13. Just Flip Out ------")
a = 0b11101110
mask = 0b11111111
print(bin(a ^ mask))




print("")
print("------ 14. Slip and Slide ------")
def flip_bit(number, n):
    mask = (0b1 << n-1)
    result = number ^ mask
    return bin(result)

print(flip_bit(0b10010, 9))
