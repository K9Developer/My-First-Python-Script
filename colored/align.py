import math
from colored import Text
import difflib
from colored import render_count
from colored import Log
import re

#Calls the print_frame_text() function
def align(string="", align="left", top_color = None, middle_color = None, bottom_color = None, width=24, top_char = "—", bottom_char = "—", middle_char = "┃", show_frame=True, offset_plus=0):
    print_frame_text(string, align, top_color, middle_color, bottom_color, width, top_char, bottom_char , middle_char, show_frame, offset_plus)



def print_frame_text(string, align, top_color, middle_color, bottom_color, width, top_char, bottom_char , middle_char, show_frame, offset_plus):

    # Checks if show_frame is false wich means the frame wont show
    if show_frame == False:

        # Sets the symbols for the frame to nothing
        bottom_char = ""
        top_char = ""
        middle_char = ""

    # Sets the colors's defaults
    if middle_color != None and bottom_color == None and top_color == None:
        bottom_color = middle_color
        top_color = middle_color
    elif middle_color != None and bottom_color != None and top_color == None:
        top_color = bottom_color
    elif middle_color == None and bottom_color != None and top_color == None:
        middle_color = bottom_color
        top_color = bottom_color
    elif middle_color == None and bottom_color != None and top_color != None:
        bottom_color = top_color
    elif middle_color == None and bottom_color == None and top_color != None:
        bottom_color = top_color
        middle_color = top_color
    elif middle_color != None and bottom_color == None and top_color != None:
        bottom_color = top_color
    elif middle_color == None and bottom_color == None and top_color == None:
        middle_color = Text.Color.black
        top_color = Text.Color.black
        bottom_color = Text.Color.black

    # If width is nothing it sets it to 24
    if width == None:
        width = 24

    # If for example the user types cneter as the align insted of center it will fix it and removes the unnecessary extras
    align = difflib.get_close_matches(align.lower(), (["center", "right", "left"]), n=1, cutoff=0.6)
    align = str(align).replace('[', "")
    align = str(align).replace(']', "")
    align = str(align).replace('\'', "")

    # Sets stringlen to 0
    stringlen = 0

    # Sets stringlen to the leangth of string
    string_len = len(string)

    # If align is none wich means the user didnt put right/left/center
    if align == None:
        align = "left"

    # Checks if the align is center
    if align.lower() == "center":

        # Sets the vars
        counetr = 0
        string2 = ""
        middle_str = string

        # Sets the top var to what the top of the frame would look like
        top = top_color + " " + top_char*(width*2+round(offset_plus/2) + len_no_ansi(string))

        # Sets the bottom var to what the bottom of the frame would look like
        bottom = bottom_color + " " + bottom_char*(width*2 +round(offset_plus/2) + len_no_ansi(string))

        # Prints the top
        print(top)

        print(middle_color + middle_char + " "*(width-1) + string + " "*(width-1) + middle_color + middle_char + Text.Style.Reset)
        print(bottom)

    elif align.lower() == "left":
        counetr = 0
        for char in string:
            if char.isalpha():
                counetr = counetr + 1
        print(top_color + top_char * (width + len_no_ansi(string)))
        print(middle_color + middle_char + string + " " * (width-6) + middle_color + " " + middle_char + Text.Style.Reset)
        print(bottom_color + bottom_char * (width  + len_no_ansi(string)))
    elif align.lower() == "right":
        counetr = 0
        for char in string:
            if char.isalpha():
                counetr = counetr + 1
        print(top_color + top_char * (width + len_no_ansi(string)))
        print(middle_color + middle_char + " " * (width-3) + string + middle_color + " " + middle_char + Text.Style.Reset)
        print(bottom_color + bottom_char * (width  + len_no_ansi(string)))





def len_no_ansi(string):
    return len(re.sub(
        r'[\u001B\u009B][\[\]()#;?]*((([a-zA-Z\d]*(;[-a-zA-Z\d\/#&.:=?%@~_]*)*)?\u0007)|((\d{1,4}(?:;\d{0,4})*)?[\dA-PR-TZcf-ntqry=><~]))', '', string))
