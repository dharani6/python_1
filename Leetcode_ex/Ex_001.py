'''

476. Number Complement
Solved
Easy
Topics
Companies
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.



Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


Constraints:

1 <= num < 231


Note: This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

'''

num = int(input("Enter Number for finding complement!!!\n"))

bin_num = bin(num)[2:] # bin(num) will be '0b101 for 5 bin will convet int to binary number as string
lst_bin = (list(bin_num)) # convert the string to list to iterate
for i in range(len(lst_bin)): # for loop iteration it convert 1 to 0 and 0 to 1 all are done on string where int cant be iterated in for loop
    if lst_bin[i] == '1': # usinng if condition to chek the iterater is 1 or 0
        lst_bin[i] = '0'
    else:
        lst_bin[i] = '1'
print(f"Converted {bin_num} num to complementary as list {lst_bin}")
print(''.join(map(str,lst_bin)))
complement_num = int(''.join(lst_bin),2) # complimented num is conveted to integer by int and base 2 to convert binary to decimal
print(complement_num)
#new_bin_lst = [e for e in lst_bin if e == '1'  e = '0' else e = '1']
#print(new_bin_lst)

# Step 1: Convert 5 to binary
num = 5
binary_num = bin(num)[2:]  # bin() gives binary with '0b' prefix, so we slice it off
print(f"Binary of {num}: {binary_num}")

# Step 2: Find the binary complement
# To find the complement, we invert the bits and ensure we keep the same bit length
binary_complement = ''.join('1' if bit == '0' else '0' for bit in binary_num)
print(f"Binary complement of {binary_num}: {binary_complement}")

# Step 3: Convert the binary complement back to a decimal number
decimal_complement = int(binary_complement, 2)
print(f"Decimal of complement {binary_complement}: {decimal_complement}")
print(binary_num)
new_bin_num = ['1' if i =='0' else '0' for i in bin_num]
print(new_bin_num)
print(type(''.join(new_bin_num)))
print((''.join(new_bin_num)))
