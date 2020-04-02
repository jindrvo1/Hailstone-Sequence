def hailstone(n):
    res = []
    while n > 1:
        res.append(int(n))
        n = n/2 if n%2 == 0 else 3*n + 1
    res.append(1)
    return res


# Load the numbers from the file
nums = []
with open('data.csv') as f:
    nums = f.readlines()
nums = [int(num) for num in nums]


# Get only the unique numbers
unique = list(set(nums))


# Calculate the sequences
sequences = [hailstone(n) for n in unique]

# Pad the sequences with ones to maximum length
max_len = max([len(sequence) for sequence in sequences])
sequences = [sequence + [1]*(max_len-len(sequence)) for sequence in sequences]

# Write sequences to file
with open('results_noLib.csv', 'w') as f:
    for sequence in sequences:
        f.write(','.join(map(str, sequence)))
        f.write('\n')