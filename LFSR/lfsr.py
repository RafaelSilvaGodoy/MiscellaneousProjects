# Random Number Generator - Linear-feedback shift register (LFSR)
# Author: Rafael Godoy
# LinkedIn: https://www.linkedin.com/in/Rafael-Godoy-ML-Eng
# Github: https://github.com/RafaelSilvaGodoy
#
# This script generates random numbers of 32bits through the LFSR method.
# This script was inspired by the video: https://www.youtube.com/watch?v=Ks1pw1X22y4

# The quantity of bits that the random number will be represented.
n_bits = 32

# The initial value of the number that will generate the random numbers.
state = (1<<127) | (1<<64) | (1<<71)| (1<<7)| (1<<97)| 1

# ref is the maximum value achieved by the b_bits number.
ref = (1<<n_bits)
for i in range(n_bits):
    ref = ref | (1<<n_bits-i)
    
rand_num,i,j = (0,)*3

while True:
    # Random generator equation -> XOR on the postion 1,2 and 7 of the state variable.
    newbit = (state ^ (state >> 1)^ (state >> 2)^ (state >> 7)) & 1
    state = (state >> 1) | (newbit << 127)
    
    # Aggregate the last digit generated (1 or 0) into the rand_number in the position between 0 and n_bits.
    rand_num = rand_num | ((state&1) << (n_bits-j)) 
    j += 1
    
    # Print the number every 32 bits generated.
    if not i%n_bits:
        print(rand_num/ref)
        rand_num = 0
        j = 0
    i+= 1