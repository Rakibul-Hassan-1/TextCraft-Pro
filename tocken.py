import re

# Function to check if a string is a keyword
def keyword(word):
    keywords = {"for", "while", "do", "int", "float", "char", "double", "static", "switch", "case"}
    if word in keywords:
        print(f"\n{word} is a keyword")
    else:
        print(f"\n{word} is an identifier")

def main():
    # Read input from the user
    print("Enter the C program (Ctrl+D to end input):")
    input_program = []
    try:
        while True:
            line = input()
            input_program.append(line)
    except EOFError:
        pass

    # Write input to a file
    with open("input.txt", "w") as f1:
        f1.write("\n".join(input_program))

    # Initialize variables
    numbers = []
    identifiers = []
    special_chars = []
    lineno = 0

    # Process the input file
    with open("input.txt", "r") as f1:
        for line in f1:
            lineno += 1
            # Extract numbers
            numbers.extend(re.findall(r'\d+', line))
            # Extract identifiers and keywords
            identifiers.extend(re.findall(r'[a-zA-Z_$][a-zA-Z0-9_$]*', line))
            # Extract special characters
            special_chars.extend(re.findall(r'[^\w\s]', line))

    # Write identifiers to a file
    with open("identifier.txt", "w") as f2:
        f2.write(" ".join(identifiers))

    # Write special characters to a file
    with open("specialchar.txt", "w") as f3:
        f3.write(" ".join(special_chars))

    # Output results
    print("\nThe numbers in the program are:", " ".join(numbers))
    print("\nThe keywords and identifiers are:")
    for word in identifiers:
        keyword(word)
    print("\nSpecial characters are:", " ".join(special_chars))
    print("\nTotal number of lines are:", lineno)

if __name__ == "__main__":
    main()