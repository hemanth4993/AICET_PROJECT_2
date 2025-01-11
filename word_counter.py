def count_words(text):
    """
    Function to count the number of words in a given text.
    :param text: Input string (sentence or paragraph).
    :return: Word count as an integer.
    """
    words = text.split()  # Split the text into words using whitespace
    return len(words)

def main():
    """
    Main function to run the Word Counter program.
    Handles input, processing, and output.
    """
    print("Welcome to the Word Counter!")
    while True:
        # Prompt user for input
        user_input = input("Please enter a sentence or paragraph (or type 'exit' to quit): ").strip()
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Thank you for using the Word Counter. Goodbye!")
            break
        
        # Check for empty input
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        
        # Count words
        word_count = count_words(user_input)
        print(f"The number of words in your text is: {word_count}\n")

if __name__ == "__main__":
    main()
