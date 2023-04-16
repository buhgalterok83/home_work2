longest_line = ''
with open('file.txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        if len(line) > len(longest_line):
            longest_line = line

print(longest_line)
