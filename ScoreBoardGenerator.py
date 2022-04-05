# Imports
import datetime
import os
from random import randint
from faker import Faker

# Setup
fake = Faker()

# generats the scoreboard to the file
def generate(spots, min_score, max_score):

    # Sets start_date to a date and end_date to a later date
    start_date = datetime.date(year=2020, month=1, day=1)
    end_date = datetime.date(year=2021, month=12, day=10)

    # Calls reset_content
    reset_content()

    # Opens ScoreBoard.txt as f to append to it
    with open('ScoreBoard.txt', 'a') as f:

        # Writes to file --++==SCOREBOARD==++--
        f.write("--++==SCOREBOARD==++--\n")

        # Loops spots times puts the counter in x
        for x in range(int(spots)):

            # Sets date to a random date between start_date and end_date
            date = str(fake.date_between(start_date=start_date, end_date=end_date))

            # Sets randomint to a random number between min_score and max_score
            randomint = str(randint(int(min_score), int(max_score)))

            # Sets name to check_if_name_exist and passes x (counter) with it
            name = check_if_name_exist(x)

            #                 place    date         name          Score
            # Writes to file (x + 1).  date | Name: name | Score: randomint
            f.write(str("\n" + str(x + 1) + ".  " + date + "| Name: " + str(name) + " | Score:  " + randomint))

        # I--------------------------------------------------I

        # Closes the file
        f.close()

        # Calls sort_scoreboard()
        sort_scoreboard()

########################################################################################################################

# Erases the content of the file ScoreBoard.txt
def reset_content():

    # Deletes ScoreBoard.txt
    os.remove("ScoreBoard.txt")

    # Creates ScoreBoard.txt
    scoreboard = open("ScoreBoard.txt", "w")

    # Closes ScoreBoard.txt
    scoreboard.close()

########################################################################################################################

# Returns name from name file
def check_if_name_exist(counter):

    # Opens the file names as f
    with open('names') as f:

        # Sets lines to an array that containes every line in names
        lines = f.readlines()

        # Sets name as the index counter of lines
        name = lines[counter]

        # Sets counetr to counetr + 1
        counter = counter + 1

        # Closes the file names
        f.close()

        # Removes \n (line down) from name
        name = name.strip('\n')

        # Returns the name with capital letter at the start to where this function was called from
        return name.title()

########################################################################################################################

# Sorts the scoreboard
def sort_scoreboard():

    # Sets data and name1 to an array
    data = []
    name1 = []

    # Clears data and name1
    data.clear()
    name1.clear()

    # Opens ScoreBoard.txt as my_file
    with open('ScoreBoard.txt') as my_file:

        # Loops through every line in the file my_file
        for line in my_file:

            # Sets score to an array that containes every word in the line
            score = line.split()

            # Checks if the line is not none or new line or "--++==SCOREBOARD==++--"
            if line is not None and str(line).find("--++==SCOREBOARD==++--") == -1 and line != "\n":

                # Sets score as score[last index - 1] wich is the number of the score
                score = score[-1]

                # Sets name as "Name: {name} |"
                name1 = line[:line.find('Score: ')].strip()
                name1 = name1[name1.find('  '):]

                # Appends to data [tup[0]: (date | Name: name | Score:) , tup[1]: (score)]
                data.append(tuple([name1 + " Score: ", str(score)]))

    # I--------------------------------------------------I

    # Closes file my_file (ScoreBoard.txt)
    my_file.close()

    # Calls reset_content()
    reset_content()

    # Opens ScoreBoard.txt to append as scoreboard
    scoreboard = open("ScoreBoard.txt", "a")

    # Writes to the file "--++==SCOREBOARD==++--" and then writes 2 lines down
    scoreboard.write("--++==SCOREBOARD==++--")
    scoreboard.write("\n\n")

    # Sorts the array data by tup[1] (score) from the highest to the lowest
    data.sort(key=lambda tup: int(tup[1]), reverse=True)

    # Loops through every value in data
    for t in data:
        # Writes to scoreboard index of value t + 1 in data wich is the place + the text
        # (wich doesn't incloude the score) + score
        scoreboard.write(str((int(data.index(t)) + 1)) + "." + str(t[0]) + " " + str(t[1]) + "\n")

########################################################################################################################
