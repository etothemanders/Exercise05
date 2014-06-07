"""Write a program, lettercount.py, that opens a file named on the command line and 
counts how many times each letter occurs in that file. 
Your program should then print those counts to the screen, in alphabetical order."""

from sys import argv

def get_file_contents():
    filename = argv[1]
    f = open(filename, "r")
    text = f.read()
    f.close()
    return text

def count_letters(text):
    text = text.lower()
    letter_counts = [ 0 for x in range(256) ]
    
    for letter in text:
        char = ord(letter)
        letter_counts[char] += 1
        
    return letter_counts
        

def print_counts(letter_counts):
    
    for index, count in enumerate(letter_counts):
        if index >= ord('a') and index <= ord('z'):
            print count

def main():
    text = get_file_contents()
    counts = count_letters(text)
    print_counts(counts)

    
if __name__ == "__main__":
    main()
