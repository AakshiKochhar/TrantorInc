""" This program will ask the user to answer a bunch of questions."""

questions = {"What is the fifth month of the year?": "May",
             "How many days in a leap year?": "366",
             "2 + 5 =": "7",
             "True/False - Eleven is a prime number.": "True",
             "True/False - 5449 is a prime number.": "True",
             "1230 * 3084 =": "3793320",
             "What is the 17th letter of the alphabet?": "Q",
             "True/False - The 29th letter of the Greek alphabet is Tau.": "False",
             "How many legs does a butterfly have?": "6",
             "8 * 120 =": "960",
             "True/False - The hashtag symbol is technically called an octothorpe.": "True",
             "True/False - Some cats are allergic to people.": "True",
             "6869055 - 75594 =": "679346",
             "True/False - Scotland's national symbol is the unicorn.": "True",
             "True/False - M&M stands for Mars & Milkyway.": "False",
             "True/False - The odds of getting a royal flush are exactly 1 in 649740.": "True",
             "(500 * (15 / (5 + 10)) - 3520) ** 2 =": "9120400",
             "True/False - There are 15820024210 possible ten-card hands in gin rummy.": "False",
             "What is a baby puffin is called?": "Puffling",
             "6 * 6549 =": "39294",
             "True/False - The reason a bug is called a bug in CS is due to a bug being found in a computer.": "True",
             "6869055 % 75594 =": "65595"
             }


def user_response(func):
    """ Calculate and check total amount of questions correctly
    answered.
    """
    def game():
        """Will ask the user questions and keep track of correct
        answers.
        """
        func()
        counter = 0
        for (key, value) in questions.items():
            answer = input(key)
            if answer == value:
                print("CORRECT\n")
                counter += 1        # If answer is correct, increment.
            else:
                print("WRONG. The answer is", value, "\n")
                continue
        total_questions = counter
        print("BONUS QUESTION")
        my_list = [1, 3, 6, 10]
        print(my_list)
        print(input("\nWhat is the sum of the above mentioned list?"))
        answer = sum(x**2 for x in my_list)         # Generator expression as bonus question.
        if answer == 146:
            print("CORRECT!")
            counter += 1
            total_questions = counter       # Increment one last time.
        else:
            print("Sorry, that is incorrect. The correct answer is 146.")
        print("You have answered all questions.\n")
        print("Correct answers:", total_questions, "out of 22 "
                                                   "questions.")
        percentage = (total_questions / 23) * 100
        print("Percentage: ", format(percentage, '.2f'), "%")
    return game


@user_response      # Same as: to_be_used = user_response(to_be_used)
def to_be_used():
    """Welcome user to the game."""
    print("Welcome to the question game. Lets "
          "start:\n")


to_be_used()
