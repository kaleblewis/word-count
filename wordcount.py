#open the original file
input_file = open('./test.txt')

word_counts = {}

for line in input_file:
    # strip out the white space and split out the words 
    line = line.rstrip()
    words = line.split()

    for word in words:
        # loop through and generate a dictionary with entries for each 'word' 
        # note:  punctuation counts as part of a 'word'
        word_counts[word] = word_counts.get(word, 0) + 1

input_file.close()

# print out the dictionary created above
for word, count in word_counts.items():
    print(word, count)