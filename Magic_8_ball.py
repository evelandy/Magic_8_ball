import random
import time
import sys


def main():
    """
        Main menu function, welcomes user then starts the
        game or depending user input
    """
    welcome = '\t\tWelcome to the Magic 8 ball...'
    deco = ((len(welcome) * '=') * 2)
    print("{}\n{}\n{}\n".format(deco, welcome, deco))
    time.sleep(1)
    choice = input('Press [a] to ask a question\nPress [q] to quit\n: ')
    if choice.lower() == 'a':
        question()
    elif choice.lower() == 'q':
        print("Come back soon...")
        sys.exit()
    else:
        print("I do not understand your response... Please try again...")
        sys.exit()


def replay():
    """
        Replay function, asks user if they want to play
        again restarts game quits depending on user input
    """
    rep = input("Press [a] to ask another question\nPress [q] to quit\n: ")
    if rep.lower() == 'a':
        question()
    elif rep.lower() == 'q':
        print("Thank you come back soon..")
        sys.exit()
    else:
        print("I do not understand your response... Please try again...")
        sys.exit()


def question():
    """
        Question function, after user input this function the
        response and prints the returned result to the then
        calls the replay function 
    """
    input('Ask your question and press the [Enter] button.')
    answer = response()
    print('\nAsking the spirits...')
    for thought in range(3):
        print('.', end='')
        time.sleep(1)
    print("\n{}\n".format(answer))
    replay()


def response():
    """
        Response function, which holds a list of possible
        answers. when called function uses the random module
        and randomly chooses an answer from the and returns
        the choice
    """
    response_list = ['Yes', 'No', 'My sources point to yes', 'Maybe', 'The outcome does not look good',
                     "I can't say for sure", "Perhaps", "Don't count on it", "Everything is blurry... Ask again...",
                     "The spirits say... Yes", "The spirits say... No", "Chances are not good", "Chances are good",
                     "I think not", "No straight answer...", "You can count on it", "The outcome looks good",
                     "My sources point to... No", "I think so", "The spirits have left... Try again in a moment...",
                     "If I were you, I would bet on it.", "If I were you I wouldn't bet on it."]
    return random.choice(response_list)


if __name__ == "__main__":
    print(main())
