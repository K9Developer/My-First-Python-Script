# Imports
import difflib
import os
import random
import sys
from datetime import datetime
from time import sleep as wait
from colored import Text
import Presentation
import ScoreBoardGenerator

# wrs

# Starts the presentation (tutorial)
def call_pres():
    # Calls Presentation.start() and passes 0.21 with it wich is the default delay
    Presentation.start(0.21)

    # Calls ask_for_command()
    ask_for_command()


########################################################################################################################

# At the start prints (You can use '?help' in any step if you don't understand what you need to do)
print(
    Text.Short.SuccessGold
    + "You can use '?help' in any step if you don't understand what you need to do\n"
)


# Asks the user what to do ("Start / See ScoreBoard")
def ask_for_command():
    # Asks the user what does he want to do (Start / See leader board / Tutorial / Generate leader)
    user_input = input(
        Text.Style.Reset
        + Text.Short.Options
        + "Start / See leader board / Tutorial / Generate leader"
        " board:  " + Text.Short.End
    )

    # If the user chooses to start it calls request_name()
    if (
        user_input.lower() == "start"
        or user_input.lower() == "go"
        or user_input.lower() == "play"
    ):
        request_name()

    # If the user chooses to see the scoreboard it calls see_scoreboard()
    elif (
        user_input.lower() == "see leader board"
        or user_input.lower() == "see"
        or user_input.lower() == "leader board"
        or user_input.lower() == "board"
        or user_input.lower() == "score"
        or user_input.lower() == "scores"
    ):
        see_scoreboard()

    # If the user chooses to start the tutorial it calls call_pres()
    elif (
        user_input.lower() == "tutorial"
        or user_input.lower() == "learn"
        or user_input.lower() == "tut"
    ):
        call_pres()

    # If the user chooses to generate the scoreboard it calls generate_leader_board()
    elif (
        user_input.lower() == "generate leader board"
        or user_input.lower() == "generate"
    ):
        generate_leader_board()

    # If the user types ?help it prints the help for the current stage and then calls ask_for_command()
    elif user_input.lower() == "?help":
        print(
            Text.Short.Comment
            + "You can write Start (To start the game), see scoreboard (to see a certain number "
            "of spots on the leader board), tutorial (to see the tutorial of the game) or "
            "genearte leader board (this command is only allowed for the owner and WILL "
            "gorequire a password)"
        )
        ask_for_command()

    # If the user type none of the above it'll get a suggestion from
    # ["start", "go", "play", "see scoreboard", "see", "scoreboard", "board", "score", "scores"]
    # that is the closest to the input
    else:

        # Sets the suggestions for all the options
        suggestions = difflib.get_close_matches(
            user_input.lower(),
            [
                "start",
                "go",
                "play",
                "see scoreboard",
                "see",
                "scoreboard",
                "board",
                "score",
                "scores",
                "tutorial",
                "learn",
                "tut",
                "generate leader board",
                "generate",
            ],
        )
        suggestions = str(suggestions).replace("[", "")
        suggestions = str(suggestions).replace("]", "")
        suggestions = str(suggestions).replace("'", "")

        # If suggestion is not empty it prints an error that says unknown command and then the suggestions
        if str(suggestions) != "":
            print(
                Text.Short.Input
                + user_input
                + Text.Short.Error_rest
                + " Is an "
                + Text.Short.Error
                + "Unknown Command! "
                + Text.Short.Error_rest
                + "(Suggestions: "
                + suggestions
                + "), you can type "
                + Text.Short.Command
                + "?help"
                + Text.Short.Error_rest
                + " for help\n"
            )

        # Prints an error that says unknown command and then all of the options if the user didn't
        # enter any of the above
        else:
            print(
                Text.Short.Input
                + user_input
                + Text.Short.Error_rest
                + " Is an "
                + Text.Short.Error
                + "Unknown Command! "
                + Text.Short.Error_rest
                + "(Suggestions: start, go, play, see scoreboard, see, "
                "scoreboard, board, score, scores), you can type "
                + Text.Short.Command
                + "?help"
                + Text.Short.Error_rest
                + " for help\n"
            )

        # Calls ask_for_command()
        ask_for_command()


########################################################################################################################

# Generates a leader board for testing
def generate_leader_board():
    # Asks the user for an answer (admin password, go back, ?help)
    user_input = input(
        Text.Short.Admin
        + "Enter the admin password or 'go back' to go back: "
        + Text.Short.End
    )

    # If the user entered the admin's password
    if user_input == "Admin1234":

        # Enters the input for the question (How many spots would you like to generate? (max 8047): ) into user_input2
        user_input2 = input(
            Text.Short.Admin
            + "How many spots would you like to generate? (max 8047): "
            + Text.Short.End
        )

        # if user_input2 is a number and the first index of user_input2 != 0 bigger than 0 and smaller than 5494
        if (
            user_input2.isdecimal()
            and user_input2[0] != "0"
            and 0 < int(user_input2) < 8048
        ):
            # Enters the input for the question (Enter the MINIMUM number for the scoers: ) into user_input1
            user_input1 = input(
                Text.Short.Admin
                + "Enter the MINIMUM number for the scoers: "
                + Text.Short.End
            )

            # If user_input1 is a number and the first index of user input != 0  bigger than 0 and smaller than 10000
            if (
                user_input1.isdecimal()
                and user_input[0] != "0"
                and 0 < int(user_input1) < 10000
            ):

                # Enters the input for the question (Enter the MAXIMUM number for the scoers: ) into user_input
                user_input = input(
                    Text.Short.Admin
                    + "Enter the MAXIMUM number for the scoers: "
                    + Text.Short.End
                )

                # If user_input is a number and the first index of user input != 0 bigger than
                # user_input1 and smaller than 20000
                if (
                    user_input.isdecimal()
                    and user_input[0] != "0"
                    and int(user_input1) < int(user_input) < 20000
                ):

                    # Prints (Generating...) then calls
                    # ScoreBoardGenerator.generate(user_input2, user_input1, user_input) and
                    # when the function ends prints (Generated!) and then calls ask_for_command()
                    Text.Animation.LoadingAnim(
                        string=Text.Color.aquamarine_1a + "Generating...",
                        wait_time=0.21,
                        total_wait_time=3,
                    )
                    sys.stdout.write("\r" + Text.Short.Success + "   Generated!\n")
                    ScoreBoardGenerator.generate(user_input2, user_input1, user_input)
                    ask_for_command()

                # If insted of a number in Max number theres ?help it will print the help for this stage
                # (max number of generator) and then it will call generate_leader_board()
                elif user_input.lower() == "?help":
                    print(
                        Text.Short.Comment
                        + "Here you need to enter what will the maximum number for the scores "
                        "will be for example min = 1 and max = 12 it will generate scores between 1 and 12"
                    )
                    generate_leader_board()

                # If the user enters none of the above in Max it will print an
                # error and will go back to generate_leader_board()
                else:

                    print(
                        Text.Short.Input
                        + user_input
                        + Text.Short.Error_rest
                        + " Is an "
                        + Text.Short.Error
                        + "Invalid Number! "
                        + Text.Short.Error_rest
                        + "it has to be a valid number that "
                        "is bigger than "
                        + Text.Short.VarOrNum
                        + "0"
                        + Text.Short.Error_rest
                        + " and smaller than "
                        + Text.Short.VarOrNum
                        + "20,000"
                        + Text.Short.Error_rest
                        + ", you can type "
                        + Text.Short.Command
                        + "?help"
                        + Text.Short.Error_rest
                        + " for help\n"
                    )

                    generate_leader_board()

            # If insted of a number in Min number theres ?help it will print the help for this stage
            # (min number of generator) and then it will call generate_leader_board()
            elif user_input1.lower() == "?help":
                print(
                    Text.Short.Comment
                    + "Here you need to enter what will the minimum number for the scores will be "
                    "for example min = 1 and max = 12 it will generate scores between 1 and 12"
                )
                generate_leader_board()

            # If the user enters none of the above in Min it will print an
            # error and will go back to generate_leader_board()
            else:
                print(
                    Text.Short.Input
                    + user_input1
                    + Text.Short.Error_rest
                    + " Is an "
                    + Text.Short.Error
                    + "Invalid Number! "
                    + Text.Short.Error_rest
                    + "it has to be a valid number that is bigger than "
                    + Text.Short.VarOrNum
                    + user_input1
                    + Text.Short.Error_rest
                    + " and smaller than "
                    + Text.Short.VarOrNum
                    + "10,000"
                    + Text.Short.Error_rest
                    + " , you can type "
                    + Text.Short.Command
                    + "?help"
                    + Text.Short.Error_rest
                    + " for help\n"
                )

                generate_leader_board()

        # If insted of a number in the question (How many spots would you like to generate? (max 5494): ) the user
        # enetrs ?help it will print the help for this stage (how many sposts will be generated)
        # and then it will call generate_leader_board()
        elif user_input2.lower() == "?help":
            print(
                Text.Short.Comment
                + "Here you need to enter how many spots you want to generate for example if you "
                "want 3 random scores in the leader board enter 3"
            )
            generate_leader_board()

        # If the user enters an invlaid input in the question (How many spots would you like to generate? (max 5494): )
        # it will print an error an will go back to generate_leader_board()
        else:
            print(
                Text.Short.Input
                + user_input2
                + Text.Short.Error_rest
                + " Is an "
                + Text.Short.Error
                + "Invalid Number! "
                + Text.Short.Error_rest
                + "it has to be a valid number that is bigger than "
                + Text.Short.VarOrNum
                + "0"
                + Text.Short.Error_rest
                + " and smaller than "
                + Text.Short.VarOrNum
                + "5494"
                + Text.Short.Error_rest
                + " , you can type "
                + Text.Short.Command
                + "?help"
                + Text.Short.Error_rest
                + " for help\n"
            )

            generate_leader_board()

    # If the user didn't enter the password and insted typed ?help it will show the help for this stage (admin's code)
    # and then will call generate_leader_board()
    elif user_input.lower() == "?help":
        print(
            Text.Short.Comment
            + "You need to enter the admin password to generate a leader board!"
        )
        generate_leader_board()

    # If the user enters go back insted of code (stage: admin's code) it will call ask_for_command()
    elif user_input.lower() == "go back":
        ask_for_command()

    # If the user enters none of the above then it will print an error saying Wrong password
    # and then it will call ask_for_command()
    else:
        print(
            Text.Short.Input
            + user_input
            + Text.Short.Error_rest
            + " Is the "
            + Text.Short.Error
            + "Wrong password! "
            + Text.Short.Error_rest
            + ", you can type "
            + Text.Short.Command
            + "?help"
            + Text.Short.Error_rest
            + " for help\n"
        )

        ask_for_command()


########################################################################################################################

# Shows the user the scoreboard
def see_scoreboard():
    # Asks the user if he wants to continue or go back
    user_input = input(Text.Short.Options + "Continue /Go Back: " + Text.Short.End)

    # Sets suggestions for all options
    suggestions = difflib.get_close_matches(
        user_input.lower(),
        [
            "continue",
            "go back",
            "back",
            "see scoreboard",
            "see",
            "scoreboard",
            "board",
            "score",
            "scores",
        ],
    )
    suggestions = str(suggestions).replace("[", "")
    suggestions = str(suggestions).replace("]", "")
    suggestions = str(suggestions).replace("'", "")

    # If the user chose to continue
    if (
        user_input.lower() == "continue"
        or user_input.lower() == "see scoreboard"
        or user_input.lower() == "see"
        or user_input.lower() == "scoreboard"
        or user_input.lower() == "score"
        or user_input.lower() == "board"
        or user_input.lower() == "scores"
    ):

        # It will count the lines in the file 'ScoreBoard.txt'
        with open("ScoreBoard.txt") as foo:
            num_lines = len(foo.readlines())

        # It will print to the user how many spots he would like to see
        user_input = input(
            Text.Short.Question
            + "How many spots would you like to see (Max: "
            + Text.Color.light_green_2
            + str(num_lines - 2)
            + Text.Short.Question
            + "): "
            + Text.Short.End
        )

        # if the user enters ?help it will print the help of stage (how many spots would the user like to see)
        # and then it will call see_scoreboard()
        if user_input == "?help":
            print(
                Text.Short.Comment
                + "Here you need to set the number of spots you want to see for example if you "
                "would write 3 it would show you the top 3 on the leader board"
            )
            see_scoreboard()

        # If the user entered a number bigger the number of lines (in the file) - 2 and if the
        # input of the user != to a number it will print an error and then will call see_scoreboard()
        if user_input.isdecimal():
            if num_lines - 2 < int(user_input):
                print(
                    Text.Short.Input
                    + user_input
                    + Text.Short.Error_rest
                    + " Is an "
                    + Text.Short.Error
                    + "Invalid Number! "
                    + Text.Short.Error_rest
                    + "it has to be smaller than "
                    + Text.Short.VarOrNum
                    + str(num_lines - 2)
                    + Text.Short.Error_rest
                    + ", you can type "
                    + Text.Short.Command
                    + "?help"
                    + Text.Short.Error_rest
                    + " for help\n"
                )
                see_scoreboard()

            # If the last check is not true
            else:

                # It will print "Printing now..." and then it will wait 2 sec
                Text.Animation.LoadingAnim(string="Printing")
                print()
                print()
                # wait(1.3)

                # It will print --==+|𝙎𝘾𝙊𝙍𝙀𝘽𝙊𝘼𝙍𝘿|+==-- and then will wait 1 sec
                print(
                    Text.Color.purple_1a
                    + Text.Style.Bold
                    + "--==+|"
                    + Text.Color.orchid + '\x1B[23m1`'+
                    "SCOREBOARD"
                    + Text.Color.purple_1a
                    + "|+==--"
                )
                wait(1)

                # Opens and loops through every line in the file 'ScoreBoard.txt'
                with open("ScoreBoard.txt", "r") as file:
                    for i, x in enumerate(file):

                        # Set up vars for the place of the current proccessed player and the other text
                        if 1 <= i <= int(user_input) + 1:
                            place = str(x).partition(".")[1]
                            place = str(x).partition(".")[0] + str(place)
                            x = str(x).partition(".")[2]

                            # If the user wants to print more than 70 it wont do a wait so it wont
                            # take a long time to load
                            if num_lines < 70:
                                wait(0.1)

                            # If the place is 1 it prints the line in green
                            if place == "1.":
                                print(
                                    Text.Color.light_green_2
                                    + Text.Style.UnderLined
                                    + str(place)
                                    + ""
                                    + Text.Style.Reset
                                    + " "
                                    + Text.Color.green_3b
                                    + str(x)
                                )

                            # If the place is 2 it prints the line in yellow
                            elif place == "2.":
                                print(
                                    Text.Color.yellow_1
                                    + Text.Style.UnderLined
                                    + str(place)
                                    + ""
                                    + Text.Style.Reset
                                    + " "
                                    + Text.Color.orange_1
                                    + str(x)
                                )

                            # If the place is 3 it prints the line in red
                            elif place == "3.":
                                print(
                                    Text.Color.red
                                    + Text.Style.UnderLined
                                    + str(place)
                                    + ""
                                    + Text.Style.Reset
                                    + " "
                                    + Text.Color.red_3a
                                    + str(x)
                                )

                            # If the place is not 1,2 or 3 it will print the line in blue
                            else:
                                print(
                                    Text.Color.blue
                                    + Text.Style.UnderLined
                                    + str(place)
                                    + ""
                                    + Text.Style.Reset
                                    + " "
                                    + Text.Color.light_blue
                                    + str(x)
                                )

                        # If the loop counter (i) reaches the number the user typed it will break out of the loop
                        elif i > int(user_input):
                            break

                # Waits 1 sec
                wait(1)

                # Prints a long line (----------------------------...) and then it will call
                # ask_for_command() and close the file
                print(
                    Text.Color.purple_1a
                    + Text.Style.Bold
                    + Text.Style.UnderLined
                    + "-------------------------------"
                    "-------------------------------"
                    "------------------------------"
                )
                ask_for_command()
                file.close()

        # If the number the user typed is bigger then the max number possible it will print an error and then it
        # will call see_scoreboard()
        else:
            print(
                Text.Short.Input
                + user_input
                + Text.Short.Error_rest
                + " Is an "
                + Text.Short.Error
                + "Unknown Number! "
                + Text.Short.Error_rest
                + "it has a valid number, you can type "
                + Text.Short.Command
                + "?help"
                + Text.Short.Error_rest
                + " for help\n"
            )
            see_scoreboard()

    # If the user typed go back it will print Going back...
    # Then it will call ask_for_command()
    elif user_input.lower() == "back" or user_input.lower() == "go back":
        print("Going back...\n")
        ask_for_command()

    # If the user entered ?help it will show the help for this stage (Continue / Go back  |  see scoreboard)
    # and then it will call ask_for_command()
    elif user_input.lower() == "?help":
        print(
            Text.Short.Comment
            + "You can write 'continue' to continue to the scoreboard "
            "OR write 'go back' to go back 1 step"
        )
        ask_for_command()

    # If the user entered none of the above (ERROR)
    else:

        # If the suggestions is not nothing (that means that the input is close enough to any options)
        if str(suggestions) != "":

            # Prints an error with the suggestions
            print(
                Text.Short.Input
                + user_input
                + Text.Short.Error_rest
                + " Is an "
                + Text.Short.Error
                + "Unknown Command! "
                + Text.Short.Error_rest
                + "(suggestions: "
                + suggestions
                + "), you can type "
                + Text.Short.Command
                + "?help"
                + Text.Short.Error_rest
                + " for help\n"
            )

        # If the suggestions == nothing (that means the user didn't type anything close enough to the options)
        else:
            print(
                Text.Short.Input
                + user_input
                + Text.Short.Error_rest
                + " Is an "
                + Text.Short.Error
                + "Unknown Command! "
                + Text.Short.Error_rest
                + "(suggestions: continue, go back, back, see scoreboard,"
                " see, scoreboard, board, score, scores), you can type "
                + Text.Short.Command
                + "?help"
                + Text.Short.Error_rest
                + " for help\n"
            )

        # Calls see_scoreboard()
        see_scoreboard()


########################################################################################################################


# Asks For user name
def request_name():
    # Prints (What is your name:  )and replaces every " " with "" so it will replace all spaces with nothing
    user_name = input(
        Text.Style.Reset + Text.Short.Question + "What is your name: " + Text.Short.End
    )
    user_name.replace(" ", "")

    # If insted of the name the user has entered ?help it will print the help for this stage (request username)
    # and then it will call request_name()
    if user_name.lower() == "?help":
        print(
            Text.Short.Comment
            + "Here you need to write your username (this username will show on the leader board)"
        )
        request_name()

    # Checks if the user_name's length has passed 20 and is bigger than 1
    if len(user_name) > 20 or len(user_name) < 3:
        # Prints an error that says that the name is too long and then it will call request_name()
        print(
            Text.Short.Input
            + user_name
            + Text.Short.Error_rest
            + " Is an "
            + Text.Short.Error
            + "Invalid Name! "
            + Text.Short.Error_rest
            + "it's length has to be between "
            + Text.Short.VarOrNum
            + "2"
            + Text.Short.Error_rest
            + " and "
            + Text.Short.VarOrNum
            + "20"
            + Text.Short.Error_rest
            + " , you can type "
            + Text.Short.Command
            + "?help"
            + Text.Short.Error_rest
            + " for help\n"
        )
        request_name()

    # Checks if the user has entered the admin command
    if user_name == "Admin5792Reset":
        # Removes the scoerboard then creats it and prints (Leader Board CLEARED!) and calls request_name()
        os.remove("ScoreBoard.txt")
        scoreboard = open("ScoreBoard.txt", "w")
        scoreboard.close()
        print(Text.Short.Admin + "Leader Board CLEARED!")
        request_name()

    # Checks if the user_name containes '|'
    if user_name.find("|") != -1:
        # Prints an error that says Invalid name and then calls request_name()
        print(
            Text.Short.Input
            + user_name
            + Text.Short.Error_rest
            + " Is an "
            + Text.Short.Error
            + "Invalid Name! "
            + Text.Short.Error_rest
            + "please choose another, you can type "
            + Text.Short.Command
            + "?help"
            + Text.Short.Error_rest
            + " for help\n"
        )
        request_name()

    # Opens file as my_file
    with open("ScoreBoard.txt") as my_file:

        # Loops through every line in the file
        for line in my_file:

            # Cuts line so it would be ONLY the name in the line
            line = line.split("Name: ")[-1]
            line = line.split("|")[0]

            # Checks if the line contains the user_name
            if line.lower() == user_name.lower() + " ":
                # Prints an error that says Name already exists
                print(
                    Text.Short.Input
                    + user_name
                    + Text.Short.Error_rest
                    + " Is an "
                    + Text.Short.Error
                    + "Invalid Name! "
                    + Text.Short.Error_rest
                    + " the name already exists please try another, you can type "
                    + Text.Short.Command
                    + "?help"
                    + Text.Short.Error_rest
                    + " for help\n"
                )

                # Closes the file and calls request_name()
                my_file.close()
                request_name()

    # Prints (Name registered!) if the checks have passed and goes to  input_range_max()
    # and passes user_name to it
    print(Text.Short.SuccessGold + " Name registered! ")
    print("")
    input_range_max(user_name)


########################################################################################################################

# Sets the max range
def input_range_max(user_name):
    # Prints (Set the maximum value for the range: ) and puts input into user_input_max
    user_input_max = input(
        Text.Short.Question + "Set the maximum value for the range: " + Text.Short.End
    )

    # If the user has typed ?help insted of the number
    if user_input_max == "?help":
        # Prints the help for this stage (max value) and calls input_range_max() and passes user_name with it
        print(
            Text.Short.Comment
            + "Here you need to set the max number that it will randomize to for example\n the "
            "minimum number is 1 and the max is 10 it will randomize a number between 1 and 10"
        )
        input_range_max(user_name)

    # If the user_input_max is a number bigger than 0 and the first index of user_input_max != to 0
    if (
        user_input_max.isdecimal()
        and int(user_input_max) > 0
        and user_input_max[0] != "0"
    ):

        # Prints Valid Input and then calls input_range_minimum() and passes user_input_max and user_name with it
        print(Text.Short.SuccessGold + "Valid Input!")
        input_range_minimum(user_input_max, user_name)

    # If check goes to false
    else:

        # Prints an error and calls input_range_max() and passes user_name with it
        print(
            Text.Short.Input
            + user_input_max
            + Text.Short.Error_rest
            + " Is an "
            + Text.Short.Error
            + "Invalid Number! "
            + Text.Short.Error_rest
            + " type only valid numbers above "
            + Text.Short.VarOrNum
            + "0"
            + Text.Short.Error_rest
            + ", you can type "
            + Text.Short.Command
            + "?help"
            + Text.Short.Error_rest
            + " for help\n"
        )
        input_range_max(user_name)


########################################################################################################################


# Sets the minimum range
def input_range_minimum(user_input_max, user_name):
    # Prints (Set the minimum value for the range: ) and puts input into user_input_min
    user_input_min = input(
        Text.Short.Question + "Set the minimum value for the range: " + Text.Short.End
    )

    # If the user has typed ?help insted of the number
    if user_input_min == "?help":
        # Prints the help for this stage (min value) and calls input_range_min()
        # and passes user_name and user_input_max with it
        print(
            Text.Short.Comment
            + "Here you need to set the minimum number that it will randomize from for example\n"
            " the minimum number is 1 and the max is 10 it will randomize a "
            "number between 1 and 10"
        )
        input_range_minimum(user_input_max, user_name)

    # If the user_input_max is a number bigger than 0 and the first index of user_input_max != to 0
    if user_input_min.isdecimal() and user_input_min[0] != "0":

        # Checks if user_input_min is lower than user_input_max
        if int(user_input_min) < int(user_input_max):

            # Prints (Valid Input!) and then calls random_num() and passes user_input_max and
            # user_name and user_input_min with it
            print(Text.Short.SuccessGold + "Valid Input!")
            print(Text.Short.Message2 + "Random number created!")

            # Waits 1 sec and calls random_num() and passes user_input_max and user_name and user_input_min with it
            wait(1)
            random_num(user_input_max, user_input_min, user_name)

        # If user_input_min is not smaller than user_input_max
        else:

            # Prints an error Invalid Input! and calls input_range_minimum()
            # and passes user_name and user_input_max with it
            print(
                Text.Short.Input
                + user_input_min
                + Text.Short.Error_rest
                + " Is an "
                + Text.Short.Error
                + "Invalid Number! "
                + Text.Short.Error_rest
                + " type only valid numbers below "
                + Text.Short.VarOrNum
                + user_input_max
                + Text.Short.Error_rest
                + ", you can type "
                + Text.Short.Command
                + "?help"
                + Text.Short.Error_rest
                + " for help\n"
            )
            input_range_minimum(user_input_max, user_name)

    # If the user_input_min is not a num OR the first index of user_input_min is 0
    else:

        # Prints an error that says Invalid input! and calls input_range_minimum() and passes user_name and
        # user_input_max with it
        print(
            Text.Short.Input
            + user_input_min
            + Text.Short.Error_rest
            + " Is an "
            + Text.Short.Error
            + "Invalid Number! "
            + Text.Short.Error_rest
            + " type only valid numbers, you can type "
            + Text.Short.Command
            + "?help"
            + Text.Short.Error_rest
            + " for help\n"
        )
        input_range_minimum(user_input_max, user_name)


########################################################################################################################


# Creates a random number between the user_input_max and the user_input_min numbers
def random_num(user_input_max, user_input_min, user_name):
    # Puts a random number between user_input_max and user_input_min into random_number
    random_number = random.randint(int(user_input_min), int(user_input_max))

    # Prints 2 lines down
    print("\n\n")

    # Prints random_number
    print(random_number)

    # Prints (What is your guess: ) and puts the input into guess_input
    guess_input = input((Text.Short.Question + "What is your guess: " + Text.Short.End))

    # If the user types ?help insted of his guess
    if guess_input.lower() == "?help":
        # Prints the help for this stage (guess of random number) calls random_num() and passes
        # user_input_max and user_name and user_input_min with it
        print(
            Text.Short.Comment
            + "Here you need to type your guess.. what do you think the randomized number between "
            + user_input_min
            + " and "
            + user_input_max
            + " If you get it right you will be on the leader board!"
        )
        random_num(user_input_max, user_input_min, user_name)

    # Checks if guess_input is a number
    if guess_input.isdecimal():

        # Checks if the guess_input is equal to random_number (wich means the user has guessed it right)
        if int(guess_input) == int(random_number):

            # Prints (WOW you did it! You are on the scoreboard now!) waits 2 sec and then calls append_to_score_board1
            # and passes user_input_max, user_input_min and user_name with it
            print(Text.Short.Success + "WOW you did it! You are on the scoreboard now!")
            wait(2)
            append_to_score_board1(user_input_max, user_input_min, user_name)

        # If the user didn't guess the number correctly
        else:

            # Prints (OOF you can try again next time the random number was ) + random_number
            print(
                Text.Short.Lose
                + "OOF you can try again next time the random number was "
                + str(random_number)
            )

    # If guess_input is not a number
    else:

        # Prints an error that say Invalid Number!, waits 0.75 sec and then calls append_to_score_board1 and passes
        # user_input_max, user_input_min and user_name with it
        print(
            Text.Short.Input
            + guess_input
            + Text.Short.Error_rest
            + " Is an "
            + Text.Short.Error
            + "Invalid Number! "
            + Text.Short.Error_rest
            + " type only valid numbers as your guess, you can type "
            + Text.Short.Command
            + "?help"
            + Text.Short.Error_rest
            + " for help\n"
        )
        wait(0.75)
        random_num(user_input_max, user_input_min, user_name)

    # Prints 8 lines down
    print("\n\n\n\n\n\n\n\n")

    # Sets done to False
    done = False

    # Loops while done is False (Loops until done is Talse) so it can reapeat the actions
    # within the loop if he answers N
    while done is False:

        # Sets user_input to input for ("Do you want to play again? Y / N)
        user_input = input(
            Text.Color.orange_1
            + "Do you want to play again?"
            + Text.Color.green_4
            + " Y"
            "/" + Text.Color.red_3b + "N: " + Text.Short.End
        )

        # Checks if user_input == ?help
        if user_input.lower() == "?help":
            # Prints the help for this stage (Do you want to play again?)
            print(
                Text.Short.Comment
                + "Enter 'Y' if you want to play the game again from the start, enter 'N' if "
                "you want to Exit the program"
            )

        # Check if user_input == y (that means the user wants to play again)
        if user_input.lower() == "y":

            # Prints 27 lines down
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            # Sets done to True and then calls ask_for_command()
            done = True
            ask_for_command()

        # Check if user_input == n (that means the user doesn't want to play again)
        elif user_input.lower() == "n":

            # Prints (Thank you for playing!) and quits the program
            print(Text.Color.green_4 + "Thank you for playing!")
            sys.exit()

        # Checks if the user didn't type y/n/?help
        else:

            # Prints an error that says Unknown command and sets done to False to it would keep looping
            print(
                Text.Short.Input
                + user_input
                + Text.Short.Error_rest
                + " Is an "
                + Text.Short.Error
                + "Unknown Command! "
                + Text.Short.Error_rest
                + " you can type only "
                + Text.Short.VarOrNum
                + "y"
                + Text.Short.Error_rest
                + ", "
                + Text.Short.VarOrNum
                + "n"
                + ", you can type "
                + Text.Short.Command
                + "?help"
                + Text.Short.Error_rest
                + " for help\n"
            )
            done = False


########################################################################################################################


# Sorts the scoreboard and prints the scoreboard at the end
def append_to_score_board1(user_input_max, user_input_min, user_name):
    # data: scoreboard sorter
    data = []

    # name: spesific words in line of file
    name = []

    # Clears data and words
    data.clear()
    name.clear()

    # Sets now as the date (format: {Y}-{m}-{d})
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    # Opens file as my_file
    with open("ScoreBoard.txt") as my_file:

        # Loops through every line in the file my_file
        for line in my_file:

            # Sets score to an array that containes every word in the line
            score = line.split()

            # Checks if the line is not none or new line or --++==SCOREBOARD==++--
            if (
                line is not None
                and str(line).find("--++==SCOREBOARD==++--") == -1
                and line != "\n"
            ):
                # Sets score as score[last index - 1] wich is the number of the score
                score = score[-1]

                # Sets name as "Name: {name} |"
                name = line[: line.find("Score: ")].strip()
                name = name[name.find("Name: ") :]

                # Appends to data [(date | Name: name | Score: , score)]
                data.append(tuple([str(now) + " | " + name + " Score: ", str(score)]))

    # Closes file my_file
    my_file.close()

    # Removes file ScoreBoard.txt creates it and then appends --++==SCOREBOARD==++-- and 2 lines down to it
    os.remove("ScoreBoard.txt")
    scoreboard = open("ScoreBoard.txt", "w")
    scoreboard.close()
    scoreboard = open("ScoreBoard.txt", "a")
    scoreboard.write("--++==SCOREBOARD==++--")
    scoreboard.write("\n\n")

    # Appends the data of the user to data [(date | Name: user_name | Score: ), (user_input_max - user_input_min + 1)]
    data.append(
        (
            ("" + str(now) + " | Name: " + str(user_name) + " | Score: "),
            (str((int(user_input_max) - int(user_input_min) + 1))),
        )
    )
    # It sorts the array by tup[1] (the score) from the biggest to the smallest
    data.sort(key=lambda tup: int(tup[1]), reverse=True)

    # Loops through every value of data[]
    for t in data:
        # Writes to scoreboard index of value t + 1 in data wich is the place + the text
        # (wich doesn't incloude the score) + score
        scoreboard.write(
            str((int(data.index(t)) + 1)) + ".  " + str(t[0]) + " " + str(t[1]) + "\n"
        )

    # Closes scoreboard and my_file
    scoreboard.close()
    my_file.close()

    # Prints 8 lines down
    print("\n\n\n\n\n\n\n\n")

    # Prints (--==+|𝙎𝘾𝙊𝙍𝙀𝘽𝙊𝘼𝙍𝘿|+==--)
    print(
        Text.Color.purple_1a
        + Text.Style.Bold
        + "--==+||"
        + Text.Color.orchid + '\x1B[23m1`'+
        "SCOREBOARD"
        + Text.Color.purple_1a
        + "||+==--"
    )

    # Wait 1 sec
    wait(1)

    # Sets place to 0
    place = 0

    # Loops through data
    for i, x in data:

        # Updates the counetr (counter + 1)
        place = place + 1

        # Checks if place is smaller than 5 (checks if it didnt print mroe than 5 times so it can print top 5)
        if place <= 5:

            # Checks if place is 1
            if place == 1:

                # Prints the line in green
                print(
                    Text.Color.light_green_2
                    + Text.Style.UnderLined
                    + str(place)
                    + "."
                    + Text.Style.Reset
                    + " "
                    + Text.Color.green_3b
                    + str(i)
                    + str(x)
                    + "\n"
                )

            # Checks if place is 2
            elif place == 2:

                # Prints the line in yellow
                print(
                    Text.Color.yellow_1
                    + Text.Style.UnderLined
                    + str(place)
                    + "."
                    + Text.Style.Reset
                    + " "
                    + Text.Color.orange_1
                    + str(i)
                    + str(x)
                    + "\n"
                )

            # Checks if place is 2
            elif place == 3:

                # Prints the line in red
                print(
                    Text.Color.red
                    + Text.Style.UnderLined
                    + str(place)
                    + "."
                    + Text.Style.Reset
                    + " "
                    + Text.Color.red_3a
                    + str(i)
                    + str(x)
                    + "\n"
                )

            # Checks if place is 5
            elif place == 5:

                # Prints the line in blue without \n
                print(
                    Text.Color.blue
                    + Text.Style.UnderLined
                    + str(place)
                    + "."
                    + Text.Style.Reset
                    + " "
                    + Text.Color.light_blue
                    + str(i)
                    + str(x)
                )

            # Checks if place is none of the above (4)
            else:

                # Prints the line in blue
                print(
                    Text.Color.blue
                    + Text.Style.UnderLined
                    + str(place)
                    + "."
                    + Text.Style.Reset
                    + " "
                    + Text.Color.light_blue
                    + str(i)
                    + str(x)
                    + "\n"
                )

    # Sets score_count and user_place to 0
    score_count = 0
    user_place = 0

    # for tup[0] and tup[1] in data
    for name, tup1 in data:

        # Sets name as the name ("Name: {name} |")
        name = name.split("Name: ")[-1]
        name = name.split("|")[0]

        # Checks if the name from the line in the file is the user_name
        if str(name) == (user_name + " "):

            # Sets user_place as score_count + 1 and then breaks
            user_place = score_count + 1
            break

        # If the name from the line in the file is not the user_name
        else:

            # Adds 1 to score_count (keeps counting)
            score_count = score_count + 1

    # Checks if the user's place (user_place) is bigger than 5 (user is not on the top 5)
    if int(user_place) > 5:
        # Prints 3 dots (•) verticly by printing 1 and going down (repeat 3 times)
        print(Text.Color.blue + "\b•\n•\n•")

        # Prints the user's data in blue
        print(
            Text.Color.blue
            + Text.Style.UnderLined
            + str(user_place)
            + "."
            + Text.Style.Reset
            + " "
            + Text.Color.light_blue
            + now
            + " | "
            + "Name: "
            + user_name
            + " | Score: "
            + str((int(user_input_max) + 1 - int(user_input_min)))
        )

        # Both will look like (Example):
        # •
        # •
        # •
        # 10.  2020-01-02| Name: Joseph | Score:  1

    # Waits 1.5 sec
    wait(1.5)

    # Prints a long line after the top 5
    print(
        Text.Style.Bold
        + Text.Color.purple_1a
        + Text.Style.UnderLined
        + "-------------------------------------------"
        "-------------------------------------------"
        "---------------------------\n"
    )

    # Checks if user_place is in the top 5 (user_place < 6)
    if int(user_place) < 6:

        # Prints (You are the + user_place + place! you are top 5!)  in green
        print(
            Text.Style.Reset
            + Text.Style.Bold
            + Text.Color.deep_sky_blue_3a
            + "You are the "
            + Text.Color.light_green_2
            + str(ordinal(user_place))
            + Text.Color.deep_sky_blue_3a
            + " place! you are on the top 5!\n"
        )

    # Checks if user_place is in the top 50 (user_place < 51)
    elif int(user_place) < 51:

        # Prints (You are the + user_place + place! you are top 50) in yellow
        print(
            Text.Color.deep_sky_blue_3a
            + "You are the "
            + Text.Color.yellow
            + str(ordinal(user_place))
            + Text.Color.deep_sky_blue_3a
            + " place! you are on the top 50\n"
        )

    # If the user_place is none of the above
    else:

        # Prints (You are the + user_place + place! you are top 50)  in red
        print(
            Text.Color.deep_sky_blue_3a
            + "You are the "
            + Text.Color.red
            + str(ordinal(user_place))
            + Text.Color.deep_sky_blue_3a
            + " place!\n"
        )

    # Sets done to False
    done = False

    # Loops while done is False (Loops until done is Talse) so it can reapeat the actions
    # within the loop if he answers N
    while done is False:

        # Sets user_input to input for Do you want to play again? Y / N
        user_input = input(
            Text.Color.orange_1
            + Text.Style.Bold
            + Text.Style.UnderLined
            + "Do you want to play again?"
            + Text.Color.green_4
            + " Y"
            "/" + Text.Color.red_3b + "N: " + Text.Short.End
        )

        # Checks if insted of Y / N he typed ?help
        if user_input.lower() == "?help":
            # Prints the help for the current stage (play again?)
            print(
                Text.Short.Comment
                + "Enter 'Y' if you want to play the game again from the start, enter 'N' if "
                "you want to Exit the program"
            )
            continue

        # Checks if the user typed y (that means he wants to play again)
        if user_input.lower() == "y":

            # Prints 27 lines down
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            # Sets done to True (wich means it won't loop anymore)
            done = True

            # Calls ask_for_command()
            ask_for_command()

        # Checks if the user has typed n (wich means he doesnt want to play again)
        elif user_input.lower() == "n":

            # Prints (Thank you for playing) and quits the program
            print(Text.Color.green_4 + "Thank you for playing!" + Text.Style.Reset)
            sys.exit()

        # Checks if the user didn't type y / n / ?help
        else:

            # Prints an error that says Unknown input and sets done to false so it would keep looping
            print(
                Text.Short.Input
+ user_input
+ Text.Short.Error_rest
+ " Is an "
+ Text.Short.Error
+ "Unknown Command! "
+ Text.Short.Error_rest
+ " you can type only "
+ Text.Short.VarOrNum
+ "y"
+ Text.Short.Error_rest
+ ", "
+ Text.Short.VarOrNum
+ "n"
+ ", you can type "
+ Text.Short.Command
+ "?help"
+ Text.Short.Error_rest
+ " for help\n"
            )
            done = False


########################################################################################################################


# Calls ask_for_command() at the start of the game
ask_for_command()
