import random
import time

# List of words for the typing test
word_list = ["The word forest broadly describes an area that has a large number of trees. There are three general types of forest that exist: temperate, tropical, and boreal. Experts estimate that these forests cover approximately one-third of Earth's surface", "The forests provide homes for people around the world", "Forests are natural habitats for many animals. The trees supply oxygen to the atmosphere. They affect the rainfall in a particular region. They also provide us with wood, medicines, food, perfumes, paper, clothes, etc", " forest is a large green wild area that grows naturally.", "Forests are a diverse ecosystem on Earth that includes trees, shrubs, grasses, and other plants. Trees and plants make up a large portion of the forest. Forests are essential not only for human beings but also for all animals. But we rarely understand the depth of its importance for our survival.", "As per Article 48A, the state shall make laws to protect and improve the environment to safeguard the forests of our country. According to Article 51A(g), it is the duty of every citizen of India to protect and improve the natural environment including the forests of our country.", "typing", "test", "openai"]

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

