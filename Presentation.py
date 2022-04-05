# Imports
import random
import sys
from datetime import datetime
from time import sleep as wait
from colored import Text, align


# Starts the tutorial
def start(wait_time):

    # Prints the title: #####=|=-+ GAME TUTORIAL +-=|=##### in a frame
    print(Text.Color.purple_1a + " " + "_"*75)
    print(Text.Style.Bold + Text.Color.medium_purple_2a + "|                   #####=|=-+" + Text.Color.medium_purple + " GAME TUTORIAL " + Text.Color.medium_purple_2a + "+-=|=#####                     |")
    print(Text.Color.purple_1a + " " + "‾" *75)

    # Prints the target of the game and how the game works
    print(Text.Color.orange_1 + "\n\nYour target is to get as many points as you can to become #1.")
    print("You can do that by setting the biggest gap between the max range and the minimum range")

    # Prints the credits
    print(Text.Color.gold_1 + Text.Style.Bold + Text.Style.UnderLined + "Created By Ilai K\n" + Text.Style.Reset)

    # Puts the input for ("Type 'Y' when you are ready to start type 'N' to go back and EDIT to edit the delay: ")
    # into user_input
    user_input = input(Text.Color.aquamarine_1a + "Type 'Y' when you are ready to start type 'N' to go back and "
                                                  "'EDIT' to edit the delay: ")

    # Checks if the user typed 'y'
    if user_input.lower() == "y":

        # Prints "Lets start!" waits 0.7 sec and then prints 27 lines down
        print(Text.Color.green_4 + "Let's Start!\n")
        wait(0.7)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        # Prints (If you type 'See scoreboard' you will see the next steps) (comment) and then waits 0.25 sec
        print(Text.Short.Comment + "\tIf you type 'See scoreboard' you will see the next steps")
        wait(0.25)

        # Calls simulate_answer and passes (Start / See leader board / Tutorial / Generate leader board:  ) as
        # the question, (see scoreboard) as the answer and wait_time as the wait_time
        simulate_answer(Text.Style.Reset + Text.Short.Options + "Start / See leader board / Tutorial / Generate leader"
                                                                " board:  ", "see scoreboard", wait_time)

        # Calls simulate_answer and passes (Continue / Go Back: ) as the question, (Continue)
        # as the answer and wait_time as the wait_time
        simulate_answer(Text.Short.Options + "Continue / Go Back: ", "Continue", wait_time)
        wait(wait_time)

        # Calls simulate_answer and passes (How many spot would you like to see (Max: 12): ) as the question, (3)
        # as the answer and wait_time as the wait_time and then waits 0.2 sec
        simulate_answer(Text.Short.Question + "How many spot would you like to see (Max: 12): ", "3", wait_time)
        wait(0.2)

        # Prints (--==+|𝙎𝘾𝙊𝙍𝙀𝘽𝙊𝘼𝙍𝘿|+==--) and then waits 0.25 sec
        print('\n' + Text.Color.purple_1a + Text.Style.Bold + "--==+|" + Text.Color.orchid + '\x1B[23m1`'+
              "SCOREBOARD" + Text.Color.purple_1a + "|+==--\n")
        wait(0.25)

        # Prints (1.  2021-07-13 | Name: Demo1 | Score: 16) as demo and then waits 0.25 sec
        print(Text.Color.light_green_2 + Text.Style.UnderLined + "1." + Text.Style.Reset + "  " +
              Text.Color.green_3b + "2021-07-13 | Name: Demo1 | Score: 16")
        wait(0.25)

        # Prints (2.  2021-07-13 | Name: Demo2 | Score: 15) as demo and then waits 0.25 sec
        print(Text.Color.yellow_1 + Text.Style.UnderLined + "2." + Text.Style.Reset + "  " +
              Text.Color.orange_1 + "2020-07-13 | Name: Demo2 | Score: 15")
        wait(0.25)

        # Prints (3.  2020-06-2 | Name: Demo3 | Score: 14) as demo and then waits 0.25 sec
        print(Text.Color.red + Text.Style.UnderLined + "3." + Text.Style.Reset + "  " +
              Text.Color.light_blue + "2020-06-2 | Name: Demo3 | Score: 14")
        wait(0.25)

        # Prints a long line
        print(Text.Color.purple_1a + Text.Style.Bold + Text.Style.UnderLined + "-------------------------------"
                                                                               "-------------------------------"
                                                                               "-------------------------------"
                                                                               "----------\n")

        # Waits 0.7 sec
        wait(0.7)

        # Prints (And then you'll go back to Start / See ScoreBoard) and then waits 1 sec
        print(Text.Short.Comment + "\tAnd then you'll go back to Start / See ScoreBoard")
        wait(1)

        # Prints (If you type 'Start' it will start the game.. here is a little demo) and then waits 0.7 sec
        print(Text.Short.Comment + "\tIf you type 'Start' it will start the game.. here is a little demo")
        wait(0.7)

        # Calls simulate_answer and passes (Start / See leader board / Tutorial / Generate leader board: )
        # as the question, (Start) as the answer and wait_time as the wait_time and then waits 0.25 sec
        simulate_answer(Text.Short.Options + "Start / See leader board / Tutorial / Generate leader boartd: ", "Start",
                        wait_time)
        wait(0.25)

        # Calls simulate_answer and passes (What is your name: )  as the question, (Tutorial123) as the answer
        # and wait_time as the wait_time
        simulate_answer(Text.Short.Options + "What is your name: ", "Tutorial123", wait_time)

        # Prints (Name registered!) and waits 0.25 sec
        print(Text.Short.SuccessGold + "\tName registered!\n")
        wait(0.25)

        # Calls simulate_answer and passes (Set the maximum value for the range:  )  as the question, (6) as the answer
        # and wait_time as the wait_time
        simulate_answer(Text.Short.Question + "Set the maximum value for the range:  ", "6", wait_time)

        # Prints (Valid input!) and then waits 0.1 sec
        print(Text.Short.SuccessGold + "Valid Input!")
        wait(0.1)

        # Calls simulate_answer and passes (Set the minimum value for the range:  )  as the question, (1) as the answer
        # and wait_time as the wait_time
        simulate_answer(Text.Short.Question + "Set the minimum value for the range:  ", "1", wait_time)
        print(Text.Short.SuccessGold + "Valid Input!")

        # Waits 0.4 sec then prints (Random number created!) and then waits 1 sec
        wait(0.4)
        print(Text.Short.Message2 + "Random number created!\n\n")
        wait(1)

        # Sets now to the current date (format: {Y}-{m}-{d})
        now = datetime.now()
        now = (now.strftime("%Y-%m-%d"))

        # Calls simulate_answer and passes (What is your guess: )  as the question, (2) as the answer
        # and wait_time as the wait_time
        simulate_answer(Text.Short.Question + "What is your guess: ", "2", wait_time)

        # Prints (WOW you did it! You are on the scoreboard now!) and then waits 0.5 sec
        print(Text.Short.Success + "WOW you did it! You are on the scoreboard now!\n\n")
        wait(0.5)

        # Prints (--==+|𝙎𝘾𝙊𝙍𝙀𝘽𝙊𝘼𝙍𝘿|+==--) and then waits 0.25 sec
        print('\n' + Text.Color.purple_1a + Text.Style.Bold + "--==+|" + Text.Color.orchid + '\x1B[23m1`'+
              "SCOREBOARD" + Text.Color.purple_1a + "|+==--\n")
        wait(0.25)

        # Prints (1.  2021-07-13 | Name: Demo1 | Score: 16) and then waits 0.25 sec
        print(Text.Color.light_green_2 + Text.Style.UnderLined + "1." + Text.Style.Reset + "  " +
              Text.Color.green_3b + "2021-07-13 | Name: Demo1 | Score: 16")
        wait(0.25)

        # Prints (2.  2021-07-13 | Name: Demo2 | Score: 15) and then waits 0.25 sec
        print(Text.Color.yellow_1 + Text.Style.UnderLined + "2." + Text.Style.Reset + "  " +
              Text.Color.orange_1 + "2020-07-13 | Name: Demo2 | Score: 15")
        wait(0.25)

        # Prints (3.  2020-06-2 | Name: Demo3 | Score: 14) and then waits 0.25 sec
        print(Text.Color.red + Text.Style.UnderLined + "3." + Text.Style.Reset + "  " +
              Text.Color.red_3a + "2020-06-2 | Name: Demo3 | Score: 14")
        wait(0.25)

        # Prints (4.  2020-06-2 | Name: Demo4 | Score: 12) and then waits 0.25 sec
        print(Text.Color.blue + Text.Style.UnderLined + "4." + Text.Style.Reset + "  " +
              Text.Color.light_blue + "2020-06-2 | Name: Demo4 | Score: 12")
        wait(0.25)

        # Prints (5.  2021-05-1 | Name: Demo5 | Score: 12) and then waits 0.25 sec
        print(Text.Color.blue + Text.Style.UnderLined + "5." + Text.Style.Reset + "  " +
              Text.Color.light_blue + "2021-05-1 | Name: Demo5 | Score: 12")
        wait(0.25)

        # Prints 3 donts verticly
        print(Text.Color.blue + "•\n•\n•")

        # Prints 9.  {now (wich is the current date)} | Name: Tutorial123 | Score: 6
        print(Text.Color.blue + Text.Style.UnderLined + "9." + Text.Style.Reset + "  " +
              Text.Color.light_blue + now + "| Name: Tutorial123 | Score: 6")

        # Prints a long line
        print(Text.Style.Bold + Text.Color.purple_1a + Text.Style.UnderLined + "-------------------------------"
                                                                               "-------------------------------"
                                                                               "-------------------------------"
                                                                               "----------\n")

        # Prints the user's place (9th)
        print(Text.Color.deep_sky_blue_3a + "You are the " + Text.Color.yellow + "9th" +
              Text.Color.deep_sky_blue_3a + " place! you are on the top 50\n")

        # Sets done to False
        done = False

        # Loops while done is False (until down will be equal to True)
        while done is False:

            # Sets user_input as the input for (Do you want to play? Y/N: )
            user_input = input(Text.Color.orange_1 + "Do you want to play?" + Text.Color.green_4 + " Y"  "/" +
                               Text.Color.red_3b + "N: ")

            # Checks if the user typed y (wich means he wants to play)
            if user_input.lower() == "y":

                # Sets done to True so it will stop looping
                done = True

                # Prints 90 lines down
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                      "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                      "\n\n\n")

                # Goes back to call_pres()
                return

            # Checks if the user has typed n (wich means he doesnt want to play)
            elif user_input.lower() == "n":

                # Prints (Thank you for playing!) and quits the program
                print(Text.Color.green_4 + "Thank you for playing!")

            # Checks if the user has typed ?help insted of y/n
            elif user_input.lower() == "?help":

                # Prints the help for this stage (do you want to play)
                print(Text.Short.Comment + "Enter 'Y' if you want to play the game from the start, enter 'N' if "
                                           "you want to Exit the program")

            # Checks if the user didn't type y/n/?help
            else:

                # Prints an error that says Unknown command and sets done to False to it would keep looping
                print(Text.Short.Error + "Unknown command you can type 'y' or 'n' or ?help for help\n")
                done = False

    

    # If the user typed n (wich means he wants to go back)
    elif user_input.lower() == "n":

        # Goes back to call_pres()
        return

    

    # Checks if the user typed ?help insted of y/n/edit
    elif user_input.lower() == "?help":

        # Prints the help for this stage (y to start n to go back and edit to edit delay) and then waits 0.25 sec
        print(Text.Short.Comment + "Enter 'Y' to start the presentation (it will last about 30 seconds) enter 'N' if "
                                   "you want to go back and 'EDIT' if you want to chnage the timing between letters")
        start(0.25)

    

    # Checks if the user typed edit
    elif user_input.lower() == "edit":

        # Prints (here you can edit the delay)
        print(Text.Short.Comment + "Here you can edit the delay")

        # Sets time_input as the input for (What delay do you want between every letter? (max recommanded 0.3,
        # recommanded 0.25): )
        time_input = input(Text.Short.Question + "What delay do you want between every letter? (max recommanded "
                                                 "0.5, recommanded 0.3): ")

        # Calls check_if_number and passes time_input and False (if it would show if its int or float) if it returns
        # True and time_input is bigger than 0 and smaller than 10 (wich would be 10 sec)
        if check_if_number(time_input, False) and 0.1 < float(time_input) < 10:

            # Prints (Time set!)
            print(Text.Short.Success + Text.Style.Bold + "Time set!")

            # Calls start and passes time_input with it so it would be wait_time
            start(float(time_input))

        

        # Checks if the user has typed ?help insted of a number
        elif user_input.lower() == "?help":

            # Prints the help for this stage (what delay between every letter) and waits 0.25 sec
            print(Text.Short.Comment + "Here you need to put the delay between every letter then is being typed "
                                       "by the demo")
            start(0.25)

        

        # Checks if the user didn't eneter a valid number OR ?help
        else:

            # Prints an error that says Invalid input! and then waits 0.25 sec
            print(Text.Short.Error + "Invalid input! It has to be a valid number that is bigger than 0 and "
                                     "smaller than 10 type ?help for help")
            start(0.25)

    

    # Checks if the user didn't enter y/n/edit
    else:

        # Prints an error that says Unknown input and then waits 0.25 sec
        print(Text.Short.Error + "Unknown input! you can enetr 'y', 'n' or ?help for help")
        start(0.25)

########################################################################################################################


# Simulates the answer (like real typing)
def simulate_answer(question, answer, wait_time):

    # Sets counter to 0 and waits 0.2 sec
    counter = 0
    wait(0.2)

    # Prints (question) wich is the first input when calling the function
    # (simulate_answer(question => "test: ", answer => "yay", wiat_time => delay))
    sys.stdout.write(question)

    # Resets answer_comb to "" (nothing)
    answer_comb = ""

    # Loops through every letter in answer and sets it to char
    for char in answer:

        # Checks if wait time smaller or equal to 2.5
        if wait_time <= 2.5:

            # Sets randomtime to a random number between wait_time and wait_time + 0.5
            randomtime = random.uniform(wait_time, wait_time + 0.5)

        

        # Checks if wait_time is bigger or equal to 3
        elif wait_time >= 3:

            # Sets randomtime to a random number between wait_time - 0.5 and wait_time + 0.7
            randomtime = random.uniform(wait_time - 0.5, wait_time + 0.7)

        

        # Checks if wait_time is between 2.5 and 3
        else:

            # Sets randomtime to a random number between wait_time - 0.2 and wait_time + 0.7
            randomtime = random.uniform(wait_time - 0.2, wait_time + 0.7)

        

        # Waits randomtime
        wait(randomtime)

        # Checks if counter is not 0
        if counter != 0:

            # Checks if answer is a decimal (number)
            if answer.isdecimal():
                # Waits 0.7 sec
                wait(0.7)
            

            # Checks if the index counter - 1 of answer is a not a number (a letter)
            # and the index counter of answer is a number
            if answer[counter - 1].isalpha() and answer[counter].isdecimal():

                # Sets randomtime to a random number betwen 0.3 and 0.5
                randomtime = random.uniform(0.3, 0.5)

                # Waits randomtime
                wait(randomtime)

                # Checks if the leangth of answer is bigger than counter and the index counter + 1 of answer is a number
                if len(answer) > counter and answer[counter + 1].isdecimal():
                    # Sets randomtime to a random number between 0.7 and 0.85
                    randomtime = random.uniform(0.7, 0.85)

                    # Waits randomtime
                    wait(randomtime)

        

            # if the index counter - 1 of answer is a number or the index counter of answer is a letter it checks if the
            # leangth of answer is bigger than counter and counter is bigger than 0 and the index counter - 1 of answer
            # is a number and the index counetr of answer is a letter
            elif len(answer) > counter > 0 and answer[counter - 1].isdecimal() and answer[
                 counter].isalpha():

                # Sets randomtime to a random number between 0.25 and 0.45
                randomtime = random.uniform(0.25, 0.45)

                # Waits randomtime
                wait(randomtime)
            

        # Sets answer_comb (answer_combination) to itself + the current processed char
        answer_comb = answer_comb + char

        # Overwrites the last print if there was 1 (because of \r) with wuestion + answer_comb
        sys.stdout.write('\r' + question + Text.Color.green + answer_comb)

        # Adds 1 to counter
        counter = counter + 1

    # Waits 0.4 sec then prints 1 new line and returns to start
    # (more specifically the line that the function was called from)
    wait(0.4)
    print("\n")
    return

########################################################################################################################


# Checks if the input of the delay is a number (whole number or decimal)
def check_if_number(time_input, showtype):
    # Sets float_var and int_var to time_input
    float_var = time_input

    float_num = 0

    # If there is an error from converting float_var to a float ignore it and put it into float_error
    try:
        float_num = float(float_var)
    except ValueError as float_error:

        # Checks if there was an error in float_error
        if float_error is not None:

            # Sets float_num and int_num to a string so it would print an error
            float_num = "sfd"

    

    # Checks if showtype is True
    if showtype:

        # Checks if float_num is a float
        if isinstance(float_num, float):

            # Returns "f" to where the function was called from
            return "f"

        # Checks if float_num is not a float
        else:

            # returns False to where the function was called from
            return False

    

    # Checks if showtype is not equal to True
    else:

        # Checks if float_num is a float (number)
        if isinstance(float_num, float):

            # Returns True to where the function was called from
            return True

        
        else:

            # Returns False to where the function was called from
            return False

########################################################################################################################
