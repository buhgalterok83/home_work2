def read_last(file_path, symbol_number):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            if line:
                last_symbols = line[-symbol_number:]
                print(last_symbols)
read_last('/Users/goncharovvitalii/Downloads/read_last.txt', 6)
