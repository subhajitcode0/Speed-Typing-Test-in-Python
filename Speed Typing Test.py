import random
import time

# List of words for the typing test
word_list = ['Dict','List','Tuple','Set','Deque','NamedTuple','Pattern','Match','Text','Optional','Sequence','Iterable','Mapping','Mutablemapping']

# Function to calculate words per minute (WPM)
def calculate_wpm(start_time, end_time, typed_words):
    elapsed_time = end_time - start_time
    wpm = (len(typed_words) / 5) / (elapsed_time / 60)
    return wpm

# Function to run the typing test
def typing_test():
    # Randomly select a word from the list
    word_to_type = random.choice(word_list)

    # Display the selected word and instructions
    print("Type the following word as fast as you can:")
    print(word_to_type)

    # Wait for the user to start typing
    input("Press Enter when you're ready to start...")

    # Record the start time
    start_time = time.time()

    # Get user input
    user_input = input("Type the word: ")

    # Record the end time
    end_time = time.time()

    # Calculate WPM
    wpm = calculate_wpm(start_time, end_time, user_input)

    # Check if the typed word matches the selected word
    if user_input == word_to_type:
        print(f"Congratulations! Your typing speed is {wpm:.2f} WPM.")
    else:
        print("Sorry, you typed the word incorrectly.")

if __name__ == "__main__":
    while True:
        typing_test()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

